import datetime
import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monstat.settings')

import django

django.setup()

from faker import Faker

fake = Faker()

import datetime
from stanovnici import models

# Unos godine
models.Godina.objects.create(godina=datetime.date(2011, 1, 1))

# Unos gradova
models.Grad.objects.create(naziv='Andrijevica')
models.Grad.objects.create(naziv='Bar')
models.Grad.objects.create(naziv='Berane')
models.Grad.objects.create(naziv="Bijelo Polje")
models.Grad.objects.create(naziv='Budva')
models.Grad.objects.create(naziv='Cetinje')
models.Grad.objects.create(naziv='Danilovgrad')
models.Grad.objects.create(naziv="Herceg Novi")
models.Grad.objects.create(naziv='Kolasin')
models.Grad.objects.create(naziv='Kotor')
models.Grad.objects.create(naziv='Mojkovac')
models.Grad.objects.create(naziv='Niksic')
models.Grad.objects.create(naziv='Plav')
models.Grad.objects.create(naziv='Pljevlja')
models.Grad.objects.create(naziv='Pluzine')
models.Grad.objects.create(naziv='Podgorica')
models.Grad.objects.create(naziv='Rozaje')
models.Grad.objects.create(naziv='Savnik')
models.Grad.objects.create(naziv='Tivat')
models.Grad.objects.create(naziv='Ulcinj')
models.Grad.objects.create(naziv='Zabljak')

# unos polova
models.Pol.objects.create(naziv='Musko')
models.Pol.objects.create(naziv='Zensko')

# unos drzavljanstva
models.Drzavljanstvo.objects.create(naziv='crnogorsko')
models.Drzavljanstvo.objects.create(naziv='srpsko')
models.Drzavljanstvo.objects.create(naziv='hrvatsko')
models.Drzavljanstvo.objects.create(naziv='bosansko')
models.Drzavljanstvo.objects.create(naziv='albansko')
models.Drzavljanstvo.objects.create(naziv='makedonsko')
models.Drzavljanstvo.objects.create(naziv='ostalo')

# unos vjeroispovijesti
models.Vjeroispovijest.objects.create(naziv='Pravoslavna')
models.Vjeroispovijest.objects.create(naziv='Islamska')
models.Vjeroispovijest.objects.create(naziv='Katolicka')
models.Vjeroispovijest.objects.create(naziv='Hriscanska')
models.Vjeroispovijest.objects.create(naziv='Budizam')
models.Vjeroispovijest.objects.create(naziv='Ateista')
models.Vjeroispovijest.objects.create(naziv='Agnostik')
models.Vjeroispovijest.objects.create(naziv='Ostalo')
models.Vjeroispovijest.objects.create(naziv='Jehovini Svjedoci')
models.Vjeroispovijest.objects.create(naziv='Protestanti')
models.Vjeroispovijest.objects.create(naziv='Ne zeli da se izjasni')

# unos maternjih jezika

models.MaternjiJezik.objects.create(naziv='srpski')
models.MaternjiJezik.objects.create(naziv='crnogorski')
models.MaternjiJezik.objects.create(naziv='crnogorsko-srpski')
models.MaternjiJezik.objects.create(naziv='srpsko-crnogorski')
models.MaternjiJezik.objects.create(naziv='hrvatski')
models.MaternjiJezik.objects.create(naziv='bosanski')
models.MaternjiJezik.objects.create(naziv='bosnjacki')
models.MaternjiJezik.objects.create(naziv='albanski')
models.MaternjiJezik.objects.create(naziv='engleski')
models.MaternjiJezik.objects.create(naziv='srpsko-hrvatski')
models.MaternjiJezik.objects.create(naziv='makedonski')
models.MaternjiJezik.objects.create(naziv='madjarski')
models.MaternjiJezik.objects.create(naziv='maternji')
models.MaternjiJezik.objects.create(naziv='ne zeli da se izjasni')
models.MaternjiJezik.objects.create(naziv='njemacki')
models.MaternjiJezik.objects.create(naziv='ostalo')
models.MaternjiJezik.objects.create(naziv='ruski')
models.MaternjiJezik.objects.create(naziv='rumunski')
models.MaternjiJezik.objects.create(naziv='romski')
models.MaternjiJezik.objects.create(naziv='slovenacki')

