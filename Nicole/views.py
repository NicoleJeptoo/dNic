from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader # for routing your templates
from django.views.decorators.csrf import csrf_exempt
from Nicole.models import Registration
from .forms import course


def Nicole(request):
    return HttpResponse("hellow welcome home")


def base(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())


def courses(request):
    template = loader.get_template('courses.html')
    return HttpResponse(template.render())

def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())


# Create your views here.

@csrf_exempt
def addstudent(request):
    if request.method == 'POST':
        formname = request.POST['name']
        formemail = request.POST['email']
        formage = request.POST['age']
        formcourse = request.POST['course']

    obj1=Registration(name=formname,email=formemail,age=formage,course=formcourse)
    obj1.save()
    #fetch the student data to be displayed
    data=Registration.objects.all()
    context = {'data':data}
    return render(request,'register.html',context)

def editstudent(request, id):
        data = Registration.objects.get(id=id);
        context = {'data': data}
        return render(request, 'updatestudent.html', context)


def updatestudent(request, id):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('Email')
    age = request.POST.get('age')
    course = request.POST.get('course')

    #modify the student details based on the student id given
    editstudent = Registration.objects.get(id=id)
    editstudent.studentname=name
    editstudent.email=email
    editstudent.age=age
    editstudent
    editstudent.save()


def deletestudent(request,id):
  deletestudent = Registration.objects.get(id=id)
  deletestudent.delete()
  return redirect('register')

def create_course(request):
    form = course()
    return render(request, 'create_course.html',{'form':form})



