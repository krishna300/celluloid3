from django.shortcuts import render

from rest_framework.generics import ListAPIView,ListCreateAPIView
from .models import Product
from .serializers import ProductSerializer
# Create your views here.


class ProductList(ListCreateAPIView):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    # ordering= ['-id']
