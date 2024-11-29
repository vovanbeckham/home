from rest_framework import serializers

from expenses.models import Source, Transaction, Transfer



class SourceAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"



class TransactionAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"



class TransferAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = "__all__"