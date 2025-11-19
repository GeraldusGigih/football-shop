from django.urls import path
from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register
from main.views import login_user, logout_user, edit_product, delete_product, add_product_entry_ajax, edit_product_ajax, delete_product_ajax
from main.views import proxy_image, create_product_flutter, get_all_products_json, get_my_products_json

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<uuid:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<uuid:id>/', edit_product, name='edit_product'),
    path('delete-product/<uuid:id>/', delete_product, name='delete_product'),
    path('add-product-entry-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('edit-product-ajax/<uuid:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('delete-product-ajax/<uuid:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('get-all-products/', get_all_products_json, name='get_all_products'),
    path('get-my-products/', get_my_products_json, name='get_my_products')
]