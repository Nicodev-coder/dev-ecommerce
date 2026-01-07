from django.shortcuts import render
from new.models import Newsletter
# Create your views here.
def newsletter(request):
    message=""
    if request.method == "POST":#si on as une req de type post
        email=request.POST.get("email")
        if email:  
            if not Newsletter.objects.filter(email=email).exists():
                Newsletter.objects.create(email=email)
                message = "Inscription réussie !"
            else:
                message=" Cet email est déjà inscrit."                 
    return render(request, 'new/news.html',context={"message":message})



def letter(request):
    message = ""
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            if not Newsletter.objects.filter(email=email).exists():
                Newsletter.objects.create(email=email)
                message = "Inscription réussie !"
            else:
                message = "Cet email est déjà inscrit."
        else:
            message = "Veuillez entrer une adresse email valide."
    
    return render(request, 'app/index.html', {'message': message})
