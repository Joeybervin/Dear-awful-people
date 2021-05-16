
from data import *
from characters import Character
from mots import Mot
# _____________________________________________________JOEY CODE 15/05/2021
from math import floor
from random import randint
# __________________________________________________________________________

class Combat : 

    def __init__(self): 
        self.is_playing = False
        self.winner = False
        self.level_jardin = False
        self.level_salleamanger = False
        self.nb_parties = 0
# _____________________________________________________JOEY CODE 15/05/2021
        self.first_turn = 0
# ________________________________________________________________________


    def start(self,surface,menu,p1,p2):
        self.is_playing = True
        menu.buttons_sprites.add(p1.image)
        menu.buttons_sprites.add(p2.image)
        #menu.buttons_sprites.add(menu.button_fincombat)
        random.shuffle(list_mots)
        self.list_mots_affiches()
        #self.afficher_mots_affiches()

    def end(self,menu,p1,p2): 
        self.is_playing = False
        self.nb_parties += 1 
        p1.points = 0
        p2.points = 0
        mots_affiches.clear()
        menu.buttons_sprites.remove(p1.image)
        menu.buttons_sprites.remove(p2.image)
        if self.nb_parties > 0 :
            self.level_jardin = True
        if self.nb_parties > 1 :
            self.level_salleamanger = True

    def final_score(self, surface, menu, p1, p2):
        #afficher le score final
        #p2.points = 400 pour tester si joueur 2 gagne
        #p1.points = 400 pour tester si joueur 1 gagne
        #menu.buttons_sprites.remove(menu.button_fincombat)
        fond = pygame.Surface((700,400))
        fond.fill((42,111,120))
        surface.blit(fond, (193,110)) 
        font = pygame.font.Font("assets/Montserrat-Regular.ttf", 28)
        score_text = font.render(f"Score Joueur 1 : {p1.points} et Score Joueur 2 : {p2.points} ", 1, (255,255,255))
        surface.blit(score_text, (250,200))
        if p1.points > p2.points : 
            score_text2 = font.render(f" Congratulations Dear {p1.name}, vous êtes", 1, (255,255,255))
            surface.blit(score_text2, (260,300))
            score_text3 = font.render(f"le grand gagnant de cette joute verbale !", 1, (255,255,255))
            surface.blit(score_text3, (260,350))
        elif p2.points > p1.points : 
            score_text2 = font.render(f" Congratulations Dear {p2.name},", 1, (255,255,255))
            surface.blit(score_text2, (320,300))
            score_text3 = font.render(f"nul ne peut se mesurer à vous !", 1, (255,255,255))
            surface.blit(score_text3, (320,350))
        else : 
            score_text2 = font.render(f"On reconnaît un grand combat", 1, (255,255,255))
            surface.blit(score_text2, (260,300))
            score_text3 = font.render(f"à la pugnacité de ses adversaires.", 1, (255,255,255))
            surface.blit(score_text3, (260,350))
            score_text4 = font.render(f"Egalité pour vous deux my dear friends!", 1, (255,255,255))
            surface.blit(score_text4, (260,400))
        menu.buttons_sprites.add(menu.button_retourmenu)

    def list_mots_affiches(self): 
        i = 0
        while len(mots_affiches) < 6 : 
            if list_mots[i].type == "adjectif" : 
                mots_affiches.append(list_mots[i])
            i = i + 1
        i = 0
        while len(mots_affiches) < 12 : 
            if list_mots[i].type == "nom" : 
                mots_affiches.append(list_mots[i])
            i = i + 1
        i = 0
        while len(mots_affiches) < 17 : 
            if list_mots[i].type == "verbe" : 
                mots_affiches.append(list_mots[i])
            i = i + 1
        i = 0
        while len(mots_affiches) < 19 : 
            if list_mots[i].type == "expression" : 
                mots_affiches.append(list_mots[i])
            i = i + 1
        i = 0
        while len(mots_affiches) < 22 : 
            if list_mots[i].type == "autre" : 
                mots_affiches.append(list_mots[i])
            i = i + 1
    
    def afficher_mots_affiches(self): 
        x = 370
        y = 260
        i = 0 
        for n in mots_affiches : 
            font = pygame.font.Font("assets/Montserrat-Regular.ttf", 14)
            mot = font.render(f"{n.text}", 1, (0,0,0))
            displaysurface.blit(mot, (x,y))
            y = y + 35
            i = i + 1 
            if i == 11 : 
                x = 570
                y = 260

    def click_word(self, player,menu) :
        self.mouse = pygame.mouse.get_pos()

        i = 0
        x_min = 369
        x_max = 569
        y_min = 259
        y_max = 294
        # position à la souris pour le clic de la colonne 1 et suppression du mot choisi
        for n in mots_affiches :
            if x_min <= self.mouse[0] <= x_max and y_min <= self.mouse[1] <= y_max :
