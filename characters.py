from data import *
from images import Image

class Character:
    def __init__(self,name,weaknesses,image,player):
        super().__init__()
        self.points = 100
        self.max_points = 200
        self.name = name
        self.weaknesses = weaknesses
        self.player = player
        self.last_word = "not_defined"
        if self.player == 1 : 
            self.image = Image(image, 30, 180)
# _____________________________________________________JOEY CODE 15/05/2021
            self.end_sentence = False
            self.own_turn = 0
            self.my_awful_sentence = []
# ______________________________________________________
        if self.player == 2 : 
            self.image = Image(image, 740, 180)
# _____________________________________________________JOEY CODE 15/05/2021
            self.end_sentence = False
            self.own_turn = 0
            self.my_awful_sentence = []
# _________________________________________________________

    def update_scorebar(self, surface):
        #affichage du score du joueur durant le combat
        bar_color = (219, 72, 72)
        bar_position = [self.image.rect.x + 10, self.image.rect.y -20, self.points, 20]     
        pygame.draw.rect(surface, bar_color, bar_position)
    
    def calcul_scorebar(self): 
        #calcul des points
        if mot_choisi.weakness == "weakness" : 
            self.points += 5
        else : 
            self.points += 2
        #calcul du malus
        if mot_choisi.type == "malus" : 
            self.points -= 2