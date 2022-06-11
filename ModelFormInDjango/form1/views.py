from django.shortcuts import render
from . forms import StudentForm
from django.http import HttpResponseRedirect
from .models import StudentRegistration


def myDjangoForm(request):
    if request.method == 'POST':
        AnotherMethodOfModelForm = StudentRegistration.objects.get(pk = 1)
        fm = StudentForm(request.POST, instance = AnotherMethodOfModelForm)
        if fm.is_valid():
            #print('Form validated...\n')
            #name = fm.cleaned_data['name']
            #email = fm.cleaned_data['email']
            #password = fm.cleaned_data['password']
            #regitration = StudentRegistration(name = name, email = email, password = password)
            #regitration.save()
            fm.save()
            return HttpResponseRedirect('/modelform/success/')
    else:
        fm = StudentForm()  # bounded form data
        print("This came from GET method ")
    return render(request, 'form1/Index.html', {'formDjango': fm})


def RegistrationSuccess(request):
    return render(request, 'form1/clickResponse.html')
# StudentForm(auto_id = True,False,chaini_%s etc)
