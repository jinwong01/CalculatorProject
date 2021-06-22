from django.db import models

# Create your models here.
#from django.db import models


class Calculation(models.Model):
   #result = models.DecimalField(max_digits = 4, decimal_places = 2)
   result = models.CharField(max_length=9)
   num_one= models.DecimalField(max_digits = 4, decimal_places = 2)
   num_two = models.DecimalField(max_digits = 4, decimal_places = 2)
   operator = models.CharField(max_length=1)
   created_at = models.DateTimeField(auto_now_add=True)

