from django.shortcuts import render
from products.models import Product


def view_bag(request):
    """ A view to return the bag contents page """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'bag/bag.html', context)
