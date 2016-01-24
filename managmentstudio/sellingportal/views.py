from django.shortcuts import render
#from django.http import HttpResponse
from sellingportal import models
from sellingportal import  forms
def Index(request):


    context={'name':'hussein',
             'age':26,
             'jobs':['eng', 'dev', 'lecture'],

             }
    return render(request,'index.html',context)

  #return HttpResponse('welcome to index page')


def Student(request):
    stuents=models.Student.objects.all()
    context={
        'stuents':stuents
    }
    return render(request,'students.html',context)



def StudentDegree(request,student_id):
    degrees=models.Degree.objects.filter(student_id=student_id )
    stuents=models.Student.objects.get(id=student_id)
    form_data=forms.DegreeRegistrar(request.POST or None)
    msg=''
    if form_data.is_valid():
       degree=models.Degree()
       degree.student_drgee=form_data.cleaned_data['student_drgee']
       degree.student_id=stuents
       degree.save()
       msg='data is saved'
    context={
        'degrees':degrees,
         'formregister':form_data,
         'msg':msg
    }

    return render(request,'degrees.html',context)




def Register(request):

  form_data=forms.UserRegistrar(request.POST or None)
  msg=''
  if form_data.is_valid():
       student=models.Student()
       student.first_name=form_data.cleaned_data['first_name']
       student.last_name=form_data.cleaned_data['last_name']
       student.age=form_data.cleaned_data['age']
       student.date_birth=form_data.cleaned_data['date_birth']
       student.save()
       msg='data is saved'

  context={
        'formregister':form_data,
      'msg':msg
    }
  return render(request,'regiester.html',context)



































# Create your views here.
#from django.http import HttpResponse

#def Details(request,student_id):
    # return HttpResponse('hellow student id:' + student_id)