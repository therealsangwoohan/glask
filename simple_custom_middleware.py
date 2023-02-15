from glask import Middleware

class SimpleCustomMiddleware(Middleware):
    def process_request(self, request):
        print("Processing request", request.environ["HTTP_HOST"])
    
    def process_response(self, request, response):
        print("Processing response", request.environ["HTTP_HOST"])