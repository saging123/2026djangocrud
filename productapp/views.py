from django.shortcuts import render
from .models import Product
# Create your views here.


def list(request):
    products = Product.objects.all()
    term = request.GET.get("keyword","").strip()

    if term:
        products = products.filter(name__icontains=term)

    context = {
        "items": products,
        "search": term
    }
    return render(request,"productapp/list.html",context)

def add(request):
    context = {
        "message": ""
    }
    if request.method == "POST":
        prodid  = request.POST.get("prod_id","").strip()
        prodname = request.POST.get("prod_name","").strip()
        prodprice = request.POST.get("prod_price","").strip()

        Product.objects.create(
            productid = prodid,
            name = prodname,
            price = prodprice
        )
        context["message"] = "Successfully Added!"


    return render(request,"productapp/add.html",context)
