import pygame
import sys
import classFile
import random
import time

class Grille:
    def __init__(self, ecran):
        self.ecran = ecran
        self.lignes = [((40, 0), (40, 600)), ((80, 0), (80, 600)), ((120, 0), (120, 600)), ((160, 0), (160, 600)),
                       ((200, 0), (200, 600)), ((240, 0), (240, 600)), ((280, 0), (280, 600)), ((320, 0), (320, 600)),
                       ((360, 0), (360, 600)), ((400, 0), (400, 600)), ((440, 0), (440, 600)),
                       ((0, 40), (440, 40)), ((0, 80), (440, 80)), ((0, 120), (440, 120)), ((0, 160), (440, 160)),
                       ((0, 200), (440, 200)), ((0, 240), (440, 240)), ((0, 280), (440, 280)), ((0, 320), (440, 320)),
                       ((0, 360), (440, 360)), ((0, 400), (440, 400)), ((0, 440), (440, 440))]

    def afficher(self):
        for ligne in self.lignes :
            pygame.draw.line(self.ecran, (25, 25, 25), ligne[0], ligne[1], 1)


class Menu:
    def __init__(self):
        self.ecran = pygame.display.set_mode((630, 480))
        self.menuPersoEnCours = True
        self.menuVehiculeEnCours = True
        pygame.display.set_caption('Quand on arrive en ville - menu')
        self.ecran.fill((200, 100, 150))
        self.type = ""
        self. vehicule = ""


    def mainFonction(self):
        fontMenu = pygame.font.SysFont("Arial", 20)
        fontTitre = pygame.font.SysFont("Arial", 32)
        while self.menuPersoEnCours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.type = "standard"
                        self.menuPersoEnCours = False
                    if event.key == pygame.K_2:
                        self.type = "hippie"
                        self.vehicule = "velo"
                        self.menuPersoEnCours = False
                        self.menuVehiculeEnCours = False
                    if event.key == pygame.K_3:
                        self.type = "hommePresse"
                        self.menuPersoEnCours = False

            self.ecran.fill((200, 100, 150))
            labelMenuPerso = fontTitre.render("Choisissez votre type : ", 1, (0, 0, 0))
            labelStandard = fontMenu.render("1. Standard", 1, (0, 0, 0))
            labelHippie = fontMenu.render("2. Hippie", 1, (0, 0, 0))
            labelHommePresse = fontMenu.render("3. Homme Presse", 1, (0, 0, 0))
            self.ecran.blit(labelMenuPerso, (125, 100))
            self.ecran.blit(labelStandard, (250, 200))
            self.ecran.blit(labelHippie, (250, 250))
            self.ecran.blit(labelHommePresse, (250, 300))

            pygame.display.flip()

        while self.menuVehiculeEnCours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.vehicule = "velo"
                        self.menuVehiculeEnCours = False
                    if event.key == pygame.K_2:
                        self.vehicule = "voiture"
                        self.menuVehiculeEnCours = False

            self.ecran.fill((200, 100, 150))
            labelMenuVehicule = fontTitre.render("Choisissez votre vehicule : ", 1, (0, 0, 0))
            labelVelo = fontMenu.render("1. Velo", 1, (0, 0, 0))
            labelVoiture = fontMenu.render("2. Voiture", 1, (0, 0, 0))
            self.ecran.blit(labelMenuVehicule, (125, 100))
            self.ecran.blit(labelVelo, (250, 200))
            self.ecran.blit(labelVoiture, (250, 300))

            pygame.display.flip()

        return self.type, self.vehicule


class Jeu:
    def __init__(self, type, vehicule):
        self.ecran = pygame.display.set_mode((630, 480))
        pygame.display.set_caption('Quand on arrive en ville - jeu')
        self.jeuEnCours = True
        self.grille = Grille(self.ecran)
        self.hero = classFile.Heros(type, vehicule)
        self.home = classFile.Maison(240, 240)
        self.lib = classFile.Bibliotheque(320, 80)
        self.uni = classFile.Universite(120, 400)
        self.food = classFile.FastFood(160, 160)
        self.bar = classFile.Bar(320, 360)


    def mapCreation(self):
        self.ecran.fill((50, 150, 50))  # foret

        pygame.draw.rect(self.ecran, (0, 150, 150), (0, 0, 360, 40))  # eau du haut
        pygame.draw.rect(self.ecran, (0, 150, 150), (360, 0, 40, 400))  # eau de droite
        pygame.draw.rect(self.ecran, (0, 150, 150), (0, 0, 80, 240))  # eau de gauche 1
        pygame.draw.rect(self.ecran, (0, 150, 150), (40, 200, 80, 80))  # eau de gauche 2
        pygame.draw.rect(self.ecran, (0, 150, 150), (80, 240, 80, 160))  # eau de gauche 3

        pygame.draw.rect(self.ecran, (50, 50, 50), (80, 40, 40, 120))  # grisee haut gauche 1
        pygame.draw.rect(self.ecran, (50, 50, 50), (40, 80, 120, 40))  # grisee haut gauche 2
        pygame.draw.rect(self.ecran, (50, 50, 50), (160, 280, 80, 80))  # grisee milieu
        pygame.draw.rect(self.ecran, (50, 50, 50), (40, 360, 80, 80))  # grisee bas carre
        pygame.draw.rect(self.ecran, (50, 50, 50), (280, 440, 80, 40))  # grisee bas
        pygame.draw.rect(self.ecran, (50, 50, 50), (400, 200, 40, 160))  # grisee droite
        pygame.draw.rect(self.ecran, (50, 50, 50), (280, 120, 40, 40))  # grisee droite petit

        pygame.draw.rect(self.ecran, (150, 150, 150), (320, 120, 40, 120))  # trottoir droite
        pygame.draw.rect(self.ecran, (150, 150, 150), (160, 200, 40, 80))  # trottoir gauche
        pygame.draw.rect(self.ecran, (150, 150, 150), (200, 240, 40, 40))  # trottoir gauche suite
        pygame.draw.rect(self.ecran, (150, 150, 150), (240, 280, 40, 160))  # trottoir milieu
        pygame.draw.rect(self.ecran, (150, 150, 150), (160, 400, 80, 40))  # trottoir bas
        pygame.draw.rect(self.ecran, (150, 150, 150), (280, 360, 40, 40))  # trottoir bas droite

        pygame.draw.rect(self.ecran, (0, 0, 0), (240, 80, 80, 40))
        pygame.draw.rect(self.ecran, (0, 0, 0), (240, 120, 40, 120))
        pygame.draw.rect(self.ecran, (0, 0, 0), (200, 160, 40, 40))
        pygame.draw.rect(self.ecran, (0, 0, 0), (280, 240, 80, 40))
        pygame.draw.rect(self.ecran, (0, 0, 0), (320, 280, 40, 80))

        myFont = pygame.font.SysFont("Arial", 12)
        labelVie = myFont.render("vie", 1, (0, 0, 0))
        labelHydr = myFont.render("Hydratation", 1, (0, 0, 0))
        labelSati = myFont.render("Satiete", 1, (0, 0, 0))
        labelMora = myFont.render("Moral", 1, (0, 0, 0))
        labelNbDiplomes = myFont.render("Diplomes", 1, (0, 0, 0))
        nbDiplomes = myFont.render(str(self.hero.nbDiplome), 1, (0, 0, 0))
        labelNbArrestations = myFont.render("Arrestations", 1, (0, 0, 0))
        nbArrestations = myFont.render(str(self.hero.nbArrestation), 1, (0, 0, 0))

        pygame.draw.rect(self.ecran, (100, 155, 155), (440, 0, 190, 480))  # interface de droite
        pygame.draw.rect(self.ecran, (50, 50, 50), (450, 20, self.hero.vieMax, 10))
        pygame.draw.rect(self.ecran, (200, 0, 0), (450, 20, self.hero.vie, 10))
        self.ecran.blit(labelVie, (555, 20))
        pygame.draw.rect(self.ecran, (50, 50, 50), (450, 40, self.hero.hydratationMax, 10))
        pygame.draw.rect(self.ecran, (50, 50, 200), (450, 40, self.hero.hydratation, 10))
        self.ecran.blit(labelHydr, (555, 40))
        pygame.draw.rect(self.ecran, (50, 50, 50), (450, 60, self.hero.satieteMax, 10))
        pygame.draw.rect(self.ecran, (100, 100, 0), (450, 60, self.hero.satiete, 10))
        self.ecran.blit(labelSati, (555, 60))
        pygame.draw.rect(self.ecran, (50, 50, 50), (450, 80, self.hero.moralMax, 10))
        pygame.draw.rect(self.ecran, (255, 255, 255), (450, 80, self.hero.moral, 10))
        self.ecran.blit(labelMora, (555, 80))
        self.ecran.blit(labelNbDiplomes, (555, 100))
        self.ecran.blit(nbDiplomes, (480, 100))
        self.ecran.blit(labelNbArrestations, (555, 120))
        self.ecran.blit(nbArrestations, (480, 120))

        pygame.draw.rect(self.ecran, (200, 0, 0), (240, 240, 40, 40))   # maison
        self.ecran.blit(pygame.image.load("home.png").convert_alpha(), (240,240))
        pygame.draw.rect(self.ecran, (0, 0, 100), (320, 80, 40, 40))    # bibliotheque
        self.ecran.blit(pygame.image.load("lib.png").convert_alpha(), (320, 80))
        pygame.draw.rect(self.ecran, (0, 255, 255), (120, 400, 40, 40))  # universite
        self.ecran.blit(pygame.image.load("uni.png").convert_alpha(), (120, 400))
        pygame.draw.rect(self.ecran, (255, 255, 0), (160, 160, 40, 40))  # Fast-Food
        self.ecran.blit(pygame.image.load("food.png").convert_alpha(), (160, 160))
        pygame.draw.rect(self.ecran, (100, 0, 100), (320, 360, 40, 40))  # bar
        self.ecran.blit(pygame.image.load("bar.png").convert_alpha(), (320, 360))

        self.grille.afficher()


    def prevCase(self, x, y):
        prev = self.ecran.get_at((x+2, y+2))
        chanceMaladie = random.randint(1, 100)
        if chanceMaladie > 95:
            self.hero.vie -= 10
            return "Vous etes tombe malade"
        if prev == (200,0,0,255):
            return self.home.actionMaison(self.hero)
        if prev == (0,0,100,255):
            return self.lib.actionBibliotheque(self.hero)
        if prev == (0,255,255,255):
            return self.uni.actionUniversite(self.hero)
        if prev == (255,255,0,255):
            self.food.actionFastFood(self.hero)
        if prev == (100,0,100,255):
            return self.bar.actionBar(self.hero)
        if prev == (150, 150, 150, 255):
            trottoir = classFile.Trottoir(x, y)
            return trottoir.piegeTrottoir(self.hero)
        if prev == (0, 0, 0, 255):
            route = classFile.Route(x, y)
            return route.piegeRoute(self.hero)
        else:
            return "RIEN"


    def perteDeplacement(self, x, y, n, m):
        if self.hero.type=="standard":
            self.hero.vie -= 1
            self.hero.moral -= 1
            self.hero.satiete -= 1
            self.hero.hydratation -= 1
        if self.hero.type=="hippie":
            self.hero.vie -= 2
            self.hero.satiete -= 2
            self.hero.hydratation -= 2
        if self.hero.type=="hommePresse":
            self.hero.moral -= 2
        if self.ecran.get_at((x, y)) == (150, 150, 150, 255):
            if self.ecran.get_at((n, m)) != (150, 150, 150, 255):
                self.hero.hydratation -= 10
                self.hero.satiete -= 10
        if self.ecran.get_at((x, y)) == (0, 0, 0, 255):
            if self.ecran.get_at((n, m)) != (0, 0, 0, 255):
                if self.hero.vehicule == "velo":
                    self.hero.hydratation -= 5
                    self.hero.satiete -= 5
                if self.hero.vehicule == "voiture":
                    self.hero.moral -= 2


    def perteAction(self, x, y):
        prev = self.ecran.get_at((x + 2, y + 2))
        if prev == (200, 0, 0, 255) or prev == (0,0,100,255) or prev == (0,255,255,255) or prev == (255,255,0,255) or prev == (100,0,100,255):
            if self.hero.type=="standard":
                self.hero.vie -= 1
                self.hero.moral -= 1
                self.hero.satiete -= 1
                self.hero.hydratation -= 1
            if self.hero.type=="hippie":
                self.hero.vie -= 0.5
                self.hero.satiete -= 0.5
                self.hero.hydratation -= 0.5
            if self.hero.type=="hommePresse":
                self.hero.vie -= 1
                self.hero.moral -= 1
                self.hero.satiete -= 1
                self.hero.hydratation -= 1


    def mainFonction(self):
        perso = pygame.image.load("perso40x40u.png").convert_alpha()
        perso_x = 240
        perso_y = 240
        lastEvent = "RIEN"
        copyEvent = "RIEN"
        eventFont = pygame.font.SysFont("Arial", 14)
        labelEvent = eventFont.render("", 1, (0, 0, 0))

        while self.jeuEnCours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        perso = pygame.image.load("perso40x40u.png").convert_alpha()
                        if perso_y >= 40 and self.ecran.get_at((perso_x+5, perso_y-30)) != (50, 50, 50, 255) and (self.ecran.get_at((perso_x+5, perso_y-30)) != (0, 150, 150, 255) or self.hero.maillot):
                            lastEvent = self.prevCase(perso_x, perso_y)
                            if lastEvent != "RIEN":
                                copyEvent = lastEvent
                            perso_y -= 40
                            self.perteDeplacement(perso_x+3, perso_y+50, perso_x+3, perso_y+3)
                    if event.key == pygame.K_DOWN:
                        perso = pygame.image.load("perso40x40d.png").convert_alpha()
                        if perso_y <= 400 and self.ecran.get_at((perso_x+5, perso_y+70)) != (50, 50, 50, 255) and (self.ecran.get_at((perso_x+5, perso_y+70)) != (0, 150, 150, 255) or self.hero.maillot):
                            lastEvent = self.prevCase(perso_x, perso_y)
                            if lastEvent != "RIEN":
                                copyEvent = lastEvent
                            perso_y += 40
                            self.perteDeplacement(perso_x+3, perso_y-10, perso_x+3, perso_y+3)
                    if event.key == pygame.K_LEFT:
                        perso = pygame.image.load("perso40x40l.png").convert_alpha()
                        if perso_x >= 40 and self.ecran.get_at((perso_x-30, perso_y+5)) != (50, 50, 50, 255) and (self.ecran.get_at((perso_x-30, perso_y+5)) != (0, 150, 150, 255) or self.hero.maillot):
                            lastEvent = self.prevCase(perso_x, perso_y)
                            if lastEvent != "RIEN":
                                copyEvent = lastEvent
                            perso_x -= 40
                            self.perteDeplacement(perso_x+50, perso_y+3, perso_x+3, perso_y+3)
                    if event.key == pygame.K_RIGHT:
                        perso = pygame.image.load("perso40x40r.png").convert_alpha()
                        if perso_x <= 360 and self.ecran.get_at((perso_x+70, perso_y+5)) != (50, 50, 50, 255) and (self.ecran.get_at((perso_x+70, perso_y+5)) != (0, 150, 150, 255) or self.hero.maillot):
                            lastEvent = self.prevCase(perso_x, perso_y)
                            if lastEvent != "RIEN":
                                copyEvent = lastEvent
                            perso_x += 40
                            self.perteDeplacement(perso_x-10, perso_y+3, perso_x+3, perso_y+3)
                    if event.key == pygame.K_SPACE:
                        lastEvent = self.prevCase(perso_x,perso_y)
                        if lastEvent != "RIEN":
                            copyEvent = lastEvent
                        self.perteAction(perso_x, perso_y)

            self.mapCreation()
            self.ecran.blit(perso, (perso_x, perso_y))
            self.hero.position = classFile.Case(perso_x, perso_y)

            if lastEvent != "RIEN":
                labelEvent = eventFont.render(str(lastEvent), 1, (0, 0, 0))
            self.ecran.blit(labelEvent, (450, 400))

            self.hero.mourir()
            if self.hero.mort:
                self.ecran.fill((10, 10, 10))
                endFont = pygame.font.SysFont("Arial", 24)
                end = endFont.render("Game Over", 1, (200, 200, 200))
                score = endFont.render("Score : "+str(self.hero.nbDiplome), 1, (200, 200, 200))
                finalEvent = endFont.render("Dernier evenement : "+str(copyEvent), 1, (100, 100, 100))
                self.ecran.blit(end, (250, 150))
                self.ecran.blit(score, (255, 250))
                self.ecran.blit(finalEvent, (25, 400))
                pygame.display.flip()
                time.sleep(2.5)
                self.jeuEnCours = False

            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()

    application = True
    while application:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            list = Menu().mainFonction()
            Jeu(list[0], list[1]).mainFonction()

    pygame.quit()
