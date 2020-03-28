import sqlite3
from django.shortcuts import render, redirect, reverse
from suitupapp.models import Store, PurchasedItem
from ..connection import Connection
from django.contrib.auth.decorators import login_required


@login_required
def purchased_item_list(request):
    if request.method == 'GET':

        current_user = request.user.id
        all_stores = Store.objects.filter(user_id=current_user).values("id", "name", "location", 
            "brands_available", "notes")

        all_items = PurchasedItem.objects.filter(user_id=current_user).values("id", "item_bought", "brand", 
            "size", "price", "cleaning_methods", "notes", "image", "store__name")
        storeId = request.GET.get('store', None)

        if storeId is not None:
            all_items = all_items.filter(store_id=storeId)

        template = 'purchased_items/list.html'
        context = {
                    'all_stores':all_stores,
                    'all_items': all_items,
        }

        return render(request, template, context)
            
    elif request.method == 'POST':
        form_data = request.POST
        new_item = PurchasedItem(
            item_bought = form_data['item_bought'],
            brand = form_data['brand'],
            size = form_data['size'],
            price = form_data['price'],
            store_id = int(form_data['store']),
            cleaning_methods = form_data['cleaning_methods'],
            notes = form_data['notes'],
            user_id = request.user.id,
        ) 
        new_item.save()
        return redirect(reverse('suitupapp:purchaseditems'))