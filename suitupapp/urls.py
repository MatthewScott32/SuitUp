from django.urls import path, include
from .views import purchased_item_list
from .views import stores_list
from .views.home.home import home
from .views.auth.logout import logout
from .views import new_item_form

app_name = "suitupapp"

urlpatterns = [
    path('home/', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout, name='logout'),
    path('purchaseditems/', purchased_item_list, name='purchaseditems'),
    path('purchaseditems/form', new_item_form, name='purchaseditemform'),
    path('stores/', stores_list, name='stores'),
]