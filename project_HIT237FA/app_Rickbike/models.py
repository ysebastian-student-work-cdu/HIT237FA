from django.db import models

# Create your models here.

class Widget(models.Model):

    part_number = models.CharField(max_length=12)
    description = models.CharField(max_length=400)
    price = models.DecimalField(max_digits =7, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str('%s: %s ~~~ $%.2f'
        % (self.part_number, self.description[0:35], self.price))
