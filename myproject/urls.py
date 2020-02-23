
from django.contrib import admin
from django.urls import path

from myapi.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductList.as_view(),name="ProductList"),
]
