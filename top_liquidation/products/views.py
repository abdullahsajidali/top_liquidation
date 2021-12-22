from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .models import User
from .serializers import ProductSerializer
import random

class ProductViewSet(viewsets.ViewSet):
    def list(self, request): # /api/products (GET method used when a user wants to view all products)
        
        # first we need to find all the products
        products = Product.objects.all()
        
        #now we need to serialize the products object
        serialized = ProductSerializer(products, many=True) # meaning this will be an array
        
        #now just return the response to the caller
        return Response(serialized.data)
    
    def create(self, request): # /api/products (POST method, when a new product needs to be added)
        
        serialized = ProductSerializer(data = request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    
    # below methods are for a single product
    # /api/products/<str:id>
    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })