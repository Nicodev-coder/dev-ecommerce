from django.http import FileResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Ebook,UserEbook
from django.shortcuts import render,get_object_or_404


# Create your views here.
def index(request):
    ebooks=Ebook.objects.all()
    recherche= request.GET.get('recherce')
    if recherche != "" and recherche is not None:
        ebooks=Ebook.objects.filter(titre__icontains=recherche)
    return render(request, 'app/index.html', context={"ebooks":ebooks})

def product_detail(request, slug):
    ebooks=get_object_or_404(Ebook, slug=slug)
    #get_object permet de recup les object si elle existe pas elle renvois 404
    return render(request,'app/download.html',context={"ebooks":ebooks})

@login_required
def mes_ebooks(request):
    """
    Affiche les ebooks téléchargés par l'utilisateur connecté.
    """
    ebooks = request.user.mes_ebooks.select_related("ebook")
    return render(request, "app/mes_ebook.html", {"ebooks": ebooks})

def telecharger_ebook(request, slug):
    ebook = get_object_or_404(Ebook, slug=slug)

    # ➕ AJOUT ICI
    if request.user.is_authenticated:
        UserEbook.objects.get_or_create(
            user=request.user,
            ebook=ebook
        )

    return FileResponse(
        ebook.pdf.open(),
        as_attachment=True,
        filename=ebook.pdf.name
    )