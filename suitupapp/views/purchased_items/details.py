import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from suitupapp.models import PurchasedItem, Store
from ..connection import Connection


def get_item(purchaseditem_id):
   
    return PurchasedItem.objects.get(pk=purchaseditem_id)


@login_required
def purchased_item_details(request, purchaseditem_id):
    if request.method == 'GET':
        purchaseditem = get_item(purchaseditem_id)
        template_name = 'purchased_items/details.html'
        return render(request, template_name, {'purchaseditem': purchaseditem})

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
          
            purchased_item_to_update = PurchasedItem.objects.get(pk=purchaseditem_id)

            purchased_item_to_update.item_bought = form_data['item_bought']
            purchased_item_to_update.brand = form_data['brand']
            purchased_item_to_update.size = form_data['size']
            purchased_item_to_update.price = form_data['price']
            purchased_item_to_update.cleaning_methods = form_data['cleaning_methods']
            purchased_item_to_update.notes = form_data['notes']
            purchased_item_to_update.store_id = form_data['store_id']

            purchased_item_to_update.save()

            return redirect(reverse('suitupapp:purchaseditems'))

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
                
            purchaseditem = PurchasedItem.objects.get(pk=purchaseditem_id)
            purchaseditem.delete()

            return redirect(reverse('suitupapp:purchaseditems'))