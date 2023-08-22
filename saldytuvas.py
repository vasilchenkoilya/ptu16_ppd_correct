
saldytuvas = {
    "apelsinai" : 1.5,
    "duona" : 0.8,
    "mesa" : 2,
    "pienas" : 1,
    "desra" : 0.5
}

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
    name = input('Iveskite produkto pavadinima')
    kiekis = float(input('Iveskite kieki'))
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
def istraukti():
    pass

# 4 - peržiūrėti produktus - Einaras
def perziureti():
    pass

# 5 - ieškoti produktų - Arnoldas
def ieskoti():
    pass

# 0 - išėjimas - Ilya
# UPDATE INFo 
def skaiciuoti(saldytuvas):
    saldytuvo_svoris = 0
    for svoris in saldytuvas:
        saldytuvo_svoris += saldytuvas[svoris]
    return saldytuvo_svoris

def ar_iseina(saldytuvas, receptas):
    iseina = []
    for produktas, kiekis in receptas.items():
        if produktas in saldytuvas and saldytuvas[produktas] > kiekis:
            iseina.append(True)
        else:
            iseina.append(False)
    if False in iseina:
        for produktas, kiekis in receptas.items():
            if produktas in saldytuvas:
                nepakanka = kiekis - saldytuvas[produktas]
            else:
                nepakanka = kiekis
            print(f'Nepakanka {produktas} ,{nepakanka}')
    else:
        print("Pakankamas produktu kiekis sitam receptui saldytuve")
        kiek_porciju = 0
        porcijos = []
        for produktas, kiekis in receptas.items():
            if produktas in saldytuvas:
                kiek_porciju = int(saldytuvas[produktas]/kiekis)
                porcijos.append(kiek_porciju)
        print(f'Iseis {min(porcijos)} porciju')
    
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
        # Ištraukti produktą nurodant kiekį
        produktas = input("Įveskite produkto pavadinimą, kurį norite ištraukti: ")
        if produktas in saldytuvas:
            kiekis = float(input(f"Įveskite kiekį, kurį norite ištraukti (turimas kiekis: {saldytuvas[produktas]}): "))
            if kiekis <= saldytuvas[produktas]:
                saldytuvas[produktas] -= kiekis
                print(f"{produktas} ištraukta {kiekis} vnt. Dabartinis kiekis: {saldytuvas[produktas]}")
                if saldytuvas[produktas] == 0:
                    del saldytuvas[produktas]
            else:
                print("Nepakankamas kiekis šaldytuve.")
        else:
            print(f"{produktas} nėra šaldytuve.")
    elif pasirinkimas == "4":
        print("Saldytuve esantys produktai:")
        print("{:<15} {:<10}".format("Produktas", "Kiekis"))
        print("-" * 25)
        for produktas, kiekis in saldytuvas.items():
            print("{:<15} {:<10}".format(produktas, kiekis))
    elif pasirinkimas == "5":
        
        # Pruduktu paeska
        produktas = input("Koki produkta ieskote? ")
        if produktas in saldytuvas:
            print(f"{produktas} - yra {saldytuvas[produktas]} šaldytuve.")
        else:
            print(f"{produktas} - nėra šaldytuve.")
    elif pasirinkimas == "6":
        print(f'{skaiciuoti(saldytuvas)} kg.')
    elif pasirinkimas == "7":
        vartotojo_ivedimas = input('Iveskite recepta pagal pavizdi : "produktas: kiekis", ""produktas: kiekis", .... ')
        receptas_list = vartotojo_ivedimas.split(', ')
        receptas = {}
        for recepto_dalis in receptas_list:
            key, value = recepto_dalis.split(': ')
            receptas[key] = float(value)
        ar_iseina(saldytuvas,receptas)