from django.shortcuts import render
from django.http import HttpResponse;
from product.models import Product;
# Create your views here.

def index(request):
    #return HttpResponse("Welcome to Product landing Page")
    return render(request,"product/index.html")

def addPage(request):
    #return HttpResponse("Welcome to Product landing Page")
    return render(request,"product/addProduct.html")

def addProductInDb(request):
    #return HttpResponse("Welcome to Product landing Page")
    pname  = request.GET.get("pname")
    price = request.GET.get("price");
    p1 = Product(p_name=pname,p_price=price);
    p1.save();
    data = {"result":"record stored successfully"}
    return render(request,"product/addProduct.html",data)

def deletePage(request):
    #return HttpResponse("Welcome to Product landing Page")
    return render(request,"product/deleteProduct.html")

def updagePage(request):
    #return HttpResponse("Welcome to Product landing Page")
    return render(request,"product/updateProduct.html")

# def viewPage(request):
#     #return HttpResponse("Welcome to Product landing Page")
#     return render(request,"product/viewProduct.html")


def viewProductFromDb(request):
    products = Product.objects.values();
    print(products);
    params = {"products":products}
    return render(request,"product/viewProduct.html",params)




