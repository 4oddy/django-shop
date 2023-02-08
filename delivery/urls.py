from django.urls import include, path

from delivery.views import DeliveryView

app_name = 'delivery'

urlpatterns = [
    path('delivery', DeliveryView.as_view(), name='delivery'),
]
