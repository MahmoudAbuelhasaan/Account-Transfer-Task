from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Account
from .forms import TransferForm, UploadFileForm
import csv

def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'accounts/account_list.html', {'accounts': accounts})

def account_detail(request, pk):
    account = get_object_or_404(Account, pk=pk)
    return render(request, 'accounts/account_detail.html', {'account': account})

def transfer_funds(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            from_account = form.cleaned_data['from_account']
            to_account = form.cleaned_data['to_account']
            amount = form.cleaned_data['amount']
            if from_account.transfer_funds(to_account, amount):
                return redirect('account_list')
            else:
                return HttpResponse('Insufficient funds', status=400)
    else:
        form = TransferForm()
    return render(request, 'accounts/transfer_funds.html', {'form': form})

def upload_accounts(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            reader = csv.reader(csv_file.read().decode('utf-8').splitlines())
            for row in reader:
                Account.objects.create(name=row[0], balance=row[1])
            return redirect('account_list')
    else:
        form = UploadFileForm()
    return render(request, 'accounts/upload_accounts.html', {'form': form})