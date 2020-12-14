import random
import sys


class Case:
    ni = 0
    mi = 0
    type = ""

class Maison(Case):
    def __init__(self, ni, mi):
        self.ni = ni
        self.mi = mi
        self.type = "maison"

    def actionMaison(self, heros):
        heros.moral += 10
        heros.satiete += 10
        heros.hydratation += 10
        chanceSoin = random.randint(1, 100)
        chanceMaillot = random.randint(1, 100)

        if heros.moral > heros.moralMax:
            heros.moral = heros.moralMax
        if heros.satiete > heros.satieteMax:
            heros.satiete = heros.satieteMax
        if heros.hydratation > heros.hydratationMax:
            heros.hydratation = heros.hydratationMax
        if heros.vie > heros.vieMax:
            heros.vie = heros.vieMax
        if chanceMaillot > 95:
            heros.maillot = True
        if chanceSoin > 95:
            heros.vie += 10

        if heros.malade:
            heros.malade = False
            heros.moral -= 20
            heros.satiete -= 20
            heros.hydratation -= 20


class Bibliotheque(Case):
    def __init__(self, ni, mi):
        self.ni = ni
        self.mi = mi
        self.type = "bibliotheque"

    def actionBibliotheque(self, heros):
        heros.moral += 20
        chance = random.randint(1, 100)

        if heros.moral > heros.moralMax:
            heros.moral = heros.moralMax
        if chance > 95:
            heros.bonusDiplome += 10

class FastFood(Case):
    def __init__(self, ni, mi):
        self.ni = ni
        self.mi = mi
        self.type = "fastfood"

    def actionFastFood(self, heros):
        heros.moral += 10
        heros.satiete += 25
        heros.hydratation += 10
        heros.vie -= 5

        if heros.moral > heros.moralMax:
            heros.moral = heros.moralMax
        if heros.satiete > heros.satieteMax:
            heros.satiete = heros.satieteMax
        if heros.hydratation > heros.hydratationMax:
            heros.hydratation = heros.hydratationMax

class Universite(Case):
    def __init__(self, ni, mi):
        self.ni = ni
        self.mi = mi
        self.type = "universite"

    def actionUniversite(self, heros):
        chance = random.randint(1, 100) + heros.bonusDiplome

        if chance > 70:
            heros.nbDiplome += 1
            heros.moral += 5
            if heros.moral > heros.moralMax:
                heros.moral = heros.moralMax

class Bar(Case):
    def __init__(self, ni, mi):
        self.ni = ni
        self.mi = mi
        self.type = "bar"

    def actionBar(self, heros):
        heros.moral += 10
        heros.hydratation += 25
        heros.vie -= 5
        chanceDiplome = random.randint(1, 100)
        chanceMaillot = random.randint(1, 100)

        if chanceDiplome > 95:
            heros.bonusDiplome += 5
        if chanceMaillot > 95:
            heros.maillot = True
        if heros.moral > heros.moralMax:
            heros.moral = heros.moralMax
        if heros.hydratation > heros.hydratationMax:
            heros.hydratation = heros.hydratationMax

class Route(Case):
    def __init__(self, ni, mi):
        self.ni = ni
        self.mi = mi
        self.type = "route"

    def piegeRoute(self, heros):
        chancePiege = random.randint(1, 100)
        if chancePiege > 95:
            choixPiege = random.randint(1, 3)
            if choixPiege == 1:   # feu rouge
                heros.vie -= 1
            if choixPiege == 2:   # Police
                heros.moral -= 1
                heros.nbArrestation += 1
            if choixPiege == 3:   # Nid de poule
                heros.hydratation -= 2
                heros.satiete -= 2

class Trottoir(Case):
    def __init__(self, ni, mi):
        self.ni = ni
        self.mi = mi
        self.type = "trottoir"

    def piegeTrottoir(self, heros):
        chancePiege = random.randint(1, 100)
        if chancePiege > 95:
            choixPiege = random.randint(1,3)
            if choixPiege == 1:   # Peau de banane
                heros.vie -= 3
            if choixPiege == 2:   # Poussette
                heros.moral -= 2
            if choixPiege == 3:   # Caca de chien
                heros.satiete -= 1

