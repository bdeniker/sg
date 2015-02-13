from django.contrib import admin
from cards.models import Skill, Problem, Card

class CardAdmin(admin.ModelAdmin):
    fields = ['name', 'duration', 'skill', 'problems']
    filter_horizontal = ['problems']
    list_filter = ['skill']
    list_display = ['name', 'skill', 'problems_solved_count']

class ProblemAdmin(admin.ModelAdmin):
    list_filter = ['skill']
    list_display = ['name', 'skill']

admin.site.register(Skill)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Card, CardAdmin)