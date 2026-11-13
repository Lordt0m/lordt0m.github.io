from django.urls import path
from orders import views

urlpatterns = [
    path('', views.index),
    path('health/', views.health),
    path('api/bootstrap/', views.bootstrap),
    path('api/role/', views.role),
    path('api/orders/', views.orders),
    path('api/orders/<uuid:order_id>/', views.detail),
    path('api/orders/<uuid:order_id>/status/', views.status),
]
