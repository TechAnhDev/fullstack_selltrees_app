from django.db import models





class Products(models.Model):
    class Meta:
        db_table = 'products'

    name = models.CharField(max_length=50)  
    image = models.URLField()  
    price = models.FloatField()
    rating = models.IntegerField()
    oldprice = models.FloatField()