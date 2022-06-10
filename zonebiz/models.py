from django.db import models


class Service(models.Model):

    name = models.CharField(
        max_length=150,
        blank=True,
        default='No name'
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(
        default=True
    )

