from django.db import models


class RSPORTcouter(models.Model):
    PortID = models.IntegerField('номер порта')
    DataCreated = models.DateTimeField('дата время')
    ProxyKey = models.CharField('ключь', max_length=50)