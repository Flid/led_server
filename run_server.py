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


# Start Flask server
def run_flask_server():

    from led_server.app import app

    app.run(
        host='0.0.0.0',
        port=10200,
    )


flask_worker = Process(target=run_flask_server)
flask_worker.start()


while True:
    time.sleep(100)
