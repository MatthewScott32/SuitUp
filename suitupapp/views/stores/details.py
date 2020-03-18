import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from suitupapp.models import Store
from ..connection import Connection


def get_store(store_id):
   
    return Store.objects.get(pk=store_id)


@login_required
def store_details(request, store_id):
    if request.method == 'GET':
        store = get_store(store_id)
        template_name = 'stores/details.html'
        return render(request, template_name, {'store': store})

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
          
            store_to_update = Store.objects.get(pk=store_id)

            store_to_update.name = form_data['name']
            store_to_update.location = form_data['location']
            store_to_update.brands_available = form_data['brands_available']
            store_to_update.notes = form_data['notes']

            store_to_update.save()

            return redirect(reverse('suitupapp:stores'))

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
                
            store = Store.objects.get(pk=store_id)
            store.delete()

            return redirect(reverse('suitupapp:stores'))