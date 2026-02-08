from rest_framework import generics,permissions
from .models import Product
from .serializers import Productserializer
from api.mixins import StaffEditorPermissionMixin

class ProductDetailAPIview(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializer
    
class ProductListCreateAPIview(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    """ CreateAPIView handles only POST requests, while ListCreateAPIView 
    handles both GET and POST on the same endpoint."""
    queryset=Product.objects.all()
    serializer_class=Productserializer
    
    
    def perform_create(self, serializer):  # runs on POST request only not for GET request
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = title

        serializer.save(content=content)
        
    


class ProductUpdateAPIView(StaffEditorPermissionMixin,generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializer
    lookup_field='pk'
    
    def perform_update(self, serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title

class ProductDeleteAPIView(StaffEditorPermissionMixin,generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializer
    lookup_field='pk'
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)

""" This is the FBV of the ListCreateAPIView , it is manual and for understanding purpose the DRF's
internal work"""
# @api_view(['GET', 'POST'])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method

#     # ---------- GET REQUEST ----------
#     if method == "GET":

#         # Detail view (single product)
#         if pk is not None:
#             obj = get_object_or_404(Product, pk=pk)
#             serializer = ProductSerializer(obj, many=False)
#             return Response(serializer.data)

#         # List view (all products)
#         queryset = Product.objects.all()
#         serializer = ProductSerializer(queryset, many=True)
#         return Response(serializer.data)

#     # ---------- POST REQUEST ----------
#     if method == "POST":
#         serializer = ProductSerializer(data=request.data)

#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None

#             if content is None:
#                 content = title

#             serializer.save(content=content)
#             return Response(serializer.data)

#         return Response({"invalid": "not good data"}, status=400)
