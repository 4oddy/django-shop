from django.urls import include, path

from tires.views import TiresView

app_name = 'tires'

urlpatterns = [
    path('tires', TiresView.as_view(), name='tires'),
]
