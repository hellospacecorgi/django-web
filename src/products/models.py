from django.db import models

# Product to inherit the Model class
class Product(models.Model):

# use different model field types to customised usage
	title		= models.CharField(max_length=100)
	description	= models.TextField(blank=True, null=True)
	price 		= models.DecimalField(max_digits=10,decimal_places=2)
	summary		= models.TextField(default='this is a default summary')

"""
After changes to models.py , in terminal run
python manage.py makemigrations
python manage.py migrate
"""