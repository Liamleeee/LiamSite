from django.urls import path
from . import views as home_views

app_name = 'home'

urlpatterns = [
    path('test/',home_views.test,name='test'),
]