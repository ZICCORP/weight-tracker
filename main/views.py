from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from main.forms import BodyWeightForm
from main.models import BodyWeight



class BweightView(View):

    def datalist(self,model):
        """
        Accepts a model as arguement and returns a list of dictionary with the date formated
        """
        calender = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
        data = model.objects.all().values('weight','date')
        d= []
        for i in data:
            for j in i:
                if j=='date':
                    d_obj = i[j]
                    d_day = d_obj.day
                    d_month = calender[d_obj.month]
                    d_year = d_obj.year
                    i['date'] =str(d_month)+' '+str(d_day)+', '+str(d_year)[:2]
            d.append(i)

        d.append({'weight':150,'date':'40'})
        d.append({'weight':98,'date':'20'})
        d.append({'weight':50,'date':'10'})
        return d

    def get(self,request,*args,**kwargs):
        context = {'form':BodyWeightForm(),'data':self.datalist(BodyWeight)}
        return render(request,'main/home.html',context)

    def post(self,request, *args, **kwargs):
        form = BodyWeightForm(request.POST)
        if form.is_valid():
            bweight = form.save()
            bweight.save()
            return HttpResponseRedirect(reverse_lazy('bwv'))
        return render(request,'main/home.html',{'form':form,'data':self.datalist(BodyWeight)})
