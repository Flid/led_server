from __future__ import unicode_literals

import logging

logger = logging.getLogger(__name__)


class RGBMatrix(object):
    _allowed_methods = {
        'SetPixel',
    }

    def __init__(self, *args, **kwargs):
        logger.warning('USING FAKE RGBMATRIX INSTANCE!!!')

    def _method_caller(self, method_name):
        def _runner(*args, **kwargs):
            logger.info(
                'Called method %s: args=%s kwargs=%s',
                method_name,
                args,
                kwargs,
            )

        return _runner

    def __getattr__(self, item):
        if item in self._allowed_methods:
            return self._method_caller(item)

        return super(RGBMatrix, self).__getattribute__(item)
