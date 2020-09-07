from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import RegisterUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def loginForm(request):
    if request.user.is_authenticated:
        return redirect('/blog')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('/blog')
        else:
            messages.info(request,'Username or Password is Incorrect')

    return render(request,'accounts/loginForm.html')

def registerForm(request):
    if request.user.is_authenticated:
        return redirect('/blog')

    frm = RegisterUser()
    if request.method == 'POST':
        frm = RegisterUser(request.POST)
        if frm.is_valid():
            frm.save(commit = True)
            # print('success')        
            return redirect('loginForm')

    context = {'form':frm}
    return render(request,'accounts/registerForm.html',context)


@login_required(login_url='/accounts/loginForm/')
def logoutUser(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/accounts/loginForm/')
def profile(request,username):
    if request.user.is_authenticated:
        user = User.objects.get(username=username)
        context = {'user':user}
        return render(request,'accounts/profile.html',context)
    return (request,'accounts/loginForm.html')

@login_required(login_url='/accounts/loginForm/')
def changePassword(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        user.set_password(request.POST['new-pswd'])
        user.save()
        update_session_auth_hash(request, user)
        messages.success(request, 'Your password was successfully updated!')
        return redirect('profile',username=user.username)
    return render(request,'accounts/loginForm.html')
    