from django.db import models

# Product to inherit the Model class
class Product(models.Model):
	title		= models.TextField()
	description	= models.TextField()
	price 		= models.TextField()
	summary		= models.TextField(default='this is a default summary')

"""
After changes to models.py , in terminal run
python manage.py makemigrations
python manage.py migrate
"""