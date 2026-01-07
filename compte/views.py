from django.contrib.auth import get_user_model,login,logout,authenticate
from django.shortcuts import render,redirect

# Create your views here.
User= get_user_model()#permet de recup le model user dans la bdd
def signup(request):
    if request.method == "POST":#si on as une req de type post
        #traitement du form
        username=request.POST.get("username")#on recup les données du champs username du form
        password=request.POST.get("password")
        user=User.objects.create_user(username=username,password=password)
        #permet de crée user avec toutes ces paramettre
        #permet de connecter l'user
        # Vérifier si username existe déjà
        login(request,user,)
        return redirect('index')                       
    return render(request, 'compte/signup.html')
def logout_user(request):
    logout(request)
    return redirect('index')

def login_user(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,
                          password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'compte/login.html')
