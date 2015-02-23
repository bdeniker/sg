from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from cards.models import Skill

class SkillList(ListView):
    model = Skill

def skill_view(request, skill_name):
    skill = get_object_or_404(Skill, name=skill_name)
    return render(request, 'cards/skill_view.html',
                  {'skill': skill,
                   'problems': skill.problem_set.annotate(card_count=Count('card')).order_by('card_count'),
                   'cards': skill.card_set.order_by('duration')})

def card_hands_view(request, skill_name):
    skill = get_object_or_404(Skill, name=skill_name)
    cards = int(request.GET.get('cards', 6))
    hands = int(request.GET.get('hands', 5))
    return render(request, 'cards/card_hands_view.html',
                  {'skill': skill, 'cards': cards, 'hands': hands})