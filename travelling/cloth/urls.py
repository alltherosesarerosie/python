from django.urls import path
from .views import TagView, AllProductsView, CreateOrderView, OrderListView, CustomerOrderView

urlpatterns = [
    path('tag/<str:tag_name>/', TagView.as_view(), name='tag'),
    path('all/', AllProductsView.as_view(), name='all_products'),
    path('create_order/', CreateOrderView.as_view(), name='create_order'),
    path('order_list/', OrderListView.as_view(), name='order_list'),
    path('customer_order/<int:customer_id>/', CustomerOrderView.as_view(), name='customer_order'),
]