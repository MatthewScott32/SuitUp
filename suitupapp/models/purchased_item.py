from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .store import Store
from django.db import IntegrityError

class PurchasedItem(models.Model):
    item_bought = models.CharField(max_length=50, default='')
    brand = models.CharField(max_length=50, default='')
    size = models.CharField(max_length=50, default='')
    price = models.CharField(max_length=50)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    cleaning_methods = models.CharField(max_length=50)
    notes = models.CharField(max_length=50, default='')
    # issues = models.CharField(max_length=50, default='')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

# These receiver hooks allow you to continue to
# work with the `Tailor` class in your Python code.

class Meta:
        verbose_name =("purchased_item")
        verbose_name_plural = ("purchased_items")

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse("_detail", kwargs={"pk": self.pk})
