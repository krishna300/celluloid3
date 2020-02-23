

from django.urls import path
from django.views.generic import TemplateView
# from .views import *

urlpatterns = [
   
     path('',TemplateView.as_view(template_name="mycss/test2.html"),name="landingpage"),
    #  path('detail/<int:post_id>',detail,name='detail'),

]