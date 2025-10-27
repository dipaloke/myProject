class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #extended_json_view
        userAgent = request.META.get('HTTP_USER_AGENT', 'unknown')
        print(f"{request.method} request for '{request.path}' with User-Agent: {userAgent}")
        # logging ip
        print(f"The ip address is: {request.META.get('REMOTE_ADDR')}, from browser: {request.META.get('HTTP_USER_AGENT')}, host: {request.META.get('HTTP_HOST')} ")
        # method logging
        print(f"This is LoggingMiddleware: {request.method} request for '{request.path}'")
        response = self. get_response(request)
        return response

class IPLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip = request.META.get('REMOTE_ADDR')
        print(f"{request.method} request from IP: {client_ip}")

        response = self. get_response(request)
        return response
class ReqLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        print(f"{request.method} for path: {request.path}")

        response = self. get_response(request)
        return response
