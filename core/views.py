from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from core.models import Ring, Bell, Comment
from django.contrib.auth.models import User

user_revenue = dict()
user_expense = dict() 

def splash(request):
    return render(request, 'splash.html', {})

# going to the bell page and making a bell 
def bell(request):
    if not request.user.is_authenticated:
        return redirect('/login') 
    if request.method == 'POST':
        title, body, price = request.POST['title'], request.POST['body'], request.POST['price']
        res = price.replace('.', '', 1)
        if len(title) != 0 and len(price) != 0 and res.isnumeric():
            price = round(float(price), 2)
            Bell.objects.create(title=title, body=body, price=price, author=request.user)
    bells = Bell.objects.all().order_by('-id')
    return render(request, 'bell.html', {'bells': bells})

# going to the ring page and making a ring 
def ring(request):
    if not request.user.is_authenticated:
        return redirect('/login') 
    if request.method == 'POST':
        title, body, price = request.POST['title'], request.POST['body'], request.POST['price']
        if len(title) != 0 and len(price) != 0 and price.isnumeric():
            price = round(float(price), 2)
            Ring.objects.create(title=title, body=body, price=price, author=request.user)
    rings = Ring.objects.all().order_by('-id')
    comments = {}
    return render(request, 'ring.html', {'rings': rings, 'comments': comments})

def comment(request):
    if request.method == 'POST':
        postId, body, postType = request.POST['postId'], request.POST['body'], request.POST['postType']
        if len(body) != 0:
            if str(postType) == 'Ring': # comment is on a ring
                ring = Ring.objects.get(id=postId)
                comment = Comment.objects.create(post_ring=ring, body=body, author=request.user)
                return redirect('/ring')
            else: # comment is on a bell 
                bell = Bell.objects.get(id=postId)
                comment = Comment.objects.create(post_bell=bell, body=body, author=request.user)
                return redirect('/bell')
        if postType == 'Ring': # if the user did not comment anything
            return redirect('/ring')
        return redirect('/bell')
            
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
    return redirect('/bell')

def delete_ring(request): 
    ring = Ring.objects.get(id=request.GET['id'])
    ring.delete()
    return redirect('/ring')

def profile_view(request, username):
    if not request.user.is_authenticated:
        return redirect('/login') 
    if len(request.user.username) == 0:
        author_user = User.objects.get(username=request.user.username)
    else:
        author_user = User.objects.get(username=username)
    bells = Bell.objects.filter(author=author_user)
    rings = Ring.objects.filter(author=author_user)
    return render(request, 'profile.html', {'rings': rings, 'bells': bells, 'username': username})