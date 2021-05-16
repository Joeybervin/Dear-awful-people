# AJOUT CODE JOEY
from data import *

class Mot :
    def __str__(self): 
        return str(self.text)

    def __init__(self,text,type,weakness): 
        self.type = type
        self.weakness = weakness
        self.text = text