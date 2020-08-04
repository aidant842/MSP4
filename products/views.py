from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from.models import Product, Category


# Create your views here.


def all_products(request):
    """ A view to return the products page """

    products = Product.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page')

    selected_category = None
    filtered_products = None

    if request.GET:
        if 'category' in request.GET:
            selected_category = request.GET['category']
            filtered_products = products.filter(category__name=selected_category)
            print(filtered_products)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)

    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'filtered_products': filtered_products,
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'page': page,
    }

    return render(request, 'products/products.html', context)
