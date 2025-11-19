from django.urls import path, include
from rest_framework.routers import DefaultRouter
from barrio import views
from .views import *

router = DefaultRouter()
router.register(r'obras', ObraMisionalViewSet)


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('hjovenes/', views.hjovenes, name='hjovenes'),
    path('mjovenes/', views.mjovenes, name='mjovenes'),
    path('primaria/', views.primaria, name='primaria'),
    path('quorum/', views.quorum, name='quorum'),
    path('obispado/', views.obispado, name='obispado'),
    path('socsoc/', views.socsoc, name='socsoc'),
    path('api/', include(router.urls)),
]

