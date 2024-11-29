

from django.urls import path

from expenses import views as vs


urlpatterns = [
    path('', vs.index, name='notes-index'),
    path('sources/', vs.Sources.as_view(), name='notes-index'),
    path('transactions/', vs.Transactions.as_view(), name='notes-index'),
    path('transfers/', vs.Transfers.as_view(), name='notes-index'),

]



