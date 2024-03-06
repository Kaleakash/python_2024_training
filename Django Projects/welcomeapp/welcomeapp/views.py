from django.http import HttpResponse;
from django.shortcuts import render;
def index(reqeust):
    params = {"name":"Akash","desg":"Trainer"}
    return render(reqeust,"index.html",params);
    #return HttpResponse("Welcome to Simple Django Application!");
    # return HttpResponse('''
    #                     <div>
    #                     <h2>Welcome to Python Django Framework </h2>
    #                     <a href="aboutus">About Us</a>|
    #                     <a href="contactus">Contact Us</a>|
    #                     <a href="feedback">Feedback</a>
    #                     </div>
    #                     ''')

def aboutus(request):
    #return HttpResponse("This is about us page ");
    # return HttpResponse('''
    #                     <div>
    #                     <h4>This is about us page </h4>
    #                     <p>About us description</p><br/>
    #                     <a href="/">back</a>
    #                     </div>
    #                     ''');
    return render(request,"aboutus.html");

def contactus(request):
    #return HttpResponse("This is contactus us page ");
    # return HttpResponse('''
    #                     <div>
    #                     <h4>This is Contact su </h4>
    #                     <p>Contact Us description</p><br/>
    #                     <a href="/">back</a>
    #                     </div>
    #                     ''');
    return render(request,"contactus.html");

def feedback(request):
    #return HttpResponse("This is feedback page ");
    # return HttpResponse('''
    #                     <div>
    #                     <h4>This is Feedback </h4>
    #                     <p>Feedback description</p><br/>
    #                     <a href="/">back</a>
    #                     </div>
    #                     ''');
    return render(request,"feedback.html");



def loginPageOpen(request):
    return render(request,"login.html");

# check multiple emailid and password present in list. 
def checkLoginDetails(request):
    print("I Came Here!");
    #print(request.GET.get("emailid"));
    emailid = request.GET.get("emailid");
    password = request.GET.get("password");
    if emailid=="akash@gmail.com" and password=="123":
        return render(request,"success.html");
    else:
        return render(request,"failure.html")




