from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.Create.as_view(), name='create'),
    path('atualizar/', views.Update.as_view(), name='update'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
