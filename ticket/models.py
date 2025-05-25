from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price  = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    date = models.DateField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(default=False)



    def __str__(self):
        return f"Название: {self.title} , Дата {self.date}, Цена {self.price}"


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    bought_at = models.DateTimeField(auto_now_add=True)

class Meta:
    unique_together = ('user', 'ticket')

