from django.db import models

# Create your models here.

class Product_spec(models.Model):
	id_n = models.IntegerField()
	product_type = models.CharField(max_length = 55)
	product_name = models.CharField(max_length = 55)
	product_code = models.CharField(max_length = 15)
	price = models.IntegerField()
	stock_count = models.IntegerField()
	create_date = models.DateTimeField()
	Update_date = models.DateTimeField()