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
    def __init__(self):
        self.ecran = pygame.display.set_mode((600, 480))
        pygame.display.set_caption('Quand on arrive en ville')
        self.jeuEnCours = True
        self.grille = Grille(self.ecran)

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
                        if perso_y >= 40 and self.ecran.get_at((perso_x+5, perso_y-30)) != (50, 50, 50, 255):
                            perso_y -= 40

                    if event.key == pygame.K_DOWN:
                        perso = pygame.image.load("perso40x40d.png").convert_alpha()
                        if perso_y <= 400 and self.ecran.get_at((perso_x+5, perso_y+70)) != (50, 50, 50, 255):
                            perso_y += 40
                    if event.key == pygame.K_LEFT:
                        perso = pygame.image.load("perso40x40l.png").convert_alpha()
                        if perso_x >= 40 and self.ecran.get_at((perso_x-30, perso_y+5)) != (50, 50, 50, 255):
                            perso_x -= 40
                    if event.key == pygame.K_RIGHT:
                        perso = pygame.image.load("perso40x40r.png").convert_alpha()
                        if perso_x <= 360 and self.ecran.get_at((perso_x+70, perso_y+5)) != (50, 50, 50, 255):
                            perso_x += 40

            self.ecran.fill((50,150,50))                                            # foret

            pygame.draw.rect(self.ecran, (0, 150, 150), (0, 0, 360, 40))            # eau du haut
            pygame.draw.rect(self.ecran, (0, 150, 150), (360, 0, 40, 400))          # eau de droite
            pygame.draw.rect(self.ecran, (0, 150, 150), (0, 0, 80, 240))            # eau de gauche 1
            pygame.draw.rect(self.ecran, (0, 150, 150), (40, 200, 80, 80))          # eau de gauche 2
            pygame.draw.rect(self.ecran, (0, 150, 150), (80, 240, 80, 160))         # eau de gauche 3

            pygame.draw.rect(self.ecran, (50, 50, 50), (80, 40, 40, 120))           # grisée haut gauche 1
            pygame.draw.rect(self.ecran, (50, 50, 50), (40, 80, 120, 40))           # grisée haut gauche 2
            pygame.draw.rect(self.ecran, (50, 50, 50), (160, 280, 80, 80))          # grisée milieu
            pygame.draw.rect(self.ecran, (50, 50, 50), (40, 360, 80, 80))           # grisée bas carre
            pygame.draw.rect(self.ecran, (50, 50, 50), (280, 440, 80, 40))          # grisée bas
            pygame.draw.rect(self.ecran, (50, 50, 50), (400, 200, 40, 160))         # grisée droite
            pygame.draw.rect(self.ecran, (50, 50, 50), (280, 120, 40, 40))          # grisée droite petit

            pygame.draw.rect(self.ecran, (150, 150, 150), (320, 120, 40, 120))      # trottoir droite
            pygame.draw.rect(self.ecran, (150, 150, 150), (160, 200, 40, 80))       # trottoir gauche
            pygame.draw.rect(self.ecran, (150, 150, 150), (200, 240, 40, 40))       # trottoir gauche suite
            pygame.draw.rect(self.ecran, (150, 150, 150), (240, 280, 40, 160))      # trottoir milieu
            pygame.draw.rect(self.ecran, (150, 150, 150), (160, 400, 80, 40))       # trottoir bas
            pygame.draw.rect(self.ecran, (150, 150, 150), (280, 360, 40, 40))       # trottoir bas droite

            pygame.draw.rect(self.ecran, (0, 0, 0), (240, 80, 80, 40))
            pygame.draw.rect(self.ecran, (0, 0, 0), (240, 120, 40, 120))
            pygame.draw.rect(self.ecran, (0, 0, 0), (200, 160, 40, 40))
            pygame.draw.rect(self.ecran, (0, 0, 0), (280, 240, 80, 40))
            pygame.draw.rect(self.ecran, (0, 0, 0), (320, 280, 40, 80))

            pygame.draw.rect(self.ecran, (220, 220, 220), (440, 0, 160, 480))       # interface de droite

            pygame.draw.rect(self.ecran, (200, 0, 0), (240, 240, 40, 40))           # maison
            pygame.draw.rect(self.ecran, (0, 0, 100), (320, 80, 40, 40))            # bibliotheque
            pygame.draw.rect(self.ecran, (0, 255, 255), (120, 400, 40, 40))         # universite
            pygame.draw.rect(self.ecran, (255, 255, 0), (160, 160, 40, 40))         # Fast-Food
            pygame.draw.rect(self.ecran, (100, 0, 100), (320, 360, 40, 40))         # bar

            self.grille.afficher()

            self.ecran.blit(perso, (perso_x, perso_y))

            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    Jeu().mainFonction()
    pygame.quit()
