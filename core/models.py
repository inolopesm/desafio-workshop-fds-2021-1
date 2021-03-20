from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return '#{}: {}'.format(self.id, self.name)

class Product(models.Model):
    name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
