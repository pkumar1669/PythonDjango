from django.shortcuts import render
from .models import Soft_course
# Create your views here.
def index(request):
    course1 = Soft_course()
    course2 = Soft_course()
    course3 = Soft_course()

    course1.name = 'Python'
    course1.des = "Simple and powerful programming langauge"
    course1.price = 500

    course2.name = "HTML"
    course2.des = "Simple Markup language or Static Web Pages"
    course2.price = 50

    course3.name = "Tkinter"
    course3.des = "GUI Apps"
    course3.price = 200

    return render(request,'index.html',{'course1':course1,'course2':course2,'course3':course3})