import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from suitupapp.models import PurchasedItem
from suitupapp.models import Store
from ..connection import Connection

def get_stores():
    # if request.method == 'GET':
    all_stores = Store.objects.all()
    return all_stores

@login_required
def new_item_form(request):
    if request.method == 'GET':
        stores = get_stores()
        template = 'purchased_items/form.html'
        context = {
            'all_stores': stores
        }

        return render(request, template, context)