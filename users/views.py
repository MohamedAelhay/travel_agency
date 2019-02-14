from django.shortcuts    import render
from django.http         import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate,logout
from django.shortcuts    import render, redirect
from .forms              import UserSignUpForm, UserloginForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required
def index(request):
    if request.user.is_authenticated():
        return HttpResponse('<h1>Hello ' + request.user.username  + '</h1>')
    else:
        return HttpResponse('<h1>Hello Stranger!</h1>')

def signup_view(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST, request.FILES)
    else:
        form = UserSignUpForm(None)

    if form.is_valid():
            user         = form.save(commit = False)
            username     = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user.set_password(raw_password)            
            user.save()

            #login the user
            user = authenticate(username=username, password=raw_password)
    
            if user:        
                login(request, user)
                return redirect('/users/')
            else:
                return render(request, 'registration/signup.html', {'form', form})
    
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    form = UserloginForm(request.POST or None)
    
    if form.is_valid():
            username     = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=raw_password)
            
            if user:        
                login(request, user)
                return redirect('/users/')
            else:
                error = "either username or password is wrong"
                return render(request, 'registration/login.html', {'form': form,'error':error})
                
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/users/')