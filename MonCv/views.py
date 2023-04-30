from django.shortcuts import redirect, render
from MonCv.forms import MessageForms

# Create your views here.

def moncv(request):
    form = MessageForms()
    if request.method =='POST':
        form = MessageForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('envoyer')
    context={'form':form}
    return render(request,'cvenligne.html',context)
    


def envoyer_message(request):
    form = MessageForms()
    if request.method=='POST':
        form = MessageForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('envoyer')
    context={'form':form}
    return render(request,'envoyer.html',context)
    