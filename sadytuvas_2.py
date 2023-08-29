import json

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
<<<<<<< HEAD
def prideti(self, product:str, quantity:float):
    self.turinys[product] = quantity
=======
    def meniu_pasirinkimas():
        print(Saldytuvas.meniu)
=======
try:
    with open("fridge.json", "r+") as saldytuvas_dict:
        saldytuvas = json.load(saldytuvas_dict)
except:
    saldytuvas = {}
    with open("fridge.json", "w") as saldytuvas_dict:
        json.dump(saldytuvas, saldytuvas_dict)

class Saldytuvas:
    
    turinys = saldytuvas
>>>>>>> cc5cb9438f17c48a4b03580f53ba004a9ef7d192

    def prideti(self, produktas, kiekis):
        self.turinys[produktas] = kiekis
>>>>>>> e11167f0a919826cfb39f931f4668a2c9551fbb4

<<<<<<< HEAD
def papildyti(self, product:str, quantity:float):
    pass
=======
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
>>>>>>> cc5cb9438f17c48a4b03580f53ba004a9ef7d192
    
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
<<<<<<< HEAD
def receptas(self, product:str, quantity:float):
    pass
    
=======
    def receptas(self, product:str, quantity:float):
        pass
=======
    def recepto_ingredientu_tikrinimas(self, receptas):
        iseina = []
        neiseina = {}
        for produktas, kiekis in receptas.items():
            if produktas in self.turinys and self.turinys[produktas] > kiekis:
                iseina.append(True)
            else:
                iseina.append(False)
                neiseina[produktas] = kiekis - self.turinys[produktas]
        return iseina, neiseina
>>>>>>> cc5cb9438f17c48a4b03580f53ba004a9ef7d192

        # 7 Isspaudinam kiek iseina porciju pagal recepta
    def spausdinti_kiek_iseina(self, receptas):
        print("Pakankamas produktu kiekis sitam receptui saldytuve")
        kiek_porciju = 0
        porcijos = []
        for produktas, kiekis in receptas.items():
            if produktas in self.turinys:
                kiek_porciju = int(self.turinys[produktas] / kiekis)
                porcijos.append(kiek_porciju)
        print(f'Iseis {min(porcijos)} porciju')

        # 7 recepto patikrinimas
    def ar_iseina(self, receptas):
        iseina, neiseina = self.recepto_ingredientu_tikrinimas(receptas)
        if False in iseina:
            for nepakankamas_produktas, nepakankamas_kiekis in neiseina.items():
                print(f'Nepakanka "{nepakankamas_produktas}" : {nepakankamas_kiekis}')
        else:
            self.spausdinti_kiek_iseina(receptas)
        
    def receptas(self):
        receptas = {}        
        while True:
            produktas = input('Iveskite produkta , arba "0", jeigu norite baigti.')
            if produktas == '0':
                break
            kiekis = input('Iveskite kieki')
            receptas[produktas] = float(kiekis)
        self.ar_iseina(receptas)
      
whirpool = Saldytuvas()

<<<<<<< HEAD
Saldytuvas.ijungti()    
>>>>>>> e11167f0a919826cfb39f931f4668a2c9551fbb4
=======
while True:
    print(meniu)
    pasirinkimas = input("Pasirinkite veiksma: ")
    if pasirinkimas == "0":
        with open("fridge.json", "w") as saldytuvas_json:
            saldytuvas_json = json.dump(Saldytuvas.turinys, saldytuvas_json, indent=2)
        break
    elif pasirinkimas == "1":
        whirpool.prideti(
            produktas=input("Iveskite produkto pavadinima"), kiekis=float(input("Iveskite kieki"))
            )
    elif pasirinkimas == "2":
        whirpool.papildyti()
    elif pasirinkimas == "3":
        whirpool.istraukti()
    elif pasirinkimas == "4":
        whirpool.perziureti()
    elif pasirinkimas == "5":
        whirpool.ieskoti_produkta()
    elif pasirinkimas == "6":
        whirpool.svoris()
    elif pasirinkimas == "7":
        whirpool.receptas()
>>>>>>> cc5cb9438f17c48a4b03580f53ba004a9ef7d192
