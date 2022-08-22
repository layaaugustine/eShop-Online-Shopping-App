from django.shortcuts import redirect

def auth_middleware(get_response):

    def middleware(request):
        # print('middleware')

        returnUrl = request.META['PATH_INFO']

        # print(request.META['PATH_INFO'])

        print("customer",request.session.get('customer'))
         
        if not request.session.get('customer'):
            return redirect(f'login?return_url={returnUrl}')
        
        else:
            response = get_response(request)
            return response

    return middleware