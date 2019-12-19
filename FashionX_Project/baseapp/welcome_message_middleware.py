class welcome_middleware:
    # One-time configuration and initialization.
 def __init__(self, get_response):
    self.get_response = get_response
    print('===================')
    print('Welome to FashionX')
    print('====================')
    
 def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
    
    
def simple_middleware(get_response):
    # One-time configuration and initialization.
    
    print('Intilize middleware')

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print('before request')

        response = get_response(request)
        
        print('after request')

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware 
    