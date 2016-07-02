# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.response import Response

from .base import BaseApiView


class StatusView(BaseApiView):
    """
    Read the current state of the system.
    """

    def get(self, request):
        return Response({'key': 'value'})
