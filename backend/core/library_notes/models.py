from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Theme(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name



class Content(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = CKEditor5Field('Text', config_name='extends')


    def __str__(self) -> str:
        return self.name    