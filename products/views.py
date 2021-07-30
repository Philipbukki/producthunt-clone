from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProductCreateForm
from .models import Product


def home(request):

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/home.html', context)


def product_create(request):

    form = ProductCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()

    else:
        form = ProductCreateForm()

    context = {
        'form': form
    }

    return render(request, 'products/product_create.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)

    context = {
        'product': product
    }

    return render(request, 'products/detail.html', context)
