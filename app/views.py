from django.shortcuts import render, redirect
from .models import SiteWeb

# Create your views here.


def accueil(request):
    sites = SiteWeb.objects.all()
    return render(request, "Accueil/accueil.html",{"sites":sites})

def detail(request, p):
    try:
        param = p.find("-")
        idSite = int(p[0:param])
        site = SiteWeb.objects.get(pk=idSite)
    except:
        return redirect("/")
    lien_url = site.url
    if(lien_url.find("https://") == 0):
        lien_url = lien_url.replace("https://", "",1)
    elif (lien_url.find("http://") == 0):
        lien_url = lien_url.replace("http://", "",1)
    return render(request, "Detail/detail.html", {"lien_url":lien_url})
