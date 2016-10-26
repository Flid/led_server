# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import exceptions as rest_exceptions
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_503_SERVICE_UNAVAILABLE,
)


class BaseApiError(rest_exceptions.APIException):
    """
    Basic exception class, never raise it directly!
    """
    code = None
    default_detail = None

    def __init__(self, detail=None):
        self.detail = detail


class InternalApiError(BaseApiError):
    status_code = HTTP_500_INTERNAL_SERVER_ERROR
    code = 'internal'
