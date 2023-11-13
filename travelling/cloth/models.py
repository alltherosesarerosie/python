from django.db import models


class CustomerCL(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'#{self.name}'


class TagCL(models.Model):
    name = models.CharField(max_length=100, verbose_name='Add tag')

    def __str__(self):
        return f'#{self.name}'




class ProductCL(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cost = models.PositiveIntegerField()
    tag = models.ManyToManyField(TagCL, related_name='content_name')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.created_at}'


class OrderCL(models.Model):
    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductCL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer}-{self.created_at}'
