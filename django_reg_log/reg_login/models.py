from django.db import models
from django.core.exceptions import ValidationError

def mail_validator(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError("Add propre values")

# Create your models here.
class register(models.Model):
    id = models.AutoField(primary_key=True)
    Firstname = models.CharField("FName", max_length=20)
    Lastname = models.CharField("LName",max_length=20)
    email = models.EmailField("Email",max_length=20)
    password = models.CharField("password",max_length=25,validators=[mail_validator])

    def __str__(self) :
        return self.Firstname
