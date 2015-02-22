from django.db import models
from django.db.models import Q

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