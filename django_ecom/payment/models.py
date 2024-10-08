from django.db import models
from django.contrib.auth.models import User


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_full_name = models.CharField(max_length=250)
    shipping_email = models.CharField(max_length=250)
    shipping_address1 = models.CharField(max_length=250)
    shipping_address2 = models.CharField(max_length=250, null=True, blank=True)
    shipping_country = models.CharField(max_length=250)
    shipping_city = models.CharField(max_length=250)
    shipping_district = models.CharField(max_length=200)
    shipping_postcode = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Shipping Address"

    def __str__(self):
        return f'{self.user} - Shipping Address - {str(self.id)}'
