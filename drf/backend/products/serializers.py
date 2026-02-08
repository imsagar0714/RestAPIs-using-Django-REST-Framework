from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from api.serializers import UserPublicSerializer

class Productserializer(serializers.ModelSerializer):
    user=UserPublicSerializer()
    sales_price = serializers.ReadOnlyField()
    edit_url=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Product
        fields=[
            'user',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sales_price',
        ]
        
    def get_edit_url(self, obj):
        request = self.context.get('request')  # self.request
        if request is None:
            return None
        return reverse(
            "product-edit",
            kwargs={"pk": obj.pk},
            request=request
        )
