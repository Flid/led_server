# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/', include('led_server.urls', namespace='led_server')),
]

handler400 = 'led_server.views.custom_400_handler'
handler403 = 'led_server.views.custom_403_handler'
handler404 = 'led_server.views.custom_404_handler'
handler500 = 'led_server.views.custom_500_handler'
