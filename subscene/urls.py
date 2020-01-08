

from django.urls import path
# from .views import home
from . import views



# app_name='subscene'	
# subscene
# 
urlpatterns = [
    
	# path('', views.home,name='home'),
    path('', views.PostListView.as_view(), name='home'),
    path('myposts/', views.MyPosts.as_view(), name='myposts'),
    path('post/new/', views.PostCreateView.as_view(), name='create'),
    # path('myposts/', views.MyPosts.as_view(), name='myposts'),
    path('detail/<int:post_id>',views.detail,name='detail'),
    # path('post/new/', views.create, name='create'),
    # path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
]
