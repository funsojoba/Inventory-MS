from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=120) 
    category = models.JSONField(blank=True, null=True, default=list)
    labels = models.JSONField(blank=True, null=True, default=list)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.ForeignKey('auth.User', related_name='carts', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='carts', blank=True)

    def __str__(self):
        return self.user.username