
from django.urls import path
from . import views;
urlpatterns = [
    path('', views.index),
    path("aboutus/",views.aboutus),
    path("courseid/<int:cid>",views.course_id),
    path("coursename/<str:cname>",views.course_name),
    path("courseslug/<slug:slugtype>",views.course_slug),
    path("viewcourse/",views.view_all_course_info)
]