# _______________________________________________________________________________JOEY CODE 15/05/2021
                player.my_awful_sentence.append(mots_affiches[i].text)
# ___________________________________________________________________________________________________
                mots_affiches.remove(mots_affiches[i])
# _______________________________________________________________________________JOEY CODE 16/05/2021
                if len(mots_affiches) == 0:
                    self.winner = True
                    menu.invisibility_fight_object()
                # calcul du score
                elif mots_affiches[i -1].weakness in player.weaknesses :
# ___________________________________________________________________________________________________
                    player.points += 5
                else :
                    player.points += 2
            y_min += 35
            y_max += 35
            i = i + 1
            if i == 11 :
                x_min = 570
                x_max = 700
                y_min = 259
                y_max = 294

# _____________________________________________________JOEY CODE 16/05/2021
    def display_of_sentence(self, player,alpha, x_min_first_ligne,y_min_first_ligne,x_max_first_ligne,y_max_first_ligne):

        i = 0
        for n in player.my_awful_sentence:
            font = pygame.font.Font("assets/Montserrat-Regular.ttf", 14)
            awful = font.render(f"{n}", True, (0,0,0))
# _____________________________________________________JOEY CODE 16/05/2021 ++++
            awful.set_alpha((alpha))
# ______________________________________________________________________________
            awful_width = awful.get_width()
            displaysurface.blit(awful, (x_min_first_ligne,y_min_first_ligne))
            x_min_first_ligne = x_min_first_ligne + awful_width + 7
            i += 1
            if x_min_first_ligne + len(n) *8 > x_max_first_ligne :
                x_min_first_ligne = x_min_first_ligne - 580
                y_min_first_ligne = y_max_first_ligne


    def display_of_sentence_p1_playing(self, player,alpha, x_min_first_ligne,y_min_first_ligne,x_max_first_ligne,y_max_first_ligne,p2):
        self.display_of_sentence( player,alpha, x_min_first_ligne,y_min_first_ligne,x_max_first_ligne,y_max_first_ligne)
        self.display_of_sentence(p2,0, 150, 75, 852, 108)


    def display_of_sentence_p2_playing(self, player,alpha, x_min_first_ligne,y_min_first_ligne,x_max_first_ligne,y_max_first_ligne,p1):
        self.display_of_sentence(p1,0, 205, 75, 920, 108 )
        self.display_of_sentence(player,alpha, x_min_first_ligne,y_min_first_ligne,x_max_first_ligne,y_max_first_ligne)


    def both_end_sentence(self,p1,p2,menu):
        if p2.end_sentence == True and p1.end_sentence == True :
            menu.invisibility_fight_object()
            self.winner =True

    def add_word_to_my_sentence(self,player):
        if pygame.mouse.get_pressed()[0] :
            player.my_awful_sentence.append(self.click_word())

    def first_player_choice(self,p1,p2,menu):
        choice = floor(randint(1,2))
        self.first_turn += 1
        if choice == 1 :
            p2.own_turn += 1
            menu.visibility_object_fight_p1()
            if pygame.mouse.get_pressed() :
                self.click_word(p1,menu)
                #self.display_of_sentence(p1,150,75,852,118)
                p1.own_turn += 2
                print("P1 TOUR :",p1.own_turn)
                print("P2 TOUR :", p2.own_turn)
                print("P1 : ",p1.my_awful_sentence)
        else :
            p1.own_turn += 1
            menu.visibility_object_fight_p2()
            #self.display_of_sentence(p2, 150, 75, 852, 108)
            if pygame.mouse.get_pressed() :
                self.click_word(p2,menu)

                p2.own_turn += 2
                print("P1 TOUR :",p1.own_turn)
                print("P2 TOUR :", p2.own_turn)
                print("P2 : ", p2.my_awful_sentence)
    

