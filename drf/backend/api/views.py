from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import Productserializer
@api_view(["GET"])
def api_home(request,*args,**kwargs):
    instance=Product.objects.all().order_by("?").first()
    data={}
    if instance:
        data=Productserializer(instance).data
    return Response(data)


@api_view(["POST"])
def api_home(request,*args,**kwargs):
    serializer=Productserializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance=serializer.save()
        print(instance)
        return Response(serializer.data,status=201)

