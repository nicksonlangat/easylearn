from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from accounts.models import User
from questions.models import Question
from blog.models import Series
from .forms import RegisterForm, ProfileUpdate, BioUpdate,SeriesForm
# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            messages.success(request, f"you're welcome to ")
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form':form})

@login_required
def profile(request):
    quuestion_list = Question.objects.filter(user=request.user).order_by('-created')
    series_list     =   Series.objects.filter(owner=request.user).order_by('-timestamp')


    ###Bio Update
    form = BioUpdate(instance=request.user)
    if request.method == "POST":
        form = BioUpdate(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f"your bio was updates successfully !!")
            return redirect('profile')

    context = {
        'series_list':series_list,
        'form':form,
        'quuestion_list':quuestion_list
    }
    return render(request, 'accounts/profile.html', context )

@login_required
def profileUpdate(request):
    form = ProfileUpdate(instance=request.user)
    if request.method == "POST":
        form = ProfileUpdate(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, F"You have successfully Updated Your Profile")
            return redirect('profile')
    return render(request, 'accounts/profile_update.html', {'form':form})



class ProfileList(ListView):
    model   =   User


class ProfileDetail(DetailView):
    model   =   User

