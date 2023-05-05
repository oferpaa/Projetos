from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('pagar/<int:pk>', views.Pay.as_view(), name='pay'),
    path('salvar-pedido/', views.SaveOrder.as_view(), name='saveorder'),
    path('lista/', views.List.as_view(), name='list'),
    path('detalhes/<int:pk>', views.Details.as_view(), name='details'),
]
