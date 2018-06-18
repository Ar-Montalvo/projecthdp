from django.conf.urls import url
from sccc.views import Index, Cultivo
app_name="sccc"
urlpatterns = [
 url(r'^',Index.as_view(), name='plantilla_inicio_vacio'),
 url(r'inicio',Index.as_view(), name='plantilla_inicio'),
 url(r'cultivo',Cultivo.as_view(), name='plantilla_cultivo')
]