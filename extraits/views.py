# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Naissance
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template


import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.views.generic import View
from django.utils import timezone
#from .render import Render

from weasyprint import HTML
import tempfile
from django.conf import settings
import weasyprint

"""
class Pdf(View):
    def get(self, request):
        extraits = Extrait.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'extraits': extraits,
            'request': request
        }
        return Render.render('pdf/extrait', params)
"""

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL # Typically /static/
    sRoot = settings.STATIC_ROOT # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL # Typically /static/media/
    mRoot = settings.MEDIA_ROOT # Typically /home/userX/project_static/media/
    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri # handle absolute uri (ie: http://some.tld/foo.png)
    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
    'media URI must start with %s or %s' % (sUrl, mUrl)
    )
    return path

def render_to_pdf(request):
    template_path = 'user_printer.html'
    extraits = Naissance.objects.all()
    context = {'extraits': extraits}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(Context(context))
    # create a pdf
    pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def extrait_pdf(request, extrait_id):
    """Generate pdf."""
    # Model data
    extrait = get_object_or_404(Naissance, id = extrait_id)

    # Rendered
    html = render_to_string('pdf/pdf.html', {'extrait': extrait})
    #html = HTML(string=html)
    #result = html.write_pdf()
    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'filename = "extrait de {} {}.pdf"' .format(extrait.nom, extrait.prenoms)
    weasyprint.HTML(string=html)\
        .write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT +
                                 '/css/bootstrap.min.css')
        ])
    return response




# Create your views here.
