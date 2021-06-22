#from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, redirect
from .form import CalculationForm
from .models import Calculation

# Create your views here.

def calculate(request):
   if request.method == 'POST':
       form = CalculationForm(request.POST)
       operator = request.POST.get('calculation_type')
       num_one = request.POST.get('num_one')
       num_two = request.POST.get('num_two')
       if form.is_valid():
           if(operator == '0'):
               result = int(num_one) + int(num_two)
           elif(operator == '1'):
               result = int(num_one) - int(num_two)
           elif(operator == '2'):
               result = int(num_one) * int(num_two)
           elif((operator == '3') and (int(num_two) == 0)):
               result = 'Undefined'
           else:
               result = int(num_one) / int(num_two)
           
           calculation = form.save(commit=False)
           calculation.result = result

           if(operator == '0'):
               calculation.operator = '+'
           elif(operator == '1'):
                calculation.operator = '-'
           elif(operator == '2'):
                calculation.operator = '*'
           else:
                calculation.operator = '/'
           calculation.save()
           return redirect('results')
   else:
       form = CalculationForm()
   return render(request, 'home.html', {'form':form})

def results(request):
   past = Calculation.objects.all()
   return render(request, 'results.html', {'past':past})