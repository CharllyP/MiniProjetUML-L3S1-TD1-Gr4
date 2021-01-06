import pygame
import sys
import classFile

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

class Jeu :
    def __init__(self, name, type):
        self.ecran = pygame.display.set_mode((620, 480))
        pygame.display.set_caption('Quand on arrive en ville')
        self.jeuEnCours = True
        self.grille = Grille(self.ecran)
        self.hero = classFile.Heros(name, type)
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

        pygame.draw.rect(self.ecran, (50, 50, 50), (80, 40, 40, 120))  # grisée haut gauche 1
        pygame.draw.rect(self.ecran, (50, 50, 50), (40, 80, 120, 40))  # grisée haut gauche 2
        pygame.draw.rect(self.ecran, (50, 50, 50), (160, 280, 80, 80))  # grisée milieu
        pygame.draw.rect(self.ecran, (50, 50, 50), (40, 360, 80, 80))  # grisée bas carre
        pygame.draw.rect(self.ecran, (50, 50, 50), (280, 440, 80, 40))  # grisée bas
        pygame.draw.rect(self.ecran, (50, 50, 50), (400, 200, 40, 160))  # grisée droite
        pygame.draw.rect(self.ecran, (50, 50, 50), (280, 120, 40, 40))  # grisée droite petit

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

        pygame.draw.rect(self.ecran, (100, 155, 155), (440, 0, 180, 480))  # interface de droite
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
        if prev == (200,0,0,255):
            self.home.actionMaison(self.hero)
        if prev == (0,0,100,255):
            self.lib.actionBibliotheque(self.hero)
        if prev == (0,255,255,255):
            self.uni.actionUniversite(self.hero)
        if prev == (255,255,0,255):
            self.food.actionFastFood(self.hero)
        if prev == (100,0,100,255):
            self.bar.actionBar(self.hero)

    def perteDeplacement(self):
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
    def perteAction(self):
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

        while self.jeuEnCours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        perso = pygame.image.load("perso40x40u.png").convert_alpha()
                        if perso_y >= 40 and self.ecran.get_at((perso_x+5, perso_y-30)) != (50, 50, 50, 255) and (self.ecran.get_at((perso_x+5, perso_y-30)) != (0, 150, 150, 255) or self.hero.maillot):
                            self.prevCase(perso_x, perso_y)
                            perso_y -= 40
                            self.perteDeplacement()
                    if event.key == pygame.K_DOWN:
                        perso = pygame.image.load("perso40x40d.png").convert_alpha()
                        if perso_y <= 400 and self.ecran.get_at((perso_x+5, perso_y+70)) != (50, 50, 50, 255) and (self.ecran.get_at((perso_x+5, perso_y+70)) != (0, 150, 150, 255) or self.hero.maillot):
                            self.prevCase(perso_x, perso_y)
                            perso_y += 40
                            self.perteDeplacement()
                    if event.key == pygame.K_LEFT:
                        perso = pygame.image.load("perso40x40l.png").convert_alpha()
                        if perso_x >= 40 and self.ecran.get_at((perso_x-30, perso_y+5)) != (50, 50, 50, 255) and (self.ecran.get_at((perso_x-30, perso_y+5)) != (0, 150, 150, 255) or self.hero.maillot):
                            self.prevCase(perso_x, perso_y)
                            perso_x -= 40
                            self.perteDeplacement()
                    if event.key == pygame.K_RIGHT:
                        perso = pygame.image.load("perso40x40r.png").convert_alpha()
                        if perso_x <= 360 and self.ecran.get_at((perso_x+70, perso_y+5)) != (50, 50, 50, 255) and (self.ecran.get_at((perso_x+70, perso_y+5)) != (0, 150, 150, 255) or self.hero.maillot):
                            self.prevCase(perso_x, perso_y)
                            perso_x += 40
                            self.perteDeplacement()
                    if event.key == pygame.K_SPACE:
                        self.prevCase(perso_x,perso_y)
                        self.perteAction()
                    print("-----")
                    print("vie : ", self.hero.vie)
                    print("hydratation : ", self.hero.hydratation)
                    print("satiete : ", self.hero.satiete)
                    print("moral : ", self.hero.moral)
                    print("diplomes : ", self.hero.nbDiplome)

            self.mapCreation()
            self.ecran.blit(perso, (perso_x, perso_y))
            self.hero.position = classFile.Case(perso_x, perso_y)

            self.hero.mourir()
            if self.hero.mort:
                self.ecran.fill((10, 10, 10))
                endFont = pygame.font.SysFont("Arial", 24)
                end = endFont.render("Game Over", 1, (200, 200, 200))
                score = endFont.render("Score : "+str(self.hero.nbDiplome), 1, (200, 200, 200))
                self.ecran.blit(end, (250, 150))
                self.ecran.blit(score, (255, 250))

            pygame.display.flip()



if __name__ == '__main__':
    pygame.init()
    Jeu("charlly", "standard").mainFonction()       # exemple
    pygame.quit()
