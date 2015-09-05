from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm


def login_page(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user and user.is_active:
			login(request, user)
			return redirect('/edit/')
		return redirect('/login/')

	form = AuthenticationForm()
	return render(request, 'login.html', {'form': form})


def edit_page(request):
	return render(request, 'edit.html')

