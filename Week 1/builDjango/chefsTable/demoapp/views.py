from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. This is  the index view of the DemoApp")

def home(request):
    return HttpResponse("<h1> Welcome to the Little Lemon! </h1>")


# Creating request and response for about page
def about(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    mag = f"""<br>
        <br>Path: {path}
        <br>Scheme: {scheme}
        <br>Method: {method}
        <br>Address: {address}
        <br>User Agent: {user_agent}
        <br>Path Info: {path_info}
        <br>
        <br>{request.headers}

        #
        <br> Request Headers: {request.headers}

        response = HttpResponse()
        response.headers['Age'] = 20


    """
    #or 
    return HttpResponse(mag, content_type='text/html',charset='utf-8')


    #or
    # response = HttpResponse("This is the about page. The path is: " + path)
    # return response


    #or 
    # return HttpResponse(path, content_type='text/html',charset='utf-8')