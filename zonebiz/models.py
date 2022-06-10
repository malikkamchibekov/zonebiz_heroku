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
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return f'{self.name}'


class Blog(models.Model):

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image')
    content = models.TextField()
    category = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=False)
    author = models.CharField(max_length=100)
    authors_photo = models.ImageField(upload_to='image')

    def __str__(self):
        return str(self.title)

