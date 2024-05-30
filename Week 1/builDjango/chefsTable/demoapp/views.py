from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. This is  the index view of the DemoApp")

def home(request):
    return HttpResponse("<h1> Welcome to the Little Lemon! </h1>")


# Creating request and response for about page
# def about(request):
#     path = request.path
#     scheme = request.scheme
#     method = request.method
#     address = request.META['REMOTE_ADDR']
#     user_agent = request.META['HTTP_USER_AGENT']
#     path_info = request.path_info

#     mag = f"""<br>
#         <br>Path: {path}
#         <br>Scheme: {scheme}
#         <br>Method: {method}
#         <br>Address: {address}
#         <br>User Agent: {user_agent}
#         <br>Path Info: {path_info}
#         <br>
#         <br>{request.headers}

#         #
#         <br> Request Headers: {request.headers}

#         response = HttpResponse()
#         response.headers['Age'] = 20


#     """
    #or 
    return HttpResponse(mag, content_type='text/html',charset='utf-8')


    #or
    # response = HttpResponse("This is the about page. The path is: " + path)
    # return response


    #or 
    # return HttpResponse(path, content_type='text/html',charset='utf-8')


# Creating request and response for drinks page
def drinks(request, drink_name):
    drink = {
        "milk": "Milk is a white liquid produced by the mammary glands of mammals. It is the primary source of nutrition for infant mammals before they are able to digest other types of food.",
        "coffee": "Coffee is a brewed drink prepared from roasted coffee beans, the seeds of berries from certain Coffea species.",
        "tea": "Tea is an aromatic beverage commonly prepared by pouring hot or boiling water over cured or fresh leaves of the Camellia sinensis, an evergreen shrub native to East Asia.",
        "water": "Water is a transparent, tasteless, odorless, and nearly colorless chemical substance, which is the main constituent of Earth's hydrosphere and the fluids of all known living organisms."
    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2>" + choice_of_drink)

# def menu(request):
#     return HttpResponse("This is the menu page")

def booking(request):
    return HttpResponse("This is the booking page")

def about(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."}
    return render(request, 'about.html', about_content)

# def menu(request):
#     menu_content = {'menu': "Our menu is inspired by the Mediterranean diet. We offer a variety of dishes, including pasta, seafood, and vegetarian options. Our chefs use fresh, locally sourced ingredients to create delicious and healthy meals that are perfect for sharing with friends and family. We also have a selection of wines and cocktails to complement your meal. Come and experience the flavors of the Mediterranean at Little Lemon!"}
#     return render(request, 'menu.html', menu_content)


from .models import Menu

def menu(request):
    menu_items = Menu.objects.all()
    items_dict = {"menu": menu_items}
    return render(request,"menu.html", items_dict)

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

def book(request):
    return render(request, 'book.html')