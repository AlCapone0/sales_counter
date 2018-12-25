from django.db import models


class RSPORTcouter(models.Model):                       #табоица com-port сообщенией
    PortID = models.IntegerField('номер порта')
    DataCreated = models.DateTimeField('дата время')
    ProxyKey = models.CharField('ключь', max_length=50)

class Companies(models.Model):
    CompanyName = models.CharField('Имя Компании', max_length=200)
    AddressCompany = models.CharField('Адрес Компании', max_length=200)

    class Meta:                        #Описание о модели, Мета данные
        verbose_name = "Компанию"
        verbose_name_plural = "Компании"
        ordering = ["CompanyName"]     #сортировка по имени компании

    def __str__(self):           #возрат имени компании из БД (для админики)
        return self.CompanyName





