from django.db import models

class Kategoria(models.Model):
    nimi = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nimi


class Tehtava(models.Model):
    otsikko = models.CharField(max_length=200)
    kategoria = models.ForeignKey(
        Kategoria,
       on_delete=models.RESTRICT,
       null=True,
    )

    
    
    
    
    
    
    
    
    
    
    
    def __str__(self):
        return self.otsikko
    