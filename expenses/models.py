from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    category_choices=[
        ('home','home'),
        ('food','food'),
        ('shopping','shopping'),
        ('entertainment','entertainment'),
        ('travelling','travelling'),
        ('others','others')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.CharField(choices=category_choices,max_length=20)
    note = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.title} - ${self.amount}"