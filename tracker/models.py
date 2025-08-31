import uuid
from django.db import models

class Trip(models.Model):
    title = models.CharField(max_length=200)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.CharField(max_length=8, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = uuid.uuid4().hex[:8]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'أكل'),
        ('Transport', 'مواصلات'),
        ('Hotel', 'سكن'),
        ('Shopping', 'تسوق'),
        ('Entertainment', 'ترفيه'),
        ('Other', 'اخرى'),
    ]

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    payer = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.title
