from django.db import models

# Create your models here.

class Divadlo(models.Model):
    nazev = models.CharField(max_length=50)
    umisteni = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nazev
     

class City(models.Model):
    nazev = models.CharField(max_length=30)
    kraj = models.CharField(max_length=50)
    rozloha = models.IntegerField()
    pocet = models.IntegerField()
    region = models.CharField(max_length=50, null=True)
    divadlo = models.ForeignKey(Divadlo, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.nazev} je hlavním městem {self.kraj}, má rozlohu {self.rozloha} km² a {self.pocet} obyvatelů."
    
    class Meta:
        verbose_name_plural = "Cities"
        ordering = [ "nazev", "id"]
    



    
    
        
        
        
    
    
    

