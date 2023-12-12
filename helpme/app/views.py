from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

from .models import *
from .forms import *
from .decorators import *

# Create your views here.
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # group = Group.objects.get(name='Team') 
            # group.user_set.add(user)
            return redirect('teamDashboard')

        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'app/loginUser.html')

@authenticated_user
def logoutUser(request):
    logout(request)
    return redirect('loginUser')

def registerUser(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('registerTeam')

    context = {
        'form': form,
    }

    return render(request, 'app/registerUser.html', context)

def registerTeam(request):
    form = TeamForm()
    
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save()
            team.user = request.user
            team.save()
            group = Group.objects.get(name='Team') 
            group.user_set.add(request.user)            
            return redirect('teamDashboard')

    context = {
        "form": form,
        }
    
    return render(request, "app/registerTeam.html", context)

@mentor_only
def mentorDashboard(request):
    mentor = Mentor.objects.get(user = request.user)  
    

    context = {
        "mentor": mentor,
        }
    
    return render(request, "app/mentorDashboard.html", context)

@team_only
def teamDashboard(request):
    team = Team.objects.get(user = request.user)  
    tickets = Ticket.objects.filter(team=team)
    form = TicketForm()

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            ticket.team = team
            ticket.save()        
            return redirect('teamDashboard')
    

    context = {
        "team": team,
        "form": form,
        "tickets": tickets,
        }
    
    return render(request, "app/teamDashboard.html", context)