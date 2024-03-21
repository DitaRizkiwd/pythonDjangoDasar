from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class LoginView(View):
    def get(self,request):
        template_name = "authentication_login.html"
        context = {}
        return render(request, template_name, context=context)

    def post(self,request):
        template_name='authentication_login.html'
        username = request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponse("Login Success")

        else:
            context={
                'error':'wrong credentials',
                'username':'username is wrong',
                'password':'password mismatch'
            }
            return render(request, template_name, context=context)