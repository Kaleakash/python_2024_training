
# from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('addPage/', views.addPage),
    path('deletePage/', views.deletePage),
    path('updatePage/', views.updagePage),
    path('viewPage/', views.viewProductFromDb),
    path('addproductindb/',views.addProductInDb)
]
