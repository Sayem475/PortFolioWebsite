from django.shortcuts import render, HttpResponse, get_object_or_404
# from django.views.generic import TemplateView, ListView
from .models import Skills, About, Portfolio, Contact, PortfolioImages
# Create your views here.
from django.views import View
from django.contrib import messages


class Home(View):
    def get(self, request):
        sk = Skills.objects.all()
        abouts = About.objects.all()
        portfolio = Portfolio.objects.all()
        context = {'skills': sk, 'abouts': abouts, 'portfolio': portfolio,}
        return render(request, 'base.html', context)

    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']
        if len(name) < 3 or len(email) < 5 or len(phone) < 8 or len(msg) < 10:
            messages.warning(request, 'Please fill the form Correctly.')
        else:
            contacts = Contact(name=name, email=email, phone=phone, msg=msg)
            contacts.save()
            messages.success(
                request, 'Congratulations! Your message has been sent Successfully...')
            
            sk = Skills.objects.all()
            abouts = About.objects.all()
            portfolio = Portfolio.objects.all()
        context = {'skills': sk, 'abouts': abouts, 'portfolio': portfolio}
        return render(request, 'base.html',context)
    

class Details(View):
    def get(self, request, id):
        portfolio = get_object_or_404(Portfolio, id=id)

        images = PortfolioImages.objects.filter(portfolio=portfolio)
        context = {'portfolio':portfolio ,'images': images}
        return render(request,'portfolio.html', context)

