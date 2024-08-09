from django.db import models


class Query(models.Model):
    cad_num = models.CharField(max_length=100, verbose_name='Кадастровый номер')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Ширина')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Долгота')
    result = models.BooleanField(null=True, blank=True, verbose_name='Ответ')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')