from django.shortcuts import render
from .models import Product,Category
# Create your views here.


def product_list(request,categoryid):
    id=categoryid
    categorii = Category.objects.all()
    produse=Product.objects.get(fk=int(categoryid))
    context={'categorii':categorii,
        'produse':produse}
    return render(request,"list.html",context)


def product_detail(request, productid):
    id = productid
    produs=Product.objects.get(pk=int(id))
    context={'produs':produs}
    return render(request,"produs.html",context)


def category_products(request,categoryid = 1):
    categorii=Category.objects.all()
    produse=Product.objects.filter(category=categoryid)
    context={'categorii':categorii,
             'produse':produse}
    return render(request,"category_product_list.html",context)
