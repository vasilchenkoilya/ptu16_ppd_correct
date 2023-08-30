import json
import os

meniu = """
 A - Atidariti saldytuva
 1 - pridėti naują produktą 
 2 - papildyti produkto kiekį
 3 - ištraukti produktą nurodant kiekį
 4 - peržiūrėti produktus
 5 - ieškoti produktų
 6 - Suzinoti saldytuvo svori
 7 - Recepto patikrinimas (ar pakanka reikalingu produktu saldytuve) 
 0 - išėjimas
         """

def meniu_pasirinkimas():
    print(Saldytuvas.meniu)

class Saldytuvas:
    def __init__(self) -> None:
        try:
            with open("fridge.json", "r+") as saldytuvo_failas:
                self.turinys = json.load(saldytuvo_failas)
        except:
            self.turinys = {}
        pass
    def prideti(self, produktas, kiekis):
        self.turinys[produktas] = kiekis

    def papildyti(self) -> str | float :
        """Funkcija isves menu, kur bus parodyta lentele 
        su visais maisto produktais ir jiems priskirti 
        eiles numeriai
        """
        indeksas = 0
        produktai_saldytuve = list(self.turinys.keys())

        print("Saldytuve yra tokie produktai: ", "\n")
        print(f"{'Nr.':3s} | {'Maisto produktas':15s} | {'Produkto kiekis':10s}", end="\n")
        for produktas in self.turinys:
            print(f"{indeksas+1:>3d} | {produktas:<16s} | {self.turinys[produktas]}")
            indeksas += 1

        pasirinktas_indeksas = int(input("Parasykite norimo produkto numeri: ")) -1
        prideti = float(input("Parasykite kiek norite prideti produkto: "))

        pasirinktas_produktas = produktai_saldytuve[pasirinktas_indeksas]
        self.turinys[pasirinktas_produktas] += prideti
    
    def istraukti(self, produktas):
        if produktas in self.turinys:
            kiekis = float(input(f"Įveskite kiekį, kurį norite ištraukti (turimas kiekis: {self.turinys[produktas]}): "))
            if kiekis <= self.turinys[produktas]:
                self.turinys[produktas] -= kiekis
                print(f"{produktas} ištraukta {kiekis:.2f}, Dabartinis kiekis: {self.turinys[produktas]:.2f}")
                if self.turinys[produktas] == 0:
                    del self.turinys[produktas]
            else:
                print('Nepakankamas kiekis šaldytuve.')
        else:
            print(f"Produktas {produktas} nerastas šaldytuve.")

    def perziureti(self):
        print("Saldytuve esantys produktai:")
        print("{:<15} {:<10}".format("Produktas", "Kiekis"))
        print("-" * 25)
        for produktas, kiekis in self.turinys.items():
            print("{:<15} {:<10}".format(produktas, kiekis))

    def ieskoti_produkta(self, produktas):
        if produktas in self.turinys:
            print(f"{produktas} - yra {self.turinys[produktas]} šaldytuve.")
        else:
            print(f"{produktas} - nėra šaldytuve.")

    def svoris(self):
        saldytuvo_svoris = 0
        for svoris in self.turinys:
            saldytuvo_svoris += self.turinys[svoris]
        print(f'Bendras produktu svoris - {saldytuvo_svoris} kg.')


    def recepto_ingredientu_tikrinimas(self, receptas):
        iseina = []
        neiseina = {}
        for produktas, kiekis in receptas.items():
            if produktas in self.turinys and self.turinys[produktas] > kiekis:
                iseina.append(True)
            else:
                iseina.append(False)
                if produktas in self.turinys:
                    neiseina[produktas] = kiekis - self.turinys[produktas]
                else:
                    neiseina[produktas] = kiekis
        return iseina, neiseina

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
    
    def uzdaryti(self):
        with open("fridge.json", "w") as json_file:
            json.dump(self.turinys,json_file, indent=2)
        
    def atidaryti(self):
        if os.path.exists("fridge.json"):
            with open("fridge.json", "r") as json_file:
                self.turinys = json.load(json_file)
        else:
            print("nerastas .json failas")

      
whirpool = Saldytuvas()

while True:
    print(meniu)
    pasirinkimas = input("Pasirinkite veiksma: ")
    if pasirinkimas == "0":
        whirpool.uzdaryti()
        break
    elif pasirinkimas == "A":
        whirpool.atidaryti()
    elif pasirinkimas == "1":
        whirpool.prideti(
            produktas=input("Iveskite produkto pavadinima"), kiekis=float(input("Iveskite kieki"))
            )
    elif pasirinkimas == "2":
        whirpool.papildyti()
    elif pasirinkimas == "3":
        produktas = input("Iveskite produkto pavadinima: ")
        whirpool.istraukti(produktas)
    elif pasirinkimas == "4":
        whirpool.perziureti()
    elif pasirinkimas == "5":
        whirpool.ieskoti_produkta(produktas=input("iveskite ieskoma produkta"))
    elif pasirinkimas == "6":
        whirpool.svoris()
    elif pasirinkimas == "7":
        whirpool.receptas()
