from django.urls import include, path

from tredin.views import TredinView

app_name = 'tredin'

urlpatterns = [
    path('tredin', TredinView.as_view(), name='tredin'),
]