# unos nacionalnosti

models.Nacionalnost.objects.create(naziv='Srbin')
models.Nacionalnost.objects.create(naziv='Crnogorac')
models.Nacionalnost.objects.create(naziv='Bosnjack')
models.Nacionalnost.objects.create(naziv='Albanac')
models.Nacionalnost.objects.create(naziv='Musliman')
models.Nacionalnost.objects.create(naziv='Hrvat')
models.Nacionalnost.objects.create(naziv='Bosanac')
models.Nacionalnost.objects.create(naziv='Bosnjak-Musliman')
models.Nacionalnost.objects.create(naziv='Crnogorac-Musliman')
models.Nacionalnost.objects.create(naziv='Crnogorac-Srbin')
models.Nacionalnost.objects.create(naziv='Srbin-Crnogorac')
models.Nacionalnost.objects.create(naziv='Egipcanin')
models.Nacionalnost.objects.create(naziv='Jugosloven')
models.Nacionalnost.objects.create(naziv='Italijan')
models.Nacionalnost.objects.create(naziv='Makedonac')
models.Nacionalnost.objects.create(naziv='Madjar')
models.Nacionalnost.objects.create(naziv='Rom')
models.Nacionalnost.objects.create(naziv='Rus')
models.Nacionalnost.objects.create(naziv='Njemac')
models.Nacionalnost.objects.create(naziv='Turcin')
models.Nacionalnost.objects.create(naziv='Ne zeli da se izjasni')
models.Nacionalnost.objects.create(naziv='Slovenac')

# unos ekonomske aktivnosti

models.EkonomskaAktivnost.objects.create(naziv='Neaktivan(<15 godina)')
models.EkonomskaAktivnost.objects.create(naziv='Zaposlen')
models.EkonomskaAktivnost.objects.create(naziv='Nezaposlen')
models.EkonomskaAktivnost.objects.create(naziv='Domacica')
models.EkonomskaAktivnost.objects.create(naziv='Student')
models.EkonomskaAktivnost.objects.create(naziv='Ucenik')
models.EkonomskaAktivnost.objects.create(naziv='Penzioner')
models.EkonomskaAktivnost.objects.create(naziv='Ostalo')

# unos bracnog statusa

models.BracniStatus.objects.create(naziv='Neudata/Neozenjen')
models.BracniStatus.objects.create(naziv='Udata/Ozenjen')
models.BracniStatus.objects.create(naziv='Razvedena/Razveden')
models.BracniStatus.objects.create(naziv='Udovica/Udovac')
models.BracniStatus.objects.create(naziv='Bez odgovora')

# unos racunarske pismenosti

models.RacunarksaPismenost.objects.create(naziv='Kompjuterski pismen')
models.RacunarksaPismenost.objects.create(naziv='Djelimicno poznavanje rada na racunaru')
models.RacunarksaPismenost.objects.create(naziv='Ne poznavanje rada na racunaru')
models.RacunarksaPismenost.objects.create(naziv='Bez odgovora')

# unos stepena obrazovanja

models.StepenObrazovanja.objects.create(naziv='Bez skole')
models.StepenObrazovanja.objects.create(naziv='Nepotpuna osnovna skola')
models.StepenObrazovanja.objects.create(naziv='Osnovna skola')
models.StepenObrazovanja.objects.create(naziv='Srednja skola')
models.StepenObrazovanja.objects.create(naziv='Visoka skola i prvi stepen fakulteta')
models.StepenObrazovanja.objects.create(naziv='Visoka skola, fakultet')
models.StepenObrazovanja.objects.create(naziv='Doktorat')
models.StepenObrazovanja.objects.create(naziv='Osnovne akademske studije')
models.StepenObrazovanja.objects.create(naziv='Osnovne akademske studije')
models.StepenObrazovanja.objects.create(naziv='Specijalsiticke studije')
models.StepenObrazovanja.objects.create(naziv='Magistarske studije')

# unos pismenosti

models.Pismenost.objects.create(naziv='Pismen')
models.Pismenost.objects.create(naziv='Nepismen')

# unos jezika

models.StraniJezik.objects.create(naziv='Engleski')
models.StraniJezik.objects.create(naziv='Ruski')
models.StraniJezik.objects.create(naziv='Italijanski')
models.StraniJezik.objects.create(naziv='Njemacki')
models.StraniJezik.objects.create(naziv='Francuski')
models.StraniJezik.objects.create(naziv='Spanski')
models.StraniJezik.objects.create(naziv='Portugalski')
models.StraniJezik.objects.create(naziv='Turski')
models.StraniJezik.objects.create(naziv='Arapski')
models.StraniJezik.objects.create(naziv='Kineski')
models.StraniJezik.objects.create(naziv='Ostalo')

# unos osoba

gradovi = list(models.Grad.objects.all())
polovi = list(models.Pol.objects.all())
godina = list(models.Godina.objects.all())
pismenost = list(models.Pismenost.objects.all())
drzavljanstva = list(models.Drzavljanstvo.objects.all())
vjeroispovijesti = list(models.Vjeroispovijest.objects.all())
m_jezici = list(models.MaternjiJezik.objects.all())
nacionalnosti = list(models.Nacionalnost.objects.all())
ek_aktivnosti = list(models.EkonomskaAktivnost.objects.all())
bracni_statusi = list(models.BracniStatus.objects.all())
racunarske_pismenosti = list(models.RacunarksaPismenost.objects.all())
obrazovanja = list(models.StepenObrazovanja.objects.all())
s_jezici = list(models.StraniJezik.objects.all())


def seed(N=10):
    for person in range(N):
        # create fake data
        fake_name = fake.first_name() + ' ' + fake.last_name()
        fake_city = random.choice(gradovi)
        fake_pol = random.choice(polovi)
        fake_godina = random.choice(godina)
        fake_drzavljanstvo = random.choice(drzavljanstva)
        fake_vjeroispovijest = random.choice(vjeroispovijesti)
        fake_m_jezik = random.choice(m_jezici)
        fake_nacionalnost = random.choice(nacionalnosti)
        fake_ek_aktivnost = random.choice(ek_aktivnosti)
        fake_brakcni_status = random.choice(bracni_statusi)
        fake_racunarksa_pismenost = random.choice(racunarske_pismenosti)
        fake_obrazovanje = random.choice(obrazovanja)
        fake_strani_jezici = random.choices(s_jezici, k=2)
        fake_pismenost = random.choice(pismenost)
        fake_godin_rodjenja = datetime.date(random.randint(1920, 2022), random.randint(1, 12), random.randint(1, 28))
        # Create new Stanovnik
        stanovnik = models.Stanovnik.objects.create(ime=fake_name, grad=fake_city, godina=fake_godina, pol=fake_pol,
                                                    drzavljanstvo=fake_drzavljanstvo, nacionalnost=fake_nacionalnost,
                                                    jezik=fake_m_jezik, vjeroispovijest=fake_vjeroispovijest,
                                                    ekonomska_aktivnost=fake_ek_aktivnost,
                                                    bracni_status=fake_brakcni_status,
                                                    racunarska_pismenost=fake_racunarksa_pismenost,
                                                    obrazovanje=fake_obrazovanje,
                                                    pismenost=fake_pismenost, godina_rodjenja=fake_godin_rodjenja, )
        stanovnik.strani_jezici.set(fake_strani_jezici)
        stanovnik.save()


if __name__ == '__main__':
    print('Seeding script!')
    seed(1000)
    print("Seeding completed!")
