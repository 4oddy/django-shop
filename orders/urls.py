from django.urls import include, path

from orders.views import OrderCreateView, OrderDetailView, OrderListView

app_name = 'orders'

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order'),
    path('', OrderListView.as_view(), name='orders_list'),
]
