from django.db import models
from django.contrib.auth.models import User


class Alert(models.Model):
    STATUS_CHOICES = (
        ('CREATED', 'Created'),
        ('DELETED', 'Deleted'),
        ('TRIGGERED', 'Triggered'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coin_name = models.CharField(max_length=100, default='Bitcoin')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='CREATED')

    def __str__(self):
        return f"{self.user.username}'s {self.coin_name} Alert for price: {self.price}"
