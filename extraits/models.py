# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

def number():
    no = Naissance.objects.count()
    if no == None:
        return 1
    else:
        return no + 1

Categorie = (
    ('ACTE DE NAISSANCES',(
        ("normal", "NORMAL"),
        ("mariage", "EN VUE DE MARIAGE"),
        )
     ),
    ('acte_mariage', 'ACTE DE MARIAGE'),
    ('acte_mariage' ,'ACTE DE DECES'),
)

class Commune(models.Model):
    libelle = models.CharField(max_length=250, verbose_name="Commune")

class Mairie(models.Model):
    Commune    = models.ForeignKey(Commune)
    maire      = models.CharField(max_length=500, verbose_name="Nom et Prenoms du Maire")
    telephone1 = models.CharField(max_length=50, verbose_name="Telephone 1")
    telephone2 = models.CharField(max_length=50, verbose_name="Telephone 2", blank=True, null=True)
    adresse    = models.CharField(max_length=100, verbose_name="Adresse Postale", blank=True)
    email      = models.CharField(max_length=100, verbose_name="Adresse Email", blank=True)
    site       = models.CharField(max_length=100, verbose_name="Site Web", blank=True)
    logo       = models.ImageField(upload_to='logos', blank=True, null=True)

    def __unicode__(self):
        return self.Commune.libelle

class Centre(models.Model):
    #commune = models.ForeignKey(Mairie)
    libelle_centre = models.CharField(max_length=500, verbose_name="Centre de Santé")
    situation = models.CharField(max_length=500, verbose_name="Situation Geographique du Centre")

    def __unicode__(self):
        return self.libelle_centre


class Naissance(models.Model):

    YEAR_CHOICES = []
    for r in range(1900, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    Sexe = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )

    # Infos Gles
    numero_registre = models.CharField(max_length=150, verbose_name='Numero du Registre')
    annee = models.IntegerField(verbose_name='Annee de Naissance', choices=YEAR_CHOICES,
                                default=datetime.datetime.now().year)
    categorie = models.IntegerField(verbose_name='Type de Document', choices=Categorie)
    #centre = models.ForeignKey(Centre)

    # informations recipiendaire
    sexe = models.CharField(max_length=150, verbose_name='Precise le sexe', choices=Sexe)
    nom = models.CharField(max_length=250, verbose_name='Nom')
    prenoms = models.CharField(max_length=250, verbose_name='Prenoms')
    date_naiss = models.DateField(verbose_name='Date de Naissance')
    heure_naiss = models.TimeField(verbose_name='Heure de Naissance')
    hopital = models.ForeignKey(Centre)

    # parents
    pere = models.CharField(max_length=250, verbose_name='Nom et Prénoms du Pere')
    profession_pere = models.CharField(max_length=250, verbose_name='Profession du Pere')
    mere = models.CharField(max_length=250, verbose_name='Nom et Prénoms de la Mere')
    profession_mere = models.CharField(max_length=250, verbose_name='Profession de la Mere')
    ajouter_le = models.DateTimeField(auto_now_add=True, auto_now=False)
    modifier_le = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = "Actes de Naissance"
        verbose_name = "Acte de naissance"


def num_mariage():
    no = Mariage.objects.count()
    if no == None:
        return 1
    else:
        return no + 1

class Mariage(models.Model):
    Requerant = (
        ('epoux(se)', 'EPOUX(se)'),
        ('conjoint(e)', 'CONJOINT(E)'),
    )

    Regime= (
        ('simple', 'SIMPLE'),
        ('communaute', 'COMUAUTE DE BIEN'),
    )

    categorie = models.IntegerField(verbose_name='Type de Document', choices=Categorie)
    numero = models.CharField(max_length=5, unique=True, default=num_mariage)
    requerant1 = models.CharField(max_length=500, verbose_name="Nom et Prenoms du Marie(e)")
    profession_req1 = models.CharField(max_length=500, verbose_name="Profession du Marie(e)")
    domicile_req1   = models.CharField(max_length=500, verbose_name="Lieu de Domicile du Marie(e)")
    date_req1   = models.DateField(verbose_name="Date de Naissance du Marie(e)")
    lieu_naiss_req1 = models.CharField(max_length=500, verbose_name="Lieu de Naissance du Marie(e)")
    pere_req1 = models.CharField(max_length=250, verbose_name='Nom et Prénoms du Pere du Marie(e)')
    mere_req1 = models.CharField(max_length=250, verbose_name='Nom et Prénoms de la Mere du Marie(e)')
    temoin_req1 = models.CharField(max_length=250, verbose_name='Nom et Prénoms du Témoin du Marie(e)')
    tel_temoin_req1 = models.CharField(max_length=250, verbose_name='Contact Temoin du Marie(e)')
    profession_temoin_req1 = models.CharField(max_length=250, verbose_name='Profession du Temoin du Marie(e)')

    conjoint   = models.CharField(max_length=150, verbose_name="CONJOINT(E)", choices=Requerant)
    requerant2 = models.CharField(max_length=500, verbose_name="Nom et Prenoms du CONJOINT(E)")
    profession_req2 = models.CharField(max_length=500, verbose_name="Profession du CONJOINT(E)")
    domicile_req2 = models.CharField(max_length=500, verbose_name="Lieu de Domicile du CONJOINT(E)")
    date_req2 = models.DateField(verbose_name="Date de Naissance du CONJOINT(E)")
    lieu_naiss_req2 = models.CharField(max_length=500, verbose_name="Lieu de Naissance du CONJOINT(E)")
    pere_req2 = models.CharField(max_length=250, verbose_name='Nom et Prénoms du Pere duCONJOINT(E)')
    mere_req2 = models.CharField(max_length=250, verbose_name='Nom et Prénoms de la Mere du CONJOINT(E)')
    temoin_req2 = models.CharField(max_length=250, verbose_name='Nom et Prénoms du Témoin du CONJOINT(E)')
    tel_temoin_req2 = models.CharField(max_length=250, verbose_name='Contact Temoin du CONJOINT(E)')
    profession_temoin_req2 = models.CharField(max_length=250, verbose_name='Profession du Temoin du CONJOINT(E)')
    regime = models.CharField(max_length=150, verbose_name="Type de Regime", choices=Regime)
    date_mariage = models.DateField(verbose_name="Date du Mariage")
    heure_mariage = models.DateField(verbose_name="Heure du Mariage")
    lieu_mariage = models.CharField(max_length=500, verbose_name="Lieu de Celebartion du Mariage")

    class Meta:
        verbose_name_plural = "Actes de Mariage"
        verbose_name = "Acte de Mariage"



  # Create your models here.
