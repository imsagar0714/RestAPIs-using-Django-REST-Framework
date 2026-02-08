from rest_framework import viewsets,mixins
from .models import Product
from .serializers import Productserializer

class ProductViewsets(viewsets.ModelViewSet):
    """
        GET (LIST,DETAIL)
        POST
        PUT
        PATCH 
        DELETE
    """
    queryset=Product.objects.all()
    serializer_class=Productserializer
    lookup_field='pk'
    
class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    """
    get  -> list     -> Queryset
    get  -> retrieve -> Product Instance Detail View
    """

    queryset = Product.objects.all()
    serializer_class = Productserializer
    lookup_field = 'pk'  