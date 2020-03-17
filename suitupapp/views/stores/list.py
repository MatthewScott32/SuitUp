import sqlite3
from django.shortcuts import render, redirect, reverse
from suitupapp.models import Store, PurchasedItem
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def stores_list(request):
    if request.method == 'GET':
        # with sqlite3.connect(Connection.db_path) as conn:
        #     conn.row_factory = sqlite3.Row
        #     db_cursor = conn.cursor()

            # db_cursor.execute("""
            # select
            #     p.item_bought,
            #     p.brand,
            #     p.size,
            #     p.price,
            #     p.store_id,
            #     p.cleaning_methods,
            #     p.notes,
            #     p.user_id
            # from suitupapp_purchased_item p
            # """)

            # all_purchased_items = []
            # # dataset = db_cursor.fetchall()
            # dataset = PurchasedItem

            # for row in dataset:
            #     purchased_item = PurchasedItem()
            #     purchased_item.id = row['id']
            #     purchased_item.item_bought = row['item_bought']
            #     purchased_item.brand = row['brand']
            #     purchased_item.size = row['size']
            #     purchased_item.price = row['price']
            #     purchased_item.store_id = row['store_id']
            #     purchased_item.cleaning_methods = row['cleaning_methods']
            #     purchased_item.notes = row['notes']
            #     purchased_item.user_id = row['user_id']

                # all_purchased_items.append(purchased_item)
                all_stores = Store.objects.values("name", "location", "brands_available", "notes")

                # purchased_item = request.GET.get('purchased_item', None)
                # for item in all_items:
                #     print(item.brand)

                # if purchased_item is not None:
                #     all_items = all_items.filter(purchased_item__contains=purchased_item)

                template = 'stores/list.html'
                context = {
                    'all_stores': all_stores
                }

                return render(request, template, context)
            
    elif request.method == 'POST':
        form_data = request.POST

        new_item = Store(
            name = form_data['name'],
            location = form_data['location'],
            brands_available = form_data['brands_available'],
            notes = form_data['notes'],
            user_id = request.user.id,
        ) 
        new_item.save()
        return redirect(reverse('suitupapp:stores'))