from django.urls import path
from .views import purchased_item_list
from .views import stores_list

app_name = "suitupapp"

urlpatterns = [
    path('', purchased_item_list, stores_list, name='home'),
    path('purchaseditems', purchased_item_list, name='purchaseditems'),
    path('stores', stores_list, name='stores'),
]