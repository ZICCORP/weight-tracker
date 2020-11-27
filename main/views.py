from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from main.forms import BodyWeightForm

class BweightView(View):
    
    def get(self,request,*args,**kwargs):
        context = {'form':BodyWeightForm()}
        return render(request,'home.html',context)

    def post(self,request, *args, **kwargs):
        form = BodyWeightForm(request.POST)
        if form.is_valid():
            bweight = form.save()
            bweight.save()
            return HttpResponseRedirect(reverse_lazy('bwv'))
        return render(request,'home.html',{'form':form})
