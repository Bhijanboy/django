from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address=models.CharField(max_length=50,null=True)

    def __str__(self):
        return f"{self.name}-{self.email}"


