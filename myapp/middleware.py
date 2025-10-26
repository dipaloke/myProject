class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"This is LoggingMiddleware: {request.method} request for '{request.path}'")
        response = self. get_response(request)
        return response
