from .models import Todo
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm

# def home(request):
#     return redirect("index")
def register_user(request):
    form = CreateUserForm()

    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Created successfully!")

            user = authenticate(request, username=form.cleaned_data.get("username"), password=form.cleaned_data.get("password1"))
            login(request, user)
            return redirect("index")

    context = {
        "form": form
    }
    return render(request, "todo/signup.html", context)

def login_user(request):
    
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
        else:
            messages.error(request, "Incorrect Username or Password!")

        return redirect("index")

    return render(request, "todo/login.html")

def logout_user(request):
    logout(request)
    return redirect(reverse("index"))


@login_required()
def index(request):
    if request.method == "POST":
        task = request.POST.get("task")

        if not task == "":
            
            todo = Todo.objects.create(user=request.user, text=task)
            todo.save()

            messages.success(request, "Task Added!!")
        
    todos = Todo.objects.filter(user=request.user)

    context = {
        "todos": todos,
        "user": request.user
    }

    return render(request, 'todo/index.html', context)

login_required()
def add_note(request, pk):
    try:
        task = Todo.objects.get(id=pk)
        if request.method == "POST":
            note = request.POST.get("note")
            if note != "":
                task.note_set.create(text=note)
                messages.success(request, "Note Added!")
    except Todo.DoesNotExist:
        pass

    context = {
        "task": task,
        "notes": task.note_set.all()
    }

    return render(request, "todo/add_note.html", context)

def delete_note(request, pk, fk):
    task = Todo.objects.get(id=pk)
    note = task.note_set.get(id=fk)

    note.delete()
    messages.success(request, "Note Deleted")
    return redirect(reverse("note", args=(pk,)))

def delete_task(request, pk):
    try:   
        task = Todo.objects.get(id=pk)
        task.delete()
    except Todo.DoesNotExist:
        pass

    messages.success(request, f"Task Deleted")
    return redirect("index")