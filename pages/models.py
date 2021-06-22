from django.db import models

class Contact(models.Model):
    name= models.CharField(max_length=200)
    email = models.EmailField()
    message = models.CharField(max_length=10000)
    def __str__(self):
        return "Kontak"+str(self.name)