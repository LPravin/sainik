from django.db import models


class Service(models.Model):
    esm_no = models.CharField(max_length=10)
    reg_type = models.SmallIntegerField(choices=reg_types)
