from functools import wraps
from django.contrib.auth import authenticate, login
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def login_required(view_func):
  @wraps(view_func)
  def wrapper(request, *args, **kwargs):
    if request.user.is_authenticated:
      return view_func(request, *args, **kwargs)
    else:
      return redirect('login')
  return wrapper

def admin_required(view_func):
  @wraps(view_func)
  def wrapper(request, *args, **kwargs):
    if request.user.is_staff:
      return view_func(request, *args, **kwargs)
    else:
      return HttpResponseForbidden()
  return wrapper
