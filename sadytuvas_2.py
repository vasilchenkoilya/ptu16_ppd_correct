import json

try:
    with open("fridge.json", "r+") as saldytuvas_dict:
        saldytuvas = json.load(saldytuvas_dict)
except:
    saldytuvas = {}
    with open("fridge.json", "w") as saldytuvas_dict:
        json.dump(saldytuvas, saldytuvas_dict)

class Saldytuvas:
    turinys = saldytuvas
    meniu = """
 1 - pridėti naują produktą 
 2 - papildyti produkto kiekį
 3 - ištraukti produktą nurodant kiekį
 4 - peržiūrėti produktus
 5 - ieškoti produktų
 6 - Suzinoti saldytuvo svori
 7 - Recepto patikrinimas (ar pakanka reikalingu produktu saldytuve) 
 0 - išėjimas
         """

<<<<<<< HEAD
def prideti(self, product:str, quantity:float):
    self.turinys[product] = quantity
=======
    def meniu_pasirinkimas():
        print(Saldytuvas.meniu)

    def prideti(self, produktas, kiekis):
        self.turinys[produktas] = kiekis
>>>>>>> e11167f0a919826cfb39f931f4668a2c9551fbb4

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

<<<<<<< HEAD
def receptas(self, product:str, quantity:float):
    pass
    
=======
    def receptas(self, product:str, quantity:float):
        pass

    def ijungti(self):
        
        Saldytuvas.meniu_pasirinkimas()
        while True:  
            pasirinkimas = input("Pasirinkite veiksma: ")
            if pasirinkimas == "0":
                with open("fridge.json", "w") as saldytuvas_json:
                    saldytuvas_json = json.dump(Saldytuvas.turinys, saldytuvas_json, indent=2)
                break
            elif pasirinkimas == "1":
                Saldytuvas.prideti(
                    produktas=input('Iveskite produkto pavadinima'), kiekis=float(input('Iveskite kieki'))
                    )
#             elif pasirinkimas == "2":
#                 saldytuvas = papildyti(saldytuvas)
#             elif pasirinkimas == "3":
#                 saldytuvas = istraukti(saldytuvas)
#             elif pasirinkimas == "4":
#                 perziureti(saldytuvas)
#             elif pasirinkimas == "5":
#                 produktas = input("Koki produkta ieskote? ")
#                 ieskoti_produkta(produktas, saldytuvas)
#             elif pasirinkimas == "6":
#                 print(f'Bendras produktu svoris: {skaiciuoti(saldytuvas)} kg.')
            elif pasirinkimas == "7":
                receptas = {}
                while True:
                    produktas = input('Iveskite produkta , arba "0", jeigu norite baigti.')
                    if produktas == '0':
                        with open("saldytuvas.json", "w") as saldytuvas_json:
                            saldytuvas_json = json.dump(Saldytuvas.turinys, saldytuvas_json, indent=2)
                        break
                    kiekis = input('Iveskite kieki')
                    receptas[produktas] = float(kiekis)
                ar_iseina(saldytuvas, receptas)

Saldytuvas.ijungti()    
>>>>>>> e11167f0a919826cfb39f931f4668a2c9551fbb4
