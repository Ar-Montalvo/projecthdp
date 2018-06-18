from django.conf.urls import url,include
from apps.usuario.views import Usuario
app_name="usuario"
urlpatterns = [
 url(r'user',Usuario.as_view(), name='plantilla_usuario')
]