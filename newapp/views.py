from django.shortcuts import render

# Create your views here.

from newapp.forms import schl_form

def school (request):
    form=schl_form()
    if request.method=="POST":
        form=schl_form(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'home.html',context)
