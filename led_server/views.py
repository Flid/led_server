from __future__ import unicode_literals, absolute_import
from flask import Response
from led_server.app import app

from led_controller.tasks import add_task


@app.route('/send_task', methods=['POST'])
def send_task():
    add_task({'name': 'set_pixel', 'coords': [10, 10], 'color': [100, 200, 100]})

    return Response()
