from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Store(models.Model):

    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    brands_available = models.CharField(max_length=50)
    # tailor = models.ForeignKey(Tailor, on_delete=models.DO_NOTHING)
    notes = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


    class Meta:
        verbose_name = ("store")
        verbose_name_plural = ("stores")


    def __str__(self):
        return u'{0}'.format(self.name)


    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
