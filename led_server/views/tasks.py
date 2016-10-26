from __future__ import unicode_literals, absolute_import

from rest_framework.response import Response
from .base import BaseApiView
from led_controller.tasks import add_task


class SendTaskView(BaseApiView):
    def post(self, request):
        add_task({'name': 'set_pixel', 'coords': [10, 10], 'color': [100, 200, 100]})

        return Response()
