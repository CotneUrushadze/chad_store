from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated

from products.models import Product, Review, FavoriteProduct, Cart, ProductTag, ProductImage
from products.serializers import ProductSerializer, ReviewSerializer, FavoriteProductSerializer, CartSerializer, ProductTagSerializer, ProductImageSerializer
from rest_framework.viewsets import GenericViewSet




class ProductViewSet(GenericViewSet, 
                     ListModelMixin, 
                     CreateModelMixin, 
                     RetrieveModelMixin, 
                     UpdateModelMixin, 
                     DestroyModelMixin):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_class = [IsAuthenticated]


        
class ReviewViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(product_id=self.kwargs['product_pk'])
    
    
    
    
    
class FavoriteProductViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin):
    queryset = FavoriteProduct.objects.all()
    serializer_class = FavoriteProductSerializer
    permission_class = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']
    
    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset
    

    
    
    

class CartViewSet(GenericViewSet, ListModelMixin, CreateModelMixin):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_class = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset





class ProductTagViewSet(GenericViewSet, ListModelMixin):
    queryset = ProductTag.objects.all()
    serializer_class = ProductTagSerializer
    permission_class = [IsAuthenticated]






class ProductImageViewSet(GenericViewSet, ListModelMixin, CreateModelMixin):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_class = [IsAuthenticated]

    
    def get_queryset(self):
        return self.queryset.filter(product_id=self.kwargs['product_pk'])
    
