from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='categories/images/')
    parent_category = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='subcategory',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image_a = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image_b = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image_c = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name
