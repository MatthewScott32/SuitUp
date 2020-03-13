import sqlite3
from django.shortcuts import render
from suitupapp.models import Store, PurchasedItem
from ..connection import Connection


def purchasedItemList(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                p.item_bought,
                p.brand,
                p.size,
                p.price,
                p.store_id,
                p.cleaning_methods,
                p.notes,
                p.user_id
            from suitupapp_purchased_item p
            """)

            all_purchased_items = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                purchased_item = PurchasedItem()
                purchased_item.id = row['id']
                purchased_item.item_bought = row['item_bought']
                purchased_item.brand = row['brand']
                purchased_item.size = row['size']
                purchased_item.price = row['price']
                purchased_item.store_id = row['store_id']
                purchased_item.cleaning_methods = row['cleaning_methods']
                purchased_item.notes = row['notes']
                purchased_item.user_id = row['user_id']

                all_purchased_items.append(purchased_item)

        template = 'purchased_item/list.html'
        context = {
            'all_purchased_items': all_purchased_items
        }

        return render(request, template, context)