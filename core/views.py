from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from core.models import Ring, Bell
from django.contrib.auth.models import User

# Create your views here.
def splash(request):
    if not request.user.is_authenticated:
        return redirect('/login') 
    return render(request, 'splash.html', {})

def bell(request):
    if request.method == 'POST':
        title, body, price = request.POST['title'], request.POST['body'], request.POST['price']
        Bell.objects.create(title=title, body=body, price=price, author=request.user)
    bells = Bell.objects.all().order_by('-id')
    return render(request, 'bell.html', {'bells': bells})

def ring(request):
    if request.method == 'POST':
        title, body, price = request.POST['title'], request.POST['body'], request.POST['price']
        Ring.objects.create(title=title, body=body, price=price, author=request.user)
    rings = Ring.objects.all().order_by('-id')
    return render(request, 'ring.html', {'rings': rings})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/') 
    if request.method == 'POST':
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return redirect('/login?error=failure')
        login(request, user)
        return redirect('/')
    return render(request, 'accounts.html')

def signup_view(request):
    if request.method == 'POST':
        username, password, email = request.POST['username'], request.POST['password'], request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect('/')
    return render(request, 'accounts.html')

def logout_view(request):
    logout(request)
    return redirect('/login')

def delete_bell(request): 
    bell = Bell.objects.get(id=request.GET['id'])
    bell.delete()
    return redirect('/')

def delete_ring(request): 
    ring = Ring.objects.get(id=request.GET['id'])
    ring.delete()
    return redirect('/')

def profile_view(request, username):
    if not request.user.is_authenticated:
        return redirect('/login') 
    if len(request.user.username) == 0:
        author_user = User.objects.get(username=request.user.username)
    else:
        author_user = User.objects.get(username=username)
    bells = Bell.objects.filter(author=author_user)
    rings = Ring.objects.filter(author=author_user)
    return render(request, 'profile.html', {'rings': rings, 'bells': bells})