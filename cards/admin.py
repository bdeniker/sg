from django.contrib import admin
from cards.models import Skill, Problem, Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    fields = ['name', 'duration', 'skill', 'problems']
    filter_horizontal = ['problems']
    list_filter = ['skill']
    list_display = ['name', 'skill', 'problems_solved_count']

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_filter = ['skill']
    list_display = ['name', 'skill', 'solved_by_count']

admin.site.register(Skill)