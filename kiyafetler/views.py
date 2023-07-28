from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class KiyafetList(APIView):
    def get(self, request):
        url = 'http://127.0.0.1:8000/api/Kiyafetler/'
        response = requests.get(url)

        if response.status_code != 200:
            print('Hatalı istek yapıldı', response.status_code)
            return Response({"error": "Hatalı istek yapıldı"}, status=response.status_code)

        data = response.json()
        for kiyafet in data:
            adet = len(kiyafet['Puanlar'])
            toplam = sum(puan['degerlendirme'] for puan in kiyafet['Puanlar'])
            
            try:
                ort = toplam / adet
            except ZeroDivisionError:
                ort = 0  # veya istediğiniz bir değer

            kiyafet['adet'] = adet
            kiyafet['ort'] = ort
        
        return render(request, 'index.html', {'data': data})
