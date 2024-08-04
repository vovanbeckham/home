from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name



class Content(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()


    def __str__(self) -> str:
        return self.name    