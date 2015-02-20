from django.conf.urls import patterns, url
from cards.views import SkillList

from cards import views

urlpatterns = patterns('',
    url(r'^$', SkillList.as_view(), name='skill-index'),
    url(r'^(?P<skill_name>[a-zA-Z ]+)/$', views.skill_view, name='skill'),
)