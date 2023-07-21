from django.urls import path
from Kiyafetler.api import views as api_views

urlpatterns = [
   path('Kiyafetler/',api_views.KiyafetListCreateAPIView.as_view(), name='Kiyafet-listesi' ),
   path('Kiyafetler/<int:pk>', api_views.KiyafetDetailAPIView.as_view(), name='Kiyafet-bilgileri'),
   path('Kiyafetler/<int:Kiyafet_pk>/Puan_ver', api_views.PuanCreateAPIView.as_view(), name='Puan-ver'),
   path('Puanlar/<int:pk>', api_views.PuanDetailAPIView.as_view(), name='Puanlar'),
]