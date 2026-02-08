from rest_framework import generics
from products.serializers import Productserializer
from products.models import Product

class SearchListView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializer
    
    def get_queryset(self, *args, **kwargs):
        qs= super().get_queryset(*args,**kwargs)
        q=self.request.GET.get('q')
        user=None
        results=Product.objects.none()
        if q is not None:
            if self.request.user.is_authenticated:
                user=self.request.user
            results=qs.search(q,user=user)
        return results
