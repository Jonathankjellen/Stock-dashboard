from django.db import models
import datetime

# Create your models here.
class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    date = models.DateField(default=datetime.date.today)
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    close_price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.BigIntegerField()

    def __str__(self):
        return f"{self.symbol} - {self.date}"

    class Meta:
        app_label = 'stocks'
        unique_together = ('symbol', 'date')
        indexes = [
            models.Index(fields=['symbol', 'date']),
        ]
