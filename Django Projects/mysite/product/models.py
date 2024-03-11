from django.db import models

class Product(models.Model):
    p_id = models.AutoField
    p_name = models.CharField(max_length=50)
    p_price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self) :
        return self.p_name