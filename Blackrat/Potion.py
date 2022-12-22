class Pocoes():
    def __init__(self, pocao1 = ":/logorat/images/plus.png"):
        self.potion1 = pocao1
        self.potion2 = ":/logorat/images/plus.png"
        self.potion3 = ":/logorat/images/plus.png"
        self.potion4 = ":/logorat/images/plus.png"
        self.potion5 = ":/logorat/images/plus.png"

    def setPotion(self, posicao:int,valor:str):
        if(posicao == 1):
            self.potion1 = valor
        elif(posicao == 2):
            self.potion2 = valor
        elif(posicao == 3):
            self.potion3 = valor
        elif(posicao == 4):
            self.potion4 = valor
        elif(posicao == 5):
            self.potion5 = valor

    def getPotion(self, posicao:int):
        if(posicao == 1):
            return self.potion1
        elif(posicao == 2):
            return self.potion2
        elif(posicao == 3):
            return self.potion3
        elif(posicao == 4):
            return self.potion4
        elif(posicao == 5):
            return self.potion5
    



