from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return self.name


class Address(models.Model):
    address = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    link_map = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.address
