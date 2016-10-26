from __future__ import unicode_literals, absolute_import

import time
import logging
from multiprocessing import Process

from led_controller.base import LEDMatrixController


logger = logging.getLogger(__name__)

matrix_controller = LEDMatrixController()


# Start LED Matrix server
def run_led_server_worker():
    global matrix_controller
    logger.info('Starting the LED controller server...')
    matrix_controller.run()


led_worker_process = Process(target=run_led_server_worker)
led_worker_process.start()


# Start Django server
def run_django_server():
    import os
    import sys

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings.dev')

    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:10201', '--noreload'])


django_worker = Process(target=run_django_server)
django_worker.start()


while True:
    time.sleep(100)
