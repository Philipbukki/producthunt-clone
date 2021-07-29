from django.shortcuts import render
from .forms import ProductCreateForm


def home(request):
    return render(request, 'products/home.html')


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
