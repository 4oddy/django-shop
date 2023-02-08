from django.urls import include, path

from disk.views import DiskView

app_name = 'disk'

urlpatterns = [
    path('disk', DiskView.as_view(), name='disk'),
]
