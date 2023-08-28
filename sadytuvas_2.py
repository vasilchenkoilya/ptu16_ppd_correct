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

    def papildyti(self) -> str | float :
        """Funkcija isves menu, kur bus parodyta lentele 
        su visais maisto produktais ir jiems priskirti 
        eiles numeriai
        """
        indeksas = 0

        print("Saldytuve yra tokie produktai: ", "\n")
        print(f"{'Nr.':3s} | {'Maisto produktas':15s} | {'Produkto kiekis':10s}", end="\n")
        for produktas in self:
            print(f"{indeksas+1:>3d} | {produktas:<16s} | {self[produktas]}")
            indeksas += 1

        pasirinktas_indeksas = int(input("Parasykite norimo produkto numeri: ")) -1
        prideti = int(input("Parasykite kiek norite prideti produkto: "))

        pasirinktas_produktas = self[pasirinktas_indeksas]
        self[pasirinktas_produktas] += prideti

        return self
    
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
    