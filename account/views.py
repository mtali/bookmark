from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section':'dashboard'})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'account/registration_done.html', {'new_user': user})
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': form})
