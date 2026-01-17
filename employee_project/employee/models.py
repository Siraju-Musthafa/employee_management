from django.db import models

# Create your models here.
class employeetable(models.Model):
    STATUS_CHOICE=(('ACTIVE','ACTIVE'),
                   ("INACTIVE",'INACTIVE'))
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    department=models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status=models.CharField(max_length=100,choices=STATUS_CHOICE,default='ACTIVE')

    def __str__(self):
        return  f"{self.name} ({self.status})"