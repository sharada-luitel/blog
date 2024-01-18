from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    views = {}
    views['services'] = Services.objects.all()
    views['feedbacks'] = Feedback.objects.all()


    return render(request,'index.html',views)

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        na = request.POST['name']
        em = request.POST['email']
        sub = request.POST['subject']
        mes = request.POST['message']
        data = Contact.objects.create(
            name=na,
            email=em,
            subject=sub,
            message=mes
        )
        data.save()
    return render(request,'contact.html')

def portfolio(request):
    return render(request,'portfolio.html')

def price(request):
    return render(request,'price.html')

def services(request):
    return render(request,'services.html')


def blog_home(request):
    views = {}
    views['blogs'] = Blog.objects.all()
    return render(request,'blog-home.html',views)

def blog_single(request, id):
    views = {}
    views['blog_details'] = Blog.objects.filter(id = id)

    return render(request,'blog-single.html',views)