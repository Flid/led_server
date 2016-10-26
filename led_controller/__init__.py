from __future__ import unicode_literals, absolute_import

import logging
import logging.config
import sys

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,

    'formatters': {
        'standard': {
            'format': ' %(asctime)s %(message)s',
        },
    },

    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'backupCount': 7,
            'filename': '/var/log/led_server.log',
            'formatter': 'standard',
        },

        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },

    'loggers': {
        'led_controller': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': True,
        },
    },
})
