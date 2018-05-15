from django.conf.urls import url
from .views import extrait_pdf
from django.utils.translation import gettext_lazy as _
urlpatterns = [
    url(r'^admin/extraits/(?P<extrait_id>\d+)/pdf/$', extrait_pdf, name='extrait_pdf'),
    #url(r'^render/(?P<extrait_id>\d+)/pdf/$', Pdf.as_view(), name='pdf')
]