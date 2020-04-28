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


class Nangareko(models.Model):
    cic = models.CharField("Cedula CIC", max_length=15, db_index=True)
    fullname = models.CharField("Nombre completo", max_length=200, blank=True)
    ignored =  models.CharField("Ignorado", max_length=200)
    carrier = models.CharField("Nueva operadora", max_length=100)
    observation = models.CharField("Observacion", max_length=255, blank=True)
    payment_confirmed = models.CharField("Pago confirmado", max_length=200)
    payment_solicited_bycarrier = models.CharField("Pago solicitado operadora", max_length=200)
    sent_sms = models.CharField("Sms Enviado", max_length=200)
    received_sms = models.CharField("Sms Recibido", max_length=200)
    requested = models.CharField("Solicitado a", max_length=100, blank=True)
    phone = models.CharField("Telefono", max_length=20, db_index=True)

    def __str__(self):
        return self.fullname

    class Meta:
        unique_together = ['cic', 'phone']