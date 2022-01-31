from django.db import models

# Create your models here.

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=50)
    sana = models.DateField()
    mavzu = models.CharField(max_length=30)
    muallif = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.sarlavha}'