from django.db import models


# Create your models here.
class Post(models.Model):
    cic = models.CharField("Cedula CIC", max_length=15, db_index=True)
    fullname = models.CharField("Nombre completo", max_length=200)
    social_code = models.CharField("Programa social", max_length=4, default="")

    def __str__(self):
        return self.fullname
