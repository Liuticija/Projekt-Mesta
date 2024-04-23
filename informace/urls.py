from django.urls import path #import z hlavni urls.py
from . import views

#router
urlpatterns = [
   path("vilnius/", views.vilnius, name="vilnius"),
   path("zajimavosti/", views.zajimavosti, name="zajimavosti"),
   path("seznam/", views.seznam, name="seznam_city"),
   
   #path("<int:city>/", views.cislo),
   path("<int:id>/", views.about_city, name="city"),
   path("<kategorie>/<druh>/", views.taxonomie),
   path("", views.index, name="hlavni"),
   path("pridani/", views.pridej , name = "pridani"),
   path("dekuji/", views.dekuji , name = "dekuji"),
   

]
