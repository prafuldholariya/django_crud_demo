# items/middleware.py

import logging

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        method = request.method
        path = request.get_full_path()
        logger.info(f"Request: {method} {path}")
        response = self.get_response(request)
        return response
