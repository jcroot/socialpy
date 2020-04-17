from django.db import models


# Create your models here.
class SocialProgram(models.Model):
    code = models.CharField("Codigo", max_length=4, db_index=True)
    description = models.CharField("Nombre del programa", max_length=200, blank=True)

    def __str__(self):
        return self.description


class Post(models.Model):
    cic = models.CharField("Cedula CIC", max_length=15, db_index=True)
    fullname = models.CharField("Nombre completo", max_length=200)
    social_code = models.CharField("Programa social", max_length=4, default="")

    def __str__(self):
        return self.fullname

    class Meta:
        unique_together = ['cic', 'social_code']
