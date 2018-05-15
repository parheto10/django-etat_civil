# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from django.contrib import admin
from .models import Naissance, Mairie, Centre, Mariage, Commune

def extrait_pdf(obj):
    return '<a href="{}">PDF</a>'.format(reverse('extraits:extrait_pdf', args=[obj.id]))
extrait_pdf.allow_tags = True
extrait_pdf.short_description = 'Extrait PDF'

class ExtraitsAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'prenoms', 'date_naiss', 'pere', 'mere', extrait_pdf]
    search_fields = ['prenoms', 'date_naiss', 'pere', 'mere', ]
    fieldsets = (
        ('INFORMATIONS GENERALES', {"fields": (('annee', 'numero_registre'), ('commune', 'centre'),)}),
        ('INFORMATIONS PERSONNELES', {"fields": (('nom', 'prenoms'), ('date_naiss', 'heure_naiss', 'maternite'), )}),
        ('PARENTS', {"fields": (('pere', 'profession_pere'), ('mere', 'profession_mere'), )}),
        ('MENTIONS (EVENTUELLEMENT)', {"fields": (('mariage', 'lieu_mariage'), 'conjoint', ('divorce', 'deces'), 'lieu_deces')}),
    )
admin.site.register(Naissance)
admin.site.register(Mairie)
admin.site.register(Centre)
admin.site.register(Mariage)
admin.site.register(Commune)

# Register your models here.
