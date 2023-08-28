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
    
def istraukti(self, product:str):
    if product in self.turinys:
        kiekis = float(input(f"Įveskite kiekį, kurį norite ištraukti (turimas kiekis: {self.turinys[product]}): "))
        if kiekis <= self.turinys[product]:
            self.turinys[product] -= kiekis
            print(f"{product} ištraukta {kiekis}, Dabartinis kiekis: {self.turinys[product]}")
            if self.turinys[product] == 0:
                del self.turinys[product]
        else:
            print('Nepakankamas kiekis šaldytuve.')
    else:
        print(f"Produktas {product} nerastas šaldytuve.")
    pass

def perziureti(self):
    pass

def ieskoti_produkta(self, product:str):
    pass

def svoris(self):
    pass

def receptas(self, product:str, quantity:float):
    pass
    