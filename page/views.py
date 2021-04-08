from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main.html')

def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render(request, '404.html')

def server_error(request, exception):
    """
    500 Page not found
    """
    return render(request, '404.html')