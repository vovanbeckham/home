from django.db import models
from django.contrib.auth.models import User


class Source(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Название источника (например, "Карта", "Наличные")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Баланс источника

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)  # Название категории (например, "Еда", "Транспорт")

    def __str__(self):
        return self.name


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        (1, 'Поступление'),
        (2, 'Расход'),
        (3, 'Комиссия'),
    ]
    
    source = models.ForeignKey(Source, on_delete=models.CASCADE)  # Источник средств
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)  # Категория расхода
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма транзакции
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE_CHOICES)  # Тип транзакции
    date = models.DateTimeField(auto_now_add=True)  # Дата и время транзакции
    description = models.TextField(blank=True)  # Описание транзакции

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} from {self.source.name}"


class Transfer(models.Model):
    from_source = models.ForeignKey(Source, related_name='transfers_out', on_delete=models.CASCADE)  # Исходный источник
    to_source = models.ForeignKey(Source, related_name='transfers_in', on_delete=models.CASCADE)  # Целевой источник
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма перевода
    date = models.DateTimeField(auto_now_add=True)  # Дата и время перевода
    description = models.TextField(blank=True)  # Описание перевода

    def __str__(self):
        return f"Transfer {self.amount} from {self.from_source.name} to {self.to_source.name}"