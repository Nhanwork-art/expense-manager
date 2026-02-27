from django.shortcuts import render, redirect, get_object_or_404

from .models import Expense

from .forms import ExpenseForm

from django.db.models import Sum


# Dashboard
def dashboard(request):

    expenses = Expense.objects.all()

    total_income = expenses.filter(
        type='income'
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    total_expense = expenses.filter(
        type='expense'
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    balance = total_income - total_expense

    context = {

        'expenses': expenses,

        'total_income': total_income,

        'total_expense': total_expense,

        'balance': balance,

    }

    return render(
        request,
        'expenses/dashboard.html',
        context
    )


# Add
def add_expense(request):

    form = ExpenseForm(request.POST or None)

    if form.is_valid():

        form.save()

        return redirect('dashboard')

    return render(
        request,
        'expenses/form.html',
        {'form': form}
    )


# Edit
def edit_expense(request, pk):

    expense = get_object_or_404(
        Expense,
        pk=pk
    )

    form = ExpenseForm(
        request.POST or None,
        instance=expense
    )

    if form.is_valid():

        form.save()

        return redirect('dashboard')

    return render(
        request,
        'expenses/form.html',
        {'form': form}
    )


# Delete
def delete_expense(request, pk):

    expense = get_object_or_404(
        Expense,
        pk=pk
    )

    expense.delete()

    return redirect('dashboard')