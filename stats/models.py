from django.db import models
from django.contrib.auth.models import User
from spiritbuzz.models import Product
# Create your models here.
class PageView(models.Model):

    class Meta:
        abstract = True

    date = models.DateTimeField(auto_now = True)
    ip_address = models.GenericIPAddressField()
    user = models.ForeignKey(User, null = True)
    tracking_id = models.CharField(max_length = 50, default = '')

class ProductView(PageView):
    product = models.ForeignKey(Product)


