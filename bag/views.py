from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def view_bag(request):
    """ A view to return the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of an item to the bag """

    quantity = int(request.POST.get('quantity', 0))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    size = request.POST.get('size', None)
    material = request.POST.get('material', None)
    colour = request.POST.get('colour', None)
    # Check if products item_id is in the bag bag_item_id
    # Check if products item_id is in the bag
    if item_id in bag:
        # Check if they have equal values, if they do just update quantity
        if size in bag[item_id]['item_data']['size'] and material\
         in bag[item_id]['item_data']['material']\
         and colour in bag[item_id]['item_data']['colour']:
            print('item exists....updating quantity')
            bag[item_id]['item_data']['quantity'] += quantity

    else:
        print('creating new item')
        bag[item_id] = {}
        bag[item_id]['item_data'] = {}
        bag[item_id]['item_data']['size'] = size
        bag[item_id]['item_data']['material'] = material
        bag[item_id]['item_data']['colour'] = colour
        bag[item_id]['item_data']['quantity'] = quantity
    print(bag)

    request.session['bag'] = bag

    return redirect(redirect_url)
