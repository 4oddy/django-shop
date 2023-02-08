from django.urls import include, path

from contacts.views import ContactsView

app_name = 'contacts'

urlpatterns = [
    path('contacts', ContactsView.as_view(), name='contacts'),
]
