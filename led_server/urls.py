# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from led_server.views import stats as stats_views

urlpatterns = [
    url(r'^status$', stats_views.StatusView.as_view()),
]
