from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Kiyafet(models.Model):
    isim = models.CharField(max_length=255)
    satici = models.CharField(max_length=255)
    aciklama = models.TextField(blank=True, null=True)
    fiyat = models.IntegerField(default=0)
    imgUrl = models.URLField(default='https://cdn.dsmcdn.com/ty965/product/media/images/20230712/14/393134474/934329462/2/2_org.jpg')

    def __str__(self):
        return f'{self.isim}'

class Puan(models.Model):
    Kiyafet = models.ForeignKey(Kiyafet, on_delete=models.CASCADE, related_name='Puanlar')
    degerlendirme = models.PositiveIntegerField(
        validators = [MinValueValidator(1), MaxValueValidator(5)],
    )
    Puan_sahibi = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Puan_sahibi', default=-1)

    def __str__(self):
        return self.degerlendirme