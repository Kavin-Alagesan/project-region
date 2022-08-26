from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Regionmodel(models.Model):
    CHOICE_COUNTRY=[
        ("0","Unknown"),
        ("1","India"),
        ("2","USA"),
        ("3","Japan"),
        ("4","China"),
        ("5","Cambodia"),
        ("6","Rwanda"),
        ("7","Thailand"),
    ]
    code=models.PositiveBigIntegerField(validators=[MaxValueValidator(9999999999)])
    name=models.CharField(max_length=30)
    country=models.CharField(max_length=30,choices=CHOICE_COUNTRY)
    image=models.ImageField(upload_to='region_image',null=True,blank=True)

    def __str__(self):
        return f"{self.name} : {self.country}"
        
