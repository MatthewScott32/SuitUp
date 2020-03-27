import sqlite3
from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from suitupapp.models import PurchasedItem
from suitupapp.models import Store
from ..connection import Connection
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.forms import ModelChoiceField


def success(request):
    return HttpResponseRedirect(reverse('suitupapp:purchaseditems'))


class ItemForm(forms.ModelForm):
    class Meta:
        model = PurchasedItem
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['store'].queryset = Store.objects.all()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['store'].queryset = Store.objects.all()


def get_purchaseditem(purchaseditem_id):

    return PurchasedItem.objects.get(pk=purchaseditem_id)


def get_stores():
    # if request.method == 'GET':
    all_stores = Store.objects.all()
    return all_stores


def upload_item(request):
    context = {}
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user_id = request.user.id
            item.save()
            return redirect('suitupapp:success')

    else:
        form = ItemForm()
        context['form'] = form
        context['purchaseditem_id'] = None

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
    context = {}
    purchaseditem = get_purchaseditem(purchaseditem_id)
    if request.method == 'GET':
        form = ItemForm(instance=purchaseditem)
        context['form'] = form
        context['purchaseditem_id'] = purchaseditem_id

        template = 'purchased_items/form.html'

        return render(request, template, context)

    if request.method == 'POST':
        # Pass in the user edited data via the resquest.POST param, and any media files via request.FILES (i.e. docs, imgs, etc.) while ensuring the correct instance is being updated
        form = ItemForm(
            request.POST, request.FILES, instance=purchaseditem)

        # Ensure form validation is complete and the correct data is being passed back to the server
        if form.is_valid():
            # Save the changes to the database
            form.save()
            # Redirect the user to the success HttpResponse method, which sends
            return redirect('suitupapp:success')