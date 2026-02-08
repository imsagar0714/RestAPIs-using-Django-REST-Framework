from django.db import models
from decimal import Decimal
from django.conf import settings
from django.db.models import Q
# Create your models here.

User = settings.AUTH_USER_MODEL

class ProductQuerySet(models.QuerySet):

    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)

        # 1️⃣ public products search
        qs = self.is_public().filter(lookup)

        # 2️⃣ private products of logged-in user
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)

            # 3️⃣ combine both
            qs = (qs | qs2).distinct()

        return qs


class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)
    

class Product(models.Model):
    user=models.ForeignKey(User,default=1,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=120)
    content=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=15,decimal_places=2,default=99.99)
    public=models.BooleanField(default=True)
    


    @property
    def sales_price(self):
        return self.price * Decimal("0.8")
