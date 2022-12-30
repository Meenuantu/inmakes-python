from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapp.forms import TodoForm
from todoapp.models import Task

from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView

class deleteview(DeleteView):
    model= Task
    template_name = 'delete.html'
    success_url = reverse_lazy('listview')

class updateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('detailview',kwargs={'pk':self.object.id})
class Detailviewhome(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class listviewhome(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task1'

# Create your views here.
def demo(request):
    v_task = Task.objects.all()
    if request.method=='POST':
        v_name=request.POST.get('name','')
        v_prior=request.POST.get('priority','')
        v_date=request.POST.get('date','')
        v_result=Task(name=v_name,priority=v_prior,date=v_date)
        v_result.save()
    return render(request,'home.html',{'task1':v_task})

#def details(request):

 #   return render(request,'details.html',)

def redirecct(param):
    pass


def delete(request,taskid):
    v_task=Task.objects.get(id=taskid)
    if request.method=='POST':
        v_task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,up_id):
    v_uptask=Task.objects.get(id=up_id)
    v_form=TodoForm(request.POST or None,instance=v_uptask)
    if v_form.is_valid():
        v_form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':v_form,'task':v_uptask})