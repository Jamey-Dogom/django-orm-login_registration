from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from apps.helpers import copy_dict_partial, print_items_new_line
import bcrypt
import re


def index(request):
    return render(request, "app_lr/index.html")

def create_user(request):

    print(request.POST['dateofbirth'])

    if User.objects.registration_valid(request):
        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

        new_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hash_pw, birthdate = request.POST['dateofbirth'])

        print(new_user)

        request.session['user_id']= new_user.id 
        request.session['logged_in'] = True

        context = {
            "fn": new_user.first_name,
            "ln": new_user.last_name
        }

        return render(request, "app_lr/success.html", context)

    return redirect('/')

def login(request):
    check_usr = User.objects.filter(email = request.POST['username'])

    if check_usr:
        usr = check_usr[0]
        
        if bcrypt.checkpw(request.POST['password'].encode(), usr.password.encode()):

            request.session['user_id']= usr.id 
            request.session['logged_in'] = True

            return redirect('/success')

        else:
            messages.error(request, "Bad credentials")  
    else:
        messages.error(request, "Bad credentials")
    return redirect('/')


def success(request):
    if not request.session.get('user_id'):
        messages.error(request, "Bruh register or login")
        return redirect("/")

    in_usr = User.objects.filter(id = request.session['user_id'])
    usr = in_usr[0]
    context = {
        "fn": usr.first_name,
        "ln": usr.last_name 
        }
    return render(request, "app_lr/success.html", context)     

def logout(request):
    request.session.clear()
    return redirect('/')

