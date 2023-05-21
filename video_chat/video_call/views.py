from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
# Create your views here.

def index(request):
    return render(request, 'video_call/index.html')

def signup(request):
    if request.method == 'POST':
        # check if form is submited
        form = SignUpForm(request.POST)

        if form.is_valid():
            # check if username do not exist
            # submited password is same and valid
            user = form.save()

            login(request, user)
            # this method will take submited form and request ask login

            return redirect('index')
    else:
        form = SignUpForm()
    
    return render(request, 'video_call/signup.html', {'form': form})
