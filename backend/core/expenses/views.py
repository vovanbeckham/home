from django.shortcuts import render

from django.http import JsonResponse
from django.shortcuts import render, redirect

from expenses.serializers import SourceAllSerializer, TransactionAllSerializer, TransferAllSerializer
from .models import Transaction, Source, Category, Transfer
from .forms import TransactionForm
from rest_framework.views import APIView


def index(request):
    data = {}
    return JsonResponse({"data": data})






class Sources(APIView):
    def get(self, request):
        source = Source.objects.all()
        serializer = SourceAllSerializer(source, many=True)
        return JsonResponse({'posts': serializer.data})
 
 
    def post(self, request):
        data = request.data.get("device", None)
        
        return JsonResponse({'post': data})



class Transactions(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionAllSerializer(transactions, many=True)
        return JsonResponse({'posts': serializer.data})
 
 
    def post(self, request):
        data = request.data.get("device", None)
        
        return JsonResponse({'post': data})



class Transfers(APIView):
    def get(self, request):
        transactions = Transfer.objects.all()
        serializer = TransferAllSerializer(transactions, many=True)
        return JsonResponse({'posts': serializer.data})
 
 
    def post(self, request):
        data = request.data.get("device", None)
        
        return JsonResponse({'post': data})



def transaction_list(request):
    transactions = Transaction.objects.all()
    return JsonResponse({'transactions': TransactionAllSerializer(transactions, many=True).data})


def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'transactions/add_transaction.html', {'form': form})


def transfer_funds(request):
    if request.method == 'POST':
        source_from_id = request.POST.get('source_from')
        source_to_id = request.POST.get('source_to')
        amount = request.POST.get('amount')

        # Создаем расход из одного источника
        Transaction.objects.create(
            source_id=source_from_id,
            amount=amount,
            transaction_type='expense',
            description='Перевод средств'
        )

        # Создаем поступление в другой источник
        Transaction.objects.create(
            source_id=source_to_id,
            amount=amount,
            transaction_type='income',
            description='Перевод средств'
        )

        return redirect('transaction_list')

    sources = Source.objects.all()
    return render(request, 'transactions/transfer_funds.html', {'sources': sources})