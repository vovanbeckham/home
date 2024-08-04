from django.db import models



class TelegramUser(models.Model):
    telegram_id = models.PositiveIntegerField()
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


    def __str__(self) -> str:
        return str(self.telegram_id)



class BaseService(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.name


class Service(models.Model):
    base = models.ForeignKey(BaseService, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    short = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    timing = models.PositiveSmallIntegerField(null=True, blank=True)


    def __str__(self) -> str:
        return self.name


class ProvidedService(models.Model):
    telegram_user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=False)


    def __str__(self) -> str:
        return self.service.name


