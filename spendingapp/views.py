from django.http import  HttpResponseRedirect
from django.shortcuts import render
from .models import Expense
from .forms import ExpenseForm
from datetime import datetime, timedelta


# Create your views here.
def spending(request):
    # Today button
    if request.GET.get('today'):
        value = request.GET.get('today')
        spendings = Expense.objects.filter(data=value).order_by('data')
    # Month button
    elif request.GET.get('month'):
        value = request.GET.get('month')
        spendings = Expense.objects.filter(data__month=value).order_by('data')
    # TODO: implement "Select week" button functionality
    elif request.GET.get('week'):
        pass
    # TODO: implement "Select day" button functionality
    elif request.GET.get('day'):
        pass
    # TODO: implement "Select range" button functionality
    elif request.GET.get('range'):
        pass
    # All Time button
    else:
        spendings = Expense.objects.all()

    now = datetime.now()
    today = {
        'value': now.strftime('%Y-%m-%d'),
        'display': now.day
    }

    month = {
        'value': now.strftime('%Y-%m-%d'),
        'display': now.month
    }

    first_day_of_week = now - timedelta(days=now.weekday())
    last_day_of_week = first_day_of_week + timedelta(days=6)

    week = {
        'first_day_of_week': first_day_of_week.strftime('%Y-%m-%d'),
        'last_day_of_week': last_day_of_week.strftime('%Y-%m-%d'),
        'display': first_day_of_week.strftime('%d %b') + '-' + last_day_of_week.strftime('%d %b')
    }
    total_amount = sum(spending.amount for spending in spendings)
    return render(request, "spending.html",
                  {"spendings": spendings, "total_amount": total_amount, "today": today, "month": month, "week": week})


def adauga(request):
    if request.method == 'GET':
        form = ExpenseForm()
        return render(request, "adauga.html", {"form": form})
    elif request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/")


# TODO: write a view function that will export the data
#  in a csv file. also write a url for it
def export(request):
    pass