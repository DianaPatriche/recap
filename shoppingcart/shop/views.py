from django.shortcuts import render
from .models import Product,Category
# Create your views here.


def product_list(request):
    categorii = Category.objects.all()
    produse=Product.objects.all()
    context={'categorii':categorii,
        'produse':produse}
    return render(request,"list.html",context)


def product_detail(request):
    id=request.GET.get('id')
    produs=Product.objects.get(pk=int(id))
    context={'produs':produs}
    return render(request,"produs.html",context)