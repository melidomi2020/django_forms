from django.shortcuts import render
from django.http import HttpResponse

from myapp import forms
from .forms import contactForms,snippetForm

# Create your views here.
def contact(request):
    if request.method=='POST':
        form=contactForms(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            print(name,email)

    form=contactForms()
    return render(request,'form.html',{'form':form})

def snippet_detail(request):
     if request.method=='POST':
        form=snippetForm(request.POST)
        if form.is_valid():
            form.save()

     form=snippetForm()
     return render(request,'form.html',{'form':form})
