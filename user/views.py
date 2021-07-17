from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, PostCreationForm
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    return render(request, 'user/register.html', {'form':form})

@login_required()
def myposts(request):
    return render(request, 'user/myposts.html')

@login_required()
def create_post(request):
    myuser = request.user
    form = PostCreationForm()
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            newpost = Post(user=myuser, text=request.POST['text'])
            newpost.save()
            msg="Post created Successfully..."
            return render(request, 'user/createpost.html', {'form':form,'newpost':newpost, 'msg':msg})
        return render(request, 'user/createpost.html', {'form':form})
    else:
        return render(request, 'user/createpost.html', {'form':form})