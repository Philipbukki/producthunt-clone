from django.urls import path
from products import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.product_create, name='create'),
    path('<int:pk>', views.product_detail, name='detail'),
]
