from django.db import models

# Create your models here.
class Order(models.Model):

    order_id=models.IntegerField()
    order_by=models.CharField(max_length=50)
    order_location=models.CharField(max_length=200)
    

    def __str__(self):
        return self.order_by
    
class OrderReciepts(models.Model):
    reciept_title=models.CharField(max_length=30)
    reciept_file=models.FileField(upload_to='files/')

    def __str__(self):
        return self.reciept_title
