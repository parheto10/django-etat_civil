# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from django.contrib import admin
from .models import Naissance, Mairie, Centre, Mariage, Commune

def pdf(obj):
    return '<a href="{}">PDF</a>'.format(reverse('extraits:pdf', args=[obj.id]))
pdf.allow_tags = True
pdf.short_description = 'Extrait PDF'

class ExtraitsAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'prenoms', 'date_naiss', 'pere', 'mere', pdf]
    # search_fields = ['prenoms', 'date_naiss', 'pere', 'mere', ]
    fieldsets = (
        ('INFORMATIONS GENERALES', {"fields": (('annee', 'numero_registre'), ('categorie'),)}),
        ('INFORMATIONS PERSONNELES', {"fields": ('sexe',('nom', 'prenoms'), ('date_naiss', 'heure_naiss'), 'hopital', )}),
        ('PARENTS', {"fields": (('mere', 'profession_mere'), ('pere', 'profession_pere'), )}),
        #('MENTIONS (EVENTUELLEMENT)', {"fields": (('mariage', 'lieu_mariage'), 'conjoint', ('divorce', 'deces'), 'lieu_deces')}),
    )


class MariageAdmin(admin.ModelAdmin):
    list_display = ['numero', 'requerant1', 'conjoint', 'regime', 'date_mariage', 'heure_mariage', 'lieu_mariage']
    # search_fields = ['prenoms', 'date_naiss', 'pere', 'mere', ]
    exclude = ("numero ",)
    readonly_fields = ('numero', )
    fieldsets = (
        ('INFORMATIONS DEMANDEUR', {"fields": (('numero', 'categorie'), ('requerant1'), ('profession_req1', 'domicile_req1'), ('date_req1', 'lieu_naiss_req1'),)}),
        ('PARENTS ET TEMOINS DU DEMANDEUR', {"fields": (('pere_req1'), ('mere_req1'), 'temoin_req1', ('tel_temoin_req1', 'profession_temoin_req1'),)}),
        ('INFORMATIONS CONJOINT(E)', {"fields": ('requerant2', ('profession_req2', 'domicile_req2'), ('date_req2', 'lieu_naiss_req2'),)}),
        ('PARENTS ET TEMOINS DU CONJOINT(E)', {"fields": (('pere_req2'), ('mere_req2'), ('temoin_req2'), ('tel_temoin_req2', 'profession_temoin_req2'),)}),
        ('REGIME ET CEREMONIE', {"fields": (('regime'), ('date_mariage', 'heure_mariage'), ('lieu_mariage'))}),

        #('MENTIONS (EVENTUELLEMENT)', {"fields": (('mariage', 'lieu_mariage'), 'conjoint', ('divorce', 'deces'), 'lieu_deces')}),
    )
admin.site.register(Naissance, ExtraitsAdmin)
admin.site.register(Mairie)
admin.site.register(Centre)
admin.site.register(Mariage, MariageAdmin)
admin.site.register(Commune)

# Register your models here.
