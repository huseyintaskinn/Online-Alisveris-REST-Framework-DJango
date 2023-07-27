from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from kiyafetler.api.serializers import KiyafetSerializer
from kiyafetler.models import Kiyafet
import requests

@api_view(['GET'])
def home(request):
    # Model ile verileri alabilirdim ama API kullanarak verileri çektim
    # data = Kiyafet.objects.all()  
    url = 'http://127.0.0.1:8000/api/Kiyafetler/'
    response = requests.get(url)
 
    if response.status_code != 200:
        print('Hatalı istek yapıldı', response.status_code)
        return

    data = response.json()

    
    ortalamalar = []

    for kiyafet in data:
        adet = 0
        ort = 0
        toplam = 0
        for puan in kiyafet['Puanlar']:
            adet += 1 
            toplam += puan['degerlendirme']
        if adet != 0:  # Sıfıra bölme hatasını engellemek için kontrol ekleniyor
            ort = toplam / adet

        kiyafet['adet'] = adet
        kiyafet['ort'] = ort

    return render(request, 'index.html', {'data': data})