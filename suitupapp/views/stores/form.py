import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from suitupapp.models import Store
from ..connection import Connection

def get_store(store_id):
   
    return Store.objects.get(pk=store_id)


@login_required
def store_form(request):
    if request.method == 'GET':
        # stores = get_stores()
        template = 'stores/form.html'
        # context = {
        #     'all_stores': stores
        # }

        return render(request, template)


@login_required
def store_edit_form(request, store_id):

    if request.method == 'GET':
        store = get_store(store_id)
        # stores = get_stores()

        template = 'stores/form.html'
        context = {
            'store': store,
            # 'all_stores': stores
        }

        return render(request, template, context)