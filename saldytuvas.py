import json
try:
    with open("saldytuvas.json", "r") as saldytuvas_dict:
        saldytuvas = json.load(saldytuvas_dict)
except:
    with open("saldytuvas.json", "w") as saldytuvas_dict:
        saldytuvas = json.load(saldytuvas_dict)
# saldytuvas = {
#     "apelsinai" : 1.5,
#     "duona" : 0.8,
#     "mesa" : 2,
#     "pienas" : 1,
#     "desra" : 0.5
# }

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

# 1 - pridėti naują produktą - Ilya
def prideti(saldytuvas):
    name = input('Įveskite produkto pavadinimą: ')
    kiekis = float(input('Įveskite kiekį: '))
    saldytuvas[name] = kiekis
    return saldytuvas

# 2 - papildyti produkto kiekį - Igoris
def papildyti(saldytuvas):
    indeksas = 0
    produktai_saldytuve = list(saldytuvas.keys())

    # Lentele kas yra saldytuve
    print("Saldytuve yra tokie produktai: ", "\n")
    print(f"{'Nr.':3s} | {'Maisto produktas':15s} | {'Produkto kiekis':10s}", end="\n")
    for produktas in saldytuvas:
        print(f"{indeksas+1:>3d} | {produktas:<16s} | {saldytuvas[produktas]}")
        indeksas += 1

    # Vartotojo ivestis
    pasirinktas_indeksas = int(input("Parasykite norimo produkto numeri: ")) -1
    prideti = int(input("Parasykite kiek norite prideti produkto: "))

    # Maisto papildymas
    pasirinktas_produktas = produktai_saldytuve[pasirinktas_indeksas]
    saldytuvas[pasirinktas_produktas] += prideti

    return saldytuvas

# 3 - ištraukti produktą nurodant kiekį -Eimantas
def istraukti(saldytuvas):
    produktas = input("Įveskite produkto pavadinimą, kurį norite ištraukti: ")
    if produktas in saldytuvas:
        kiekis = float(input(f"Įveskite kiekį, kurį norite ištraukti (turimas kiekis: {saldytuvas[produktas]}): "))
        if kiekis <= saldytuvas[produktas]:
            saldytuvas[produktas] -= kiekis
            print(f"{produktas} ištraukta {kiekis}, Dabartinis kiekis: {saldytuvas[produktas]}")
            if saldytuvas[produktas] == 0:
                del saldytuvas[produktas]
    return saldytuvas

# 4 - peržiūrėti produktus - Einaras
def perziureti(saldytuvas):
    print("Saldytuve esantys produktai:")
    print("{:<15} {:<10}".format("Produktas", "Kiekis"))
    print("-" * 25)
    for produktas, kiekis in saldytuvas.items():
        print("{:<15} {:<10}".format(produktas, kiekis))
    

# 5 - ieškoti produktų - Arnoldas
def ieskoti_produkta(produktas, saldytuvas):
    if produktas in saldytuvas:
        print(f"{produktas} - yra {saldytuvas[produktas]} šaldytuve.")
    else:
        print(f"{produktas} - nėra šaldytuve.")

# 6 skaiciuoti produktu svori
def skaiciuoti(saldytuvas):
    saldytuvo_svoris = 0
    for svoris in saldytuvas:
        saldytuvo_svoris += saldytuvas[svoris]
    return saldytuvo_svoris

# 7.1 surenkame produktus, kuriu receptui iseina i viena sarasa, kitus i kita
def recepto_ingredientu_tikrinimas(saldytuvas, receptas):
    iseina = []
    neiseina = {}
    for produktas, kiekis in receptas.items():
        if produktas in saldytuvas and saldytuvas[produktas] > kiekis:
            iseina.append(True)
        else:
            iseina.append(False)
            neiseina[produktas] = kiekis - saldytuvas[produktas]
    return iseina, neiseina

# 7.2 Isspaudinam kiek iseina porciju pagal recepta
def spausdinti_kiek_iseina(saldytuvas, receptas):
    print("Pakankamas produktu kiekis sitam receptui saldytuve")
    kiek_porciju = 0
    porcijos = []
    for produktas, kiekis in receptas.items():
        if produktas in saldytuvas:
            kiek_porciju = int(saldytuvas[produktas] / kiekis)
            porcijos.append(kiek_porciju)
    print(f'Iseis {min(porcijos)} porciju')

# 7 recepto patikrinimas
def ar_iseina(saldytuvas, receptas):
    iseina, neiseina = recepto_ingredientu_tikrinimas(saldytuvas, receptas)
    if False in iseina:
        for nepakankamas_produktas, nepakankamas_kiekis in neiseina.items():
            print(f'Nepakanka "{nepakankamas_produktas}" : {nepakankamas_kiekis}')
    else:
        spausdinti_kiek_iseina(saldytuvas, receptas)

while True:
    print(meniu)
    pasirinkimas = input("Pasirinkite veiksma: ")
    if pasirinkimas == "0":
        break
    elif pasirinkimas == "1":
        saldytuvas = prideti(saldytuvas)
    elif pasirinkimas == "2":
        saldytuvas = papildyti(saldytuvas)
    elif pasirinkimas == "3":
        saldytuvas = istraukti(saldytuvas)
    elif pasirinkimas == "4":
        perziureti(saldytuvas)
    elif pasirinkimas == "5":
        produktas = input("Koki produkta ieskote? ")
        ieskoti_produkta(produktas, saldytuvas)
    elif pasirinkimas == "6":
        print(f'Bendras produktu svoris: {skaiciuoti(saldytuvas)} kg.')
    elif pasirinkimas == "7":
        receptas = {}
        while True:
            produktas = input('Iveskite produkta , arba "0", jeigu norite baigti.')
            if produktas == '0':
                with open("saldytuvas.json", "w") as saldytuvas_json:
                    saldytuvas_json = json.dump(saldytuvas, saldytuvas_json, indent=2)
                break
            kiekis = input('Iveskite kieki')
            receptas[produktas] = float(kiekis)
        ar_iseina(saldytuvas, receptas)