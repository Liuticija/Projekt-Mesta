from django.shortcuts import render, get_object_or_404
from django.urls import reverse       
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from datetime import datetime
from .models import City
from .forms import CityForm



# Create your views here.


def about_city(request, id):
   
    #city = get_object_or_404(City, pk=id)
        
    city = City.objects.get(pk=id)
    return render(request, "informace/city.html", {
            "city": city,
            "nadpis" : f"{city.nazev.title()}",  
        })
    
    
    
def seznam(request):
    
    return render(request, "informace/seznam.html", {
        "seznam" : City.objects.all()
    })

def vilnius(request):
    return render(request, "informace/vilnius.html")

def zajimavosti(request):
    return render(request, "informace/zajimavosti.html" , {
        "zajimavost1" : "katedrální náměstí",
        "zajimavost2" : "gediminasův hrad" ,
       
    })
    
def index(request):
    pocet_obyvatel = 2.9
    prezident = "Gitanas Nauseda"
    return render(request, "informace/litva.html" , {
        "pocet": pocet_obyvatel,
        "prezident" : prezident,
        	
    })
    
def pridej(request):
    if request.method == "POST":
        formular = CityForm(request.POST)
        if formular.is_valid():
            city = City(
                   nazev=formular.cleaned_data["nazev"],
                   kraj = formular.cleaned_data["kraj"],
                   rozloha = formular.cleaned_data["rozloha"],
                   pocet = formular.cleaned_data["pocet"]
                        )
            city.save()
            return HttpResponseRedirect(reverse("dekuji"))
            
    else:
        formular = CityForm()
    return render(request, "informace/pridani.html", {
        "formular": formular,
    })
    
def dekuji(request):
   
    return render(request, "informace/dekuji.html")
    
    
def cislo(request, city):
    return HttpResponse(f"<h2> cislo {city}. </h2>")


def taxonomie(request, kategorie, druh):
   return HttpResponse(f"<p> Kategorie je {kategorie}.</p><p> Druh je {druh}.</p>")
