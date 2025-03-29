from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User  
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def dashboard(request):
    expenses = Expense.objects.filter(user=request.user) 

    total_spent = sum(expense.amount for expense in expenses) 
    return render(request,'expenses/dashboard.html',{"expenses":expenses,"total_spent":total_spent})

@login_required
def add_expense(request):
    categories = ['home', 'food', 'shopping', 'entertainment', 'travelling', 'others']
    if request.method == 'POST':
        title = request.POST.get("title")
        amount = request.POST.get("amount")
        category = request.POST.get("category")
        note = request.POST.get("note")

        if request.user.is_authenticated:
            Expense.objects.create(
                user=request.user,
                title=title,
                amount=amount,
                category=category,
                note=note
            )
            messages.success(request, "Expenses added successfully !")
            return redirect("dashboard")
        else:
            messages.error(request,"You must be logged in to add an expense!")
    return render(request,'expenses/add_expense.html',{"categories":categories})