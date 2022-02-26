from django.db import models

# Create your models here.

class Grad(models.Model):
    naziv = models.CharField(max_length=255)

    def __str__(self):
        return self.naziv

class Godina(models.Model):
    godina = models.DateField()

    def __str__(self):
        return str(self.godina)

class Pol(models.Model):
    naziv = models.CharField(max_length=255)

    def __str__(self):
        return self.naziv

class Drzavljanstvno(models.Model):
    naziv = models.CharField(max_length=255)

    def __str__(self):
        return self.naziv

class Vjeroispovijest(models.Model):
    naziv = models.CharField(max_length=255)

    def __str__(self):
        return self.naziv

class MaternjiJezik(models.Model):
    naziv = models.CharField(max_length=255)

    def __str__(self):
        return self.naziv

class Nacionalnost(models.Model):
    naziv = models.CharField(max_length=255)

    def __str__(self):
        return self.naziv

class EkonomskaAktivnost(models.Model):
    naziv = models.CharField(max_length=255)

    def __str__(self):
        return self.naziv

class BracniStatus(models.Model):
    naziv = models.CharField(max_length=255)

    def __str__(self):
        return self.naziv

class RacunarksaPismenost(models.Model):
    naziv = models.CharField(max_length=255)

    def __str__(self):
        return self.naziv

class StepenObrazovanja(models.Model):
    naziv = models.CharField(max_length=255)

    def __str__(self):
        return self.naziv

class StraniJezik(models.Model):
    naziv = models.CharField(max_length=255)

    def __str__(self):
        return self.naziv

class Pismenost(models.Model):
    naziv = models.CharField(max_length=255)

    def __str__(self):
        return self.naziv

class Stanovnik(models.Model):
    ime = models.CharField(max_length=255)
    godina_rodjenja = models.DateField()
    grad = models.ForeignKey(Grad,on_delete=models.CASCADE,related_name='stanovnici')
    godina = models.ForeignKey(Godina,on_delete=models.CASCADE)
    pol = models.ForeignKey(Pol,on_delete=models.CASCADE)
    drzavljanstvo = models.ForeignKey(Drzavljanstvno,on_delete=models.CASCADE)
    vjeroispovijest = models.ForeignKey(Vjeroispovijest,on_delete=models.CASCADE)
    jezik = models.ForeignKey(MaternjiJezik,on_delete=models.CASCADE)
    nacionalnost = models.ForeignKey(Nacionalnost,on_delete=models.CASCADE)
    ekonomska_aktivnost = models.ForeignKey(EkonomskaAktivnost,on_delete=models.CASCADE)
    bracni_status = models.ForeignKey(BracniStatus,on_delete=models.CASCADE)
    racunarska_pismenost = models.ForeignKey(RacunarksaPismenost,on_delete=models.CASCADE)
    obrazovanje = models.ForeignKey(StepenObrazovanja,on_delete=models.CASCADE,related_name='obrazovanje')
    pismenost = models.ForeignKey(Pismenost,on_delete=models.CASCADE)
    strani_jezici = models.ManyToManyField(StraniJezik,related_name='strani_jezici')

    def __str__(self):
        return self.ime



