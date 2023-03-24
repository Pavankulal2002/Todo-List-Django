from django.shortcuts import render,redirect
from .models  import todo

# Create your views here.
def index(request):
    todolist = todo.objects.all()
    if request.method == 'POST':
        todo_list=todo(title=request.POST["titl"])
        todo_list.save()
        return redirect('/')

    return render(request,'index.html',{'todos':todolist})

def delete(request,pk):
    todo_del=todo.objects.get(id=pk)
    todo_del.delete()
    return redirect('/')
