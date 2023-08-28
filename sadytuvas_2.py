import json
try:
    with open("fridge.json", "r") as saldytuvas_dict:
        saldytuvas = json.load(saldytuvas_dict)
except:
    with open("fridge.json", "w") as saldytuvas_dict:
        saldytuvas = json.load(saldytuvas_dict)

class Saldytuvas:
    turinys = saldytuvas

    def prideti(self, product:str, quantity:float):
        self.turinys[product] = quantity

    def papildyti(self, product:str, quantity:float):
        pass
    
    def istraukti(self, product:str, quantity:float):
        pass

    def perziureti(self):
        pass

    def ieskoti_produkta(self, product:str):
        pass

    def svoris(self):
        pass

    def receptas(self, product:str, quantity:float):
        pass
    