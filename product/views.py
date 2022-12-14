from rest_framework import viewsets
from .models import Product

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action

from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status, permissions

from rest_framework.permissions import IsAuthenticated

from django.db import transaction

class ProductViewed(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CartViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        # request_body=serializers.XlsxUploadSerializer,
        methods=["post"],
        operation_description="Import component data sheet",
        operation_summary="Imports and stores a provider's component data sheet",
        tags=["Components"],
        # responses=schema_examples.CREATE_COMPONENT,
    )
    @action(
        detail=False,
        methods=["post"],
        url_path="(?P<pk>[^/.]+)/add",
    )
    def add_to_cart(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        cart = Cart.objects.get(user=request.user)
        if product.quantity == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        with transaction.atomic():
            cart.products.add(product)
            product.quantity -= 1
            product.save()
            cart.save()
        return Response(status=status.HTTP_200_OK)
