from django.urls import path
from django.urls import path, include
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('roles/', RolesListCreate.as_view(), name='roles-list-create'),
    path('roles/<int:pk>/', RolesRetrieveUpdateDestroy.as_view(), name='roles-retrieve-update-destroy'),
    path('planes/', PlanesListCreate.as_view(), name='planes-list-create'),
    path('planes/<int:pk>/', PlanesRetrieveUpdateDestroy.as_view(), name='planes-retrieve-update-destroy'),
    path('usuarios/', UsuarioListCreate.as_view(), name='usuarios-list-create'),
    path('usuarios/<int:pk>/', UsuarioRetrieveUpdateDestroy.as_view(), name='usuarios-retrieve-update-destroy'),
    path('planesusuario/', PlanesUsuarioListCreate.as_view(), name='planesusuario-list-create'),
    path('planesusuario/<int:pk>/', PlanesUsuarioRetrieveUpdateDestroy.as_view(), name='planesusuario-retrieve-update-destroy'),
    path('notificaciones/', NotificacionListCreate.as_view(), name='notificaciones-list-create'),
    path('notificaciones/<int:pk>/', NotificacionRetrieveUpdateDestroy.as_view(), name='notificaciones-retrieve-update-destroy'),
    path('sorteos/', SorteoListCreate.as_view(), name='sorteos-list-create'),
    path('sorteos/<int:pk>/', SorteoRetrieveUpdateDestroy.as_view(), name='sorteos-retrieve-update-destroy'),
    path('historialsorteos/', HistorialSorteoListCreate.as_view(), name='historialsorteos-list-create'),
    path('historialsorteos/<int:pk>/', HistorialSorteoRetrieveUpdateDestroy.as_view(), name='historialsorteos-retrieve-update-destroy'),
    path('participantes/', ParticipanteListCreate.as_view(), name='participantes-list-create'),
    path('participantes/<int:pk>/', ParticipanteRetrieveUpdateDestroy.as_view(), name='participantes-retrieve-update-destroy'),
    path('sorteoparticipantes/', SorteoParticipanteListCreate.as_view(), name='sorteoparticipantes-list-create'),
    path('sorteoparticipantes/<int:pk>/', SorteoParticipanteRetrieveUpdateDestroy.as_view(), name='sorteoparticipantes-retrieve-update-destroy'),
    path('ganadores/', GanadoresListCreate.as_view(), name='ganadores-list-create'),
    path('ganadores/<int:pk>/', GanadoresRetrieveUpdateDestroy.as_view(), name='ganadores-retrieve-update-destroy'),
    path('publicaciones/', PublicacionListCreate.as_view(), name='publicaciones-list-create'),
    path('publicaciones/<int:pk>/', PublicacionRetrieveUpdateDestroy.as_view(), name='publicaciones-retrieve-update-destroy'),
    path('admin/', admin.site.urls),
]


urlpatterns = [
    # Otras rutas definidas aquí
     re_path(r'^.*$', TemplateView.as_view(template_name='dist/giveaway/index.html')),

]
urlpatterns += staticfiles_urlpatterns()