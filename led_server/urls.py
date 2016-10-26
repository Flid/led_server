# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from led_server.views import stats as stats_views
from led_server.views import tasks as tasks_views


urlpatterns = [
    url(r'^status$', stats_views.StatusView.as_view()),
    url(r'^post_task$', tasks_views.SendTaskView.as_view()),
]
