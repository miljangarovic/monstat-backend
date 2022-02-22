from django.db import models

# Create your models here.

class Grad(models.Model):
    naziv = models.CharField(max_length=255)

    # def __str__(self):
    #     return self.naziv

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
    grad_id = models.ForeignKey(Grad,on_delete=models.CASCADE,related_name='stanovnici')
    godina_id = models.ForeignKey(Godina,on_delete=models.CASCADE)
    pol_id = models.ForeignKey(Pol,on_delete=models.CASCADE)
    drzavljanstvo_id = models.ForeignKey(Drzavljanstvno,on_delete=models.CASCADE)
    vjeroispovijest_id = models.ForeignKey(Vjeroispovijest,on_delete=models.CASCADE)
    jezik_id = models.ForeignKey(MaternjiJezik,on_delete=models.CASCADE)
    nacionalnost_id = models.ForeignKey(Nacionalnost,on_delete=models.CASCADE)
    ekonomska_aktivnost_id = models.ForeignKey(EkonomskaAktivnost,on_delete=models.CASCADE)
    bracni_status_id = models.ForeignKey(BracniStatus,on_delete=models.CASCADE)
    racunarska_pismenost_id = models.ForeignKey(RacunarksaPismenost,on_delete=models.CASCADE)
    obrazovanje_id = models.ForeignKey(StepenObrazovanja,on_delete=models.CASCADE,related_name='obrazovanje')
    pismenost_id = models.ForeignKey(Pismenost,on_delete=models.CASCADE)
    strani_jezici = models.ManyToManyField(StraniJezik,related_name='strani_jezici')

    def __str__(self):
        return self.ime



