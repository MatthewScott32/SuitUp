from django.urls import path, include
# from .views import purchased_item_list
# from .views import purchased_item_details
# from .views import stores_list
# from .views import home
# from .views import register_user
# from .views.auth.logout import logout_user
# # from .views import new_item_form
# from .views import purchased_item_edit_form
# from .views import store_form
# from .views import store_details
# from .views import store_edit_form
# from .views import guide
from .views import *

app_name = "suitupapp"

urlpatterns = [
    path('', home, name='home'),
    path('guide/', guide, name='guide'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register_user, name="register"),
    path('logout/', logout_user, name='logout'),
    path('purchaseditems/', purchased_item_list, name='purchaseditems'),
    path('purchaseditems/form', upload_item, name='upload_item'),
    path('purchaseditems/<int:purchaseditem_id>/',
         purchased_item_details, name='purchaseditem'),
    path('purchaseditems/<int:purchaseditem_id>/form/',
         purchased_item_edit_form, name='purchased_item_edit_form'),
    path('stores/', stores_list, name='stores'),
    path('stores/form', store_form, name='store_form'),
    path('stores/<int:store_id>/', store_details, name='store'),
    path('stores/<int:store_id>/form/', store_edit_form, name='store_edit_form'),
    path('success/', success, name='success')
]
