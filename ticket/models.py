from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price  = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    date = models.DateField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(default=False)



    def __str__(self):
        return f"Название: {self.title} , Дата {self.date}, Цена {self.price}"