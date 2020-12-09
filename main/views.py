from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from main.forms import BodyWeightForm
from main.models import BodyWeight
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from users.forms import CustomUserCreationForm
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser
from datetime import datetime
from main.forms import AuthenticationForm


class BweightView(LoginRequiredMixin,View):
    

    def datalist(self,model):
        """
        Accepts a model as arguement and returns a list of dictionary with the date formated
        """
        calender = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
        data = model.objects.filter(owner=self.request.user).values().order_by('date')
        a= 0
        d= []
       
        for i in data:
            g={}
            for j in i:
                if j=='date':
                   
                    d_obj = i[j]
                    d_day = d_obj.day
                    d_month = calender[d_obj.month]
                    d_year = d_obj.year
                    g['label'] =str(d_month)+' '+str(d_day)+', '+str(d_year)
                   
                elif j=='weight':
                    w_obj = i[j]
                    g['y'] = w_obj
           
            d.append(g)

        d.append({'label':'40','y':150})
        d.append({'label':'20','y':98})
        d.append({'label':10,'y':50})
       
        return d

    def get(self,request,*args,**kwargs):
        context = {'form':BodyWeightForm(),'data':self.datalist(BodyWeight)}
        return render(request,'main/chart.html',context)

    def post(self,request, *args, **kwargs):
        form = BodyWeightForm(request.POST)
        objs = BodyWeight.objects.filter(owner=request.user).values()
        today = datetime.today().strftime('%Y-%m-%d')
        today = today.split('-')
        if form.is_valid():
                bweight = form.save(commit=False)
                if objs:
                    for i in objs:
                        model_date = i['date']
                        if model_date.year == int(today[0]) and model_date.month == int(today[1]) and model_date.day==int(today[2]):
                            try:
                                a = 9/0
                            except ZeroDivisionError:
                                messages.warning(request,'Sorry,you have entered your weight for the day.')
                            finally:         
                                return HttpResponseRedirect(reverse_lazy('main:weight'))
                bweight.owner = request.user
                today = datetime.today().strftime('%Y-%m-%d')
                bweight.date = today
                bweight.save()        
                return HttpResponseRedirect(reverse_lazy('main:weight'))
        return render(request,'main/chart.html',{'form':form,'data':self.datalist(BodyWeight)})

class SignUpView(FormView):
    template_name = "main/signup_signin.html"
    form_class=CustomUserCreationForm
    
    def get_success_url(self):
        redirect_to =self.request.GET.get("next","/")
        return redirect_to
    def form_valid(self,form):
        response = super().form_valid(form)
        form.save()
        email = form.cleaned_data.get("email")
        raw_password = form.cleaned_data.get("password1")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        birth_date = form.cleaned_data.get("birth_date")
        gender= form.cleaned_data.get("gender")
        user =authenticate(email=email,password=raw_password,first_name=first_name,last_name=last_name,birth_date=birth_date,gender=gender)
        login(self.request,user)
        form.send_mail()
        messages.info(self.request,"You signed up successfully")
        return response

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        sign_in_form = AuthenticationForm()
        context['sign_in_form'] =sign_in_form
        return context
        

class SignInView(LoginView):
    template_name= "main/signup_signin.html"
    form_class = AuthenticationForm

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        sign_up_form = CustomUserCreationForm()
        context['sign_up_form'] = sign_up_form
        return context