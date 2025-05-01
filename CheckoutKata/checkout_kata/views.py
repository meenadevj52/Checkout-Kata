from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

from checkout_kata.models import Product, Discount, Cart
from checkout_kata.serializers import ProductSerializer, DiscountSerializer, CartSerializer

class ProductListAPIView(generics.ListAPIView):
    """List all products."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DiscountView(APIView):
    """Retrieve, create, update, or delete a discount."""

    def get(self, request, pk):
        discount = get_object_or_404(Discount, pk=pk)
        serializer = DiscountSerializer(discount)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DiscountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        discount = get_object_or_404(Discount, pk=pk)
        serializer = DiscountSerializer(discount, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        discount = get_object_or_404(Discount, pk=pk)
        discount.delete()
        return Response({"message": "Discount deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class CartView(APIView):
    """Manage cart operations: view, add, update, or delete items."""

    def get(self, request):
        """Retrieve all cart items."""
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Add or update item in cart."""
        cart, _ = Cart.objects.get_or_create(id=1)
        product_name = request.data.get("product_name")
        quantity = int(request.data.get("quantity", 1))

        if not product_name:
            return Response({"error": "Product name is required"}, status=status.HTTP_400_BAD_REQUEST)

        product = Product.objects.filter(name=product_name).first()
        if not product:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        if cart.items is None:
            cart.items = {}

        cart.items[product_name] = cart.items.get(product_name, 0) + quantity

        cart.calculate_final_price()
        cart.save()
        return Response(CartSerializer(cart).data, status=status.HTTP_200_OK)

    def put(self, request):
        """Update item quantity in cart."""
        cart, _ = Cart.objects.get_or_create(id=1)
        product_name = request.data.get("product_name")
        new_quantity = int(request.data.get("quantity", 1))

        if not product_name:
            return Response({"error": "Product name is required"}, status=status.HTTP_400_BAD_REQUEST)

        if product_name not in cart.items:
            return Response({"error": "Product not in cart"}, status=status.HTTP_404_NOT_FOUND)

        if new_quantity <= 0:
            del cart.items[product_name]
        else:
            cart.items[product_name] = new_quantity

        cart.calculate_final_price()
        cart.save()
        return Response(CartSerializer(cart).data, status=status.HTTP_200_OK)

    def delete(self, request):
        """Delete an item or clear the entire cart."""
        cart, _ = Cart.objects.get_or_create(id=1)
        product_name = request.data.get("product_name")

        if product_name:
            if product_name not in cart.items:
                return Response({"error": "Product not in cart"}, status=status.HTTP_404_NOT_FOUND)
            del cart.items[product_name]
        else:
            cart.items = {}

        cart.calculate_final_price()
        cart.save()
        return Response({"message": "Cart updated successfully"}, status=status.HTTP_200_OK)