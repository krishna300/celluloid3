

from django.urls import path
# from .views import home
from . import views



# app_name='subscene'
# subscene

urlpatterns = [
    path('', views.home,name='home'),
    # path('home',views.Home.as_view(),name='home'),
    path('detail/<int:post_id>',views.detail,name='detail'),
]
