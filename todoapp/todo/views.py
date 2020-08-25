from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import TodoModel
from .forms import TodoForm

def index(request):
    todos = TodoModel.objects.all()
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            print('valid')
            return redirect('/')

    context = {'form':form, 'todos':todos}
    return render(request, 'todo/index.html', context)

def update(request,pk):
    sel_todo = TodoModel.objects.get(id=pk)
    form1 = TodoForm(instance=sel_todo)

    if request.method == "POST":
        form1 = TodoForm(request.POST,instance=sel_todo )
        if form1.is_valid():
                form1.save()
                return redirect('/')

    return render(request,'todo/update.html',{'form':form1})

def delete(request,pk):
    del_todo = TodoModel.objects.get(id=pk)
    if request.method == "POST":
        del_todo.delete()
        return redirect('/')
    return render(request, 'todo/delet.html')
