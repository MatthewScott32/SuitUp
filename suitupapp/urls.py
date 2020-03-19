from django.urls import path, include
from .views import purchased_item_list
from .views import purchased_item_details
from .views import stores_list
from .views.home.home import home
from .views import register_user
from .views.auth.logout import logout
from .views import new_item_form
from .views import purchased_item_edit_form
from .views import store_form
from .views import store_details
from .views import store_edit_form

app_name = "suitupapp"

urlpatterns = [
    path('home/', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register_user, name="register"),
    path('logout/', logout, name='logout'),
    path('purchaseditems/', purchased_item_list, name='purchaseditems'),
    path('purchaseditems/form', new_item_form, name='purchaseditemform'),
    path('purchaseditems/<int:purchaseditem_id>/', purchased_item_details, name='purchaseditem'),
    path('purchaseditems/<int:purchaseditem_id>/form/', purchased_item_edit_form, name='purchaseditem_edit_form'),
    path('stores/', stores_list, name='stores'),
    path('stores/form', store_form, name='store_form'),
    path('stores/<int:store_id>/', store_details, name='store'),
    path('stores/<int:store_id>/form/', store_edit_form, name='store_edit_form'),
]