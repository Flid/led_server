from __future__ import unicode_literals, absolute_import
import logging
from multiprocessing import Value

try:
    import rgbmatrix
except ImportError:
    from . import fake_rgbmatrix as rgbmatrix

from .settings import LED_MATRIX_CONF
from .tasks import pop_task, process_task


_stop_shared = Value('i')


logger = logging.getLogger(__name__)


class LEDMatrixController(object):
    def initialize(self):
        logger.info('Starting LED Matrix server...')

        _stop_shared.value = 0

        self.matrix = rgbmatrix.RGBMatrix(
            LED_MATRIX_CONF['rows'],
            LED_MATRIX_CONF['chain'],
            LED_MATRIX_CONF['parallel'],
        )
        self.matrix.pwmBits = LED_MATRIX_CONF['pwmbits']
        self.matrix.brightness = LED_MATRIX_CONF['brightness']

        if not LED_MATRIX_CONF['luminance_correction']:
            self.matrix.luminanceCorrect = False

    def run(self):
        self.initialize()

        while True:
            task = pop_task()

            if _stop_shared.value == 1:
                # Exitting...
                logger.info('!'*100)
                return

            if not task:
                continue

            logger.info('Received a task %s', task)

            try:
                process_task(self.matrix, task)
            except Exception:
                logger.exception(
                    'Error while processing task %s',
                    task,
                )
