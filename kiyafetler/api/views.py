from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from kiyafetler.api.permissions import IsAdminUserOrReadOnly, IsPuanSahibiOrReadOnly
from kiyafetler.api.pagination import SmallPagination, LargePagination


from kiyafetler.api.serializers import KiyafetSerializer, PuanSerializer
from kiyafetler.models import Kiyafet, Puan



class KiyafetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kiyafet.objects.all().order_by('id')
    serializer_class = KiyafetSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    # pagination_class = LargePagination




class KiyafetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kiyafet.objects.all()
    serializer_class = KiyafetSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class PuanCreateAPIView(generics.CreateAPIView):
    queryset = Puan.objects.all()
    serializer_class = PuanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
    def perform_create(self, serializer):
        Kiyafet_pk = self.kwargs.get('Kiyafet_pk')
        kiyafet = get_object_or_404(Kiyafet, pk=Kiyafet_pk)
        kullanici = self.request.user 
        Puanlar = Puan.objects.filter(Kiyafet=kiyafet, Puan_sahibi=kullanici)
        if Puanlar.exists():
            raise ValidationError('Bir ürüne sadece bir kes puan verebilirsiniz.')

        serializer.save(Kiyafet=kiyafet, Puan_sahibi=kullanici)


class PuanDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Puan.objects.all()
    serializer_class = PuanSerializer  
    permission_classes = [IsPuanSahibiOrReadOnly]


