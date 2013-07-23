# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
import datetime
from models import DbConnections

@login_required
def index_view(request):
  qs = DbConnections.objects.all()
  return render(request, 'index.html', {"connlist": qs})

def logout_view(request):
  logout(request)
  return redirect('/')
        
