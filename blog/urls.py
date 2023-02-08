from django.urls import include, path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('<int:pk>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
]
