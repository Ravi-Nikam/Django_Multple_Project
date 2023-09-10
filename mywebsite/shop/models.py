from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70,default='')
    email = models.EmailField('Enter email',max_length=50)
    phone  = models.CharField("Phone number", max_length=12,default='')
    desc = models.CharField('description',max_length=120,default='',)

    def __str__(self):
        return self.id