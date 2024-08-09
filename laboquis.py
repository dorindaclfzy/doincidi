# Instead of calling a view within another view
def add_stuff(bar):
    item = Item.objects.create(foo=bar)
    return item

def specific_add_item_view(request):
    item = add_stuff(bar)
    # ...

def big_view(request):
    item = add_stuff(bar)
    # ...

# Refactor the code to extract common functionality
def add_stuff(bar):
    item = Item.objects.create(foo=bar)
    return item

def specific_add_item_view(request):
    item = add_stuff(bar)
    # ...

def big_view(request):
    item = add_stuff(bar)
    # ...
