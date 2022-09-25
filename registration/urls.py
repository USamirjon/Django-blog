from django.urls import path
from . import views


app_name = 'registration'
urlpatterns = [
    path('', views.reg, name='reg'),
    path('create_account', views.create_account, name='create_account'),
    path('authorization', views.authorization, name='authorization')
]

