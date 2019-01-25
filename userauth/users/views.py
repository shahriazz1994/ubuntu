from django.shortcuts import render, redirect
# from users import user_manager
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_login_view(request):
    # Creating user object & authenticating.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    # checking if user is valid
        if user is not None:
            login(request, user)
            messages.success(request, f'{user.username} is logged in successfully')
            return redirect('landing_page')  # on successful login redirect to home
        else:
            messages.info(request, f'Invalid Username or Password.')
            return redirect('login')  # on failure redirect to login itself
    else:
        return render(request, 'users/login.html', {})


def user_logout_view(request):
    logout(request)
    messages.warning(request, f'You have been logged out. Login Again.')
    return redirect('login')


@login_required(redirect_field_name='login', login_url='login')
def user_profile_view(request):
    if User.is_authenticated:
        return render(request, 'users/profile.html', {})
    else:
        messages.warning(request, f'You are not logged in please login first.')


def user_register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(username=username, password=password1)
            login(request, user)
            messages.success(request, f'{user.username} Registered successfully.')
            return redirect('landing_page')
    else:
        form = UserCreationForm()

    context = {
            'form': form,
        }
    return render(request, 'users/register.html', context)

