from django.db import models


class db01(models.Model):
    objects = None
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
       return f"{self.nom} {self.prenom}"