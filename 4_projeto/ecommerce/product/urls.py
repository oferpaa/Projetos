from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ListProduct.as_view(), name='list'),
    path('<slug>', views.DetailProduct.as_view(), name='detail'),
    path('adicionar-ao-carrinho/', views.AddCart.as_view(), name='addcart'),
    path('remover-do-carrinho/', views.RemoveCart.as_view(), name='removecart'),
    path('carrinho/<int:pk>', views.Cart.as_view(), name='cart'),
    path('finalizar/<int:pk>', views.Finalizar.as_view(), name='finalizar'),
]
