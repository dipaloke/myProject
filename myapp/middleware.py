class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # logging ip
        print(f"The ip address is: {request.META.get('REMOTE_ADDR')}, from browser: {request.META.get('HTTP_USER_AGENT')}, host: {request.META.get('HTTP_HOST')} ")
        # method logging
        print(f"This is LoggingMiddleware: {request.method} request for '{request.path}'")
        response = self. get_response(request)
        return response
