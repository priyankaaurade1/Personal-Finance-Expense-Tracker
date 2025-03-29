from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def dashboard(request):
    if request.user.is_authenticated:
        # Fetch user-specific expenses if logged in
        expenses = Expense.objects.filter(user=request.user)
        total_spent = sum(exp.amount for exp in expenses)
    else:
        # If user is not logged in, show a message instead
        expenses = []
        total_spent = 0

    return render(request, 'expenses/dashboard.html', {
        'expenses': expenses,
        'total_spent': total_spent
    })

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


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('dashboard')  
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  
    
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  
        else:
            messages.error(request, "Invalid username or password")
    
    form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  
