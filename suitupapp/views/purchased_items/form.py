import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from suitupapp.models import PurchasedItem
from suitupapp.models import Store
from ..connection import Connection
from django.forms import ModelForm
from django.http import HttpResponseRedirect


def success(request): 
    return HttpResponseRedirect(reverse('suitupapp:purchaseditems'))

class CreateItemForm(ModelForm):
    class Meta:
        model = PurchasedItem
        exclude = ["user"]

def get_purchaseditem(purchaseditem_id):
   
    return PurchasedItem.objects.get(pk=purchaseditem_id)

def get_stores():
    # if request.method == 'GET':
    all_stores = Store.objects.all()
    return all_stores

def upload_item(request):
    context = {}
    if request.method == 'POST':
        form = CreateItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user_id = request.user.id
            item.save()
            return redirect('suitupapp:success')

    else:
        form = CreateItemForm()
        context['form']=form
        return render(request, 'purchased_items/form.html', context)

# @login_required
# def new_item_form(request):
#     if request.method == 'GET':
#         stores = get_stores()
#         template = 'purchased_items/form.html'
#         context = {
#             'all_stores': stores
#         }

#         return render(request, template, context)

@login_required
def purchased_item_edit_form(request, purchaseditem_id):

    if request.method == 'GET':
        purchaseditem = get_purchaseditem(purchaseditem_id)
        stores = get_stores()

        template = 'purchased_items/form.html'
        context = {
            'purchaseditem': purchaseditem,
            'all_stores': stores
        }

        return render(request, template, context)

    elif request.method == 'POST':
        print("edit post")
    