from django.db import models

class Olahraga(models.Model):
    jenis = models.CharField(max_length=255)
    waktu = models.CharField(max_length=255)

    def __str__(self):
        return self.jenis        

class Latihan(models.Model):
    hari = models.CharField(max_length=255)
    total_waktu = models.CharField(max_length=255)
    olahraga = models.ManyToManyField(Olahraga)

    def __str__(self):
        return self.hari