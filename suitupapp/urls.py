from django.urls import path
from .views import purchased_item_list
from .views import stores_list
from .views.home.home import home

app_name = "suitupapp"

urlpatterns = [
    path('home/', home, name='home'),
    path('purchaseditems/', purchased_item_list, name='purchaseditems'),
    path('stores/', stores_list, name='stores'),
]