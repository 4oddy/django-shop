"""сохранить конфигурацию URL-адреса

Список `urlpatterns` направляет URL-адреса в представления. Для получения дополнительной информации см.:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Примеры:
Представления функций
    1. Добавьте импорт: из представлений импорта my_app
    2. Добавьте URL-адрес в urlpatterns: path('', views.home, name='home')
Представления на основе классов
    1. Добавьте импорт: from other_app.views import Home
    2. Добавьте URL-адрес в шаблоны URL-адресов: path('', Home.as_view(), name='home')
Включение другой конфигурации URL
    1. Импортируйте функцию include(): из django.urls import include, path
    2. Добавьте URL-адрес в urlpatterns: path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


from products.views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('accounts/', include('allauth.urls')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('contacts/', include('contacts.urls', namespace='contacts')),
    path('delivery/', include('delivery.urls', namespace='delivery')),
    path('disk/', include('disk.urls', namespace='disk')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('tires/', include('tires.urls', namespace='tires')),
    path('tredin/', include('tredin.urls', namespace='tredin')),


]


if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
