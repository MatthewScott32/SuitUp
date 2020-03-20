import sqlite3
from django.shortcuts import render, redirect, reverse
from suitupapp.models import Store
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def stores_list(request):
    if request.method == 'GET':
                current_user = request.user.id
                all_stores = Store.objects.filter(user_id=current_user).values("id", "name", "location", "brands_available", 
                "notes")
                template = 'stores/list.html'
                context = {
                    'all_stores': all_stores
                }

                return render(request, template, context)
            
    elif request.method == 'POST':
        form_data = request.POST
        new_store = Store(
            name = form_data['name'],
            location = form_data['location'],
            brands_available = form_data['brands_available'],
            notes = form_data['notes'],
            user_id = request.user.id,
        ) 
        new_store.save()
        return redirect(reverse('suitupapp:stores'))