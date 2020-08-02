from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from.models import Product


# Create your views here.


def all_products(request):
    """ A view to return the products page """

    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)

    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'page': page,
    }

    return render(request, 'products/products.html', context)