class Eau(Case):
    def __init__(self, ni, mi):
        self.ni = ni
        self.mi = mi
        self.type = "eau"

class Foret(Case):
    def __init__(self, ni, mi):
        self.ni = ni
        self.mi = mi
        self.type = "foret"

class Grisee(Case):
    def __init__(self, ni, mi):
        self.ni = ni
        self.mi = mi
        self.type = "grisee"

class Heros:
    pseudo = ""
    nbDiplome = 0
    type = ""
    malade = False
    maillot = False
    vie = 100
    vieMax = 100
    hydratation = 100
    hydratationMax = 100
    satiete = 100
    satieteMax = 100
    moral = 100
    moralMax = 100
    bonusDiplome = 0
    nbArrestation = 0
    vehicule = ""
    position = Case()
    prevCase = Case()

    def __init__(self, name, type):
        self.pseudo = name
        self.type = type
        if type == "standard":
            self.vie = self.vieMax = 75
            self.hydratation = self.hydratationMax = 75
            self.satiete = self.satieteMax = 75
            self.moral = self.moralMax = 75
        if type == "hippie":
            self.vie = self.vieMax = 75
            self.hydratation = self.hydratationMax = 50
            self.satiete = self.satieteMax = 50
            self.moral = self.moralMax = 100
        if type == "hommePresse":
            self.vie = self.vieMax = 100
            self.hydratation = self.hydratationMax = 75
            self.satiete = self.satieteMax = 75
            self.moral = self.moralMax = 50

    def maladie(self):
        chance = random.randint(1, 100)

        if chance > 90:
            self.malade = True

    def mourir(self):
        if self.vie <= 0 or self.hydratation <= 0 or self.satiete <= 0 or self.moral <= 0 or self.nbArrestation >= 3:
            print("t mor mdr")                                                                                          #A FAIRE



class Etat:
    etatheros = Heros
    map = Case

    def __init__(self, heros, map):
        self.etatheros = heros
        self.map = map

    def sauvegarder(self, heros, map, numeroSave):
        fichierSave = open("save"+str(numeroSave)+".txt", "w")
        fichierSave.write(heros.pseudo+"\n")
        fichierSave.write(heros.nbDiplome+"\n")
        fichierSave.write(heros.type+"\n")
        fichierSave.write(heros.malade+"\n")
        fichierSave.write(heros.maillot+"\n")
        fichierSave.write(heros.vie+"\n")
        fichierSave.write(heros.vieMax+"\n")
        fichierSave.write(heros.hydratation+"\n")
        fichierSave.write(heros.hydratationMax+"\n")
        fichierSave.write(heros.satiete+"\n")
        fichierSave.write(heros.satieteMax+"\n")
        fichierSave.write(heros.moral+"\n")
        fichierSave.write(heros.moralMax+"\n")
        fichierSave.write(heros.bonusDiplome+"\n")
        fichierSave.write(heros.nbArrestation+"\n")
        fichierSave.write(heros.vehicule+"\n")
        fichierSave.write(heros.position.ni+"\n")
        fichierSave.write(heros.position.mi+"\n")
        fichierSave.write(heros.position.type+"\n")
        fichierSave.write(heros.prevCase.ni+"\n")
        fichierSave.write(heros.prevCase.mi+"\n")
        fichierSave.write(heros.prevCase.type+"\n")
        fichierSave.write(str(len(map))+","+str(len(map[0]))+"\n")
        for i in range(len(map)):
            for j in range(len(map[i])):
                fichierSave.write(map[i][j].ni+",")
                fichierSave.write(map[i][j].mi+",")
                fichierSave.write(map[i][j].type+"\n")

    def sauvegarderEtQuitter(self, heros, map, numeroSave):
        self.sauvegarder(heros, map, numeroSave)
        sys.exit(0)