from rest_framework import viewsets
from rest_framework import response
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
        return response(serialized.data)
    
    def create(self, request): # /api/products (POST method, when a new product needs to be added)
        pass
    
    # below methods are for a single product
    # /api/products/<str:id>
    def retreive(self, request, pk=None):
        pass
    
    def update(self, request, pk=None):
        pass
    
    def destroy(self, request, pk=None):
        pass
    
class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return response({
            'id': user.id
        })