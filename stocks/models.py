from django.db import models

# Create your models here.
class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()
    class Meta:
        app_label = 'stocks'


    def __str__(self):
        return self.symbol
