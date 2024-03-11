from django.http import HttpResponse

def index(request):
    return HttpResponse("This is main view page of my-site")

