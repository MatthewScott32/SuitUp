from django.urls import path
from .views import purchased_item_list

app_name = "suitupapp"

urlpatterns = [
    path('', purchased_item_list, name='home'),
    path('purchaseditems', purchased_item_list, name='purchaseditems'),
]