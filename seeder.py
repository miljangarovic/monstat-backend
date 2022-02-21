import datetime
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monstat.settings')

import django

django.setup()

import datetime
from stanovnici import models


# Unos godine
models.Godina.objects.create(godina=datetime.date(2011,1,1))

# Unos gradova
models.Grad.objects.create(naziv='Andrijevica')
models.Grad.objects.create(naziv='Bar')
models.Grad.objects.create(naziv='Berane')
models.Grad.objects.create(naziv='Bijelo Polje')
models.Grad.objects.create(naziv='Budva')
models.Grad.objects.create(naziv='Cetinje')
models.Grad.objects.create(naziv='Danilovgrad')
models.Grad.objects.create(naziv='Herceg Novi')
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
models.Drzavljanstvno.objects.create(naziv='crnogorsko')
models.Drzavljanstvno.objects.create(naziv='srpsko')
models.Drzavljanstvno.objects.create(naziv='hrvatsko')
models.Drzavljanstvno.objects.create(naziv='bosansko')
models.Drzavljanstvno.objects.create(naziv='albansko')
models.Drzavljanstvno.objects.create(naziv='makedonsko')
models.Drzavljanstvno.objects.create(naziv='ostalo')

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

models.Nacionalnost.objects.create(naziv='Srbi')
models.Nacionalnost.objects.create(naziv='Crnogorci')
models.Nacionalnost.objects.create(naziv='Bosnjaci')
models.Nacionalnost.objects.create(naziv='Albanci')
models.Nacionalnost.objects.create(naziv='Muslimani')
models.Nacionalnost.objects.create(naziv='Hrvati')
models.Nacionalnost.objects.create(naziv='Bosanci')
models.Nacionalnost.objects.create(naziv='Bosnjaci-Muslimani')
models.Nacionalnost.objects.create(naziv='Crnogorci-Muslimani')
models.Nacionalnost.objects.create(naziv='Crnogorci-Srbi')
models.Nacionalnost.objects.create(naziv='Srbi-Crnogorci')
models.Nacionalnost.objects.create(naziv='Egipcani')
models.Nacionalnost.objects.create(naziv='Jugosloveni')
models.Nacionalnost.objects.create(naziv='Italijani')
models.Nacionalnost.objects.create(naziv='Makedonci')
models.Nacionalnost.objects.create(naziv='Madjari')
models.Nacionalnost.objects.create(naziv='Romi')
models.Nacionalnost.objects.create(naziv='Rusi')
models.Nacionalnost.objects.create(naziv='Njemci')
models.Nacionalnost.objects.create(naziv='Turci')
models.Nacionalnost.objects.create(naziv='Ne zeli da se izjasni')
models.Nacionalnost.objects.create(naziv='Slovenci')

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








