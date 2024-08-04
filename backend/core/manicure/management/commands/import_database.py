import json
from django.core.management.base import BaseCommand

from manicure.models import ProvidedService


class Command(BaseCommand):
    help = 'Отображает текущее время'
    def handle(self, *args, **kwargs):
        with open('data.json', 'r') as f:
            data = json.load(f)
        for d in data:
            pr = ProvidedService(telegram_user_id=d["user"])
            pr.service_id = d["service"]
            pr.date = d["date"]
            pr.price = d["price"]
            pr.save()