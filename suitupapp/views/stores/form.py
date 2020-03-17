import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from suitupapp.models import Store
from ..connection import Connection


@login_required
def store_form(request):
    if request.method == 'GET':
        # stores = get_stores()
        template = 'stores/form.html'
        # context = {
        #     'all_stores': stores
        # }

        return render(request, template)