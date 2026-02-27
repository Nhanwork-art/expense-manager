from django.db import models


class Expense(models.Model):

    TYPE_CHOICES = (
        ('income', 'Thu nhập'),
        ('expense', 'Chi tiêu'),
    )

    title = models.CharField(max_length=255)

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES
    )

    category = models.CharField(max_length=100)

    date = models.DateField()

    note = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title