

def bag_contents(request):

    bag_items = []
    total = 0
    delivery = total * .10

    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
