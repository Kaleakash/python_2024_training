from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    #return HttpResponse("Welcome to course page")
    return render(request,"course/index.html");

def aboutus(request):
    return render(request,"aboutus.html")

def course_id(request,cid):
    return HttpResponse(f'your course id is {cid}')

def course_name(request,cname):
    return HttpResponse(f'your course cname is {cname}')

def course_slug(request,slugtype):
    return HttpResponse(f'your course info type {slugtype}')


def view_all_course_info(request):
    data = {
        "name":"View Course Info",
        "course_data":{"cid":100,"cname":"python"},
        "number":[100,200,300,400],
        "course_info":[
            {"cid":1,"cname":"python"},
            {"cid":2,"cname":"java"},
            {"cid":3,"cname":"angular"},
            {"cid":4,"cname":"react"},
        ]
    }
    return render(request,"course/courseInfo.html",data)



