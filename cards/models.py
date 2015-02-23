from django.db import models
from django.db.models import Q

# NOTE Signals captured in apps.py!

# Natural key managers
class SkillManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class ProblemCardManager(models.Manager):
    def get_by_natural_key(self, name, skill):
        return self.get(name=name,
                        skill=Skill.objects.get_by_natural_key(skill))

# Models
class Skill(models.Model):
    objects = SkillManager()

    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)

class Problem(models.Model):
    objects = ProblemCardManager()

    name = models.CharField(max_length=200)
    skill = models.ForeignKey(Skill)

    def __str__(self):
        return "{} [{}]".format(self.name, self.skill.name)

    def natural_key(self):
        return (self.name,) + self.skill.natural_key()
    natural_key.dependencies = ['cards.skill']

    def solved_by_count(self):
        return self.card_set.all().count()

class Card(models.Model):
    objects = ProblemCardManager()

    name = models.CharField(max_length=200)
    skill = models.ForeignKey(Skill)
    problems = models.ManyToManyField(Problem, null=True, blank=True)
    duration = models.IntegerField(default=0)

    def __str__(self):
        return "{} [{}]".format(self.name, self.skill.name)

    def natural_key(self):
        return (self.name,) + self.skill.natural_key()
    natural_key.dependencies = ['cards.skill', 'cards.problem']

    def problems_solved_count(self):
        return self.problems.all().count()

class Hand(models.Model):
    skill = models.ForeignKey(Skill)
    cards = models.ManyToManyField(Card)
    coverage = models.DecimalField()
    redundancy = models.DecimalField()

    def generate_stats(self):
        # For each problem for this skill, how many cards in this hand cover it
        problems = 0
        coverage = 0
        redundancy = 0

        for problem in Problem.objects.filter(skill=self.skill):
            problems += 1
            cards_solving = Card.objects.filter(
                problems__id__exact=problem.id).count()
            if cards_solving > 1:
                coverage += 1
            redundancy += cards_solving

        return (coverage/problems, redundancy/problems)

    def save(self):
        super(Hand, self).save()
        self.coverage, self.redundancy = self.generate_stats()
        super(Hand, self).save()