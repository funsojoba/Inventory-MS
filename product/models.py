from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=120) 
    category = models.JSONField(blank=True, null=True, default=list)
    labels = models.JSONField(blank=True, null=True, default=list)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=10000)

    def get_absolute_url(self):
        return f"/products/{self.id}/"

    def get_edit_url(self):
        return f"/products/{self.id}/edit/"

    def get_delete_url(self):
        return f"/products/{self.id}/delete/"