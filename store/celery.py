import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')

app = Celery('store')

# Использование здесь строки означает, что рабочему процессу не нужно сериализовать
# объект конфигурации дочерним процессам.
# - namespace='CELERY' означает все ключи конфигурации, связанные с сельдереем
# должен иметь префикс `CELERY_`.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()