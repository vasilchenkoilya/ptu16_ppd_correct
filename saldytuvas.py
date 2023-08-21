
# while True : - True
# 1 - pridėti naują produktą - Ilya

# 2 - papildyti produkto kiekį - Igoris

# 3 - ištraukti produktą nurodant kiekį -Eimantas

# 4 - peržiūrėti produktus - Einaras

# 5 - ieškoti produktų - Arnoldas

# 0 - išėjimas - Ilya
import os
#os system isvalo konsole kaip clear komanda kad kiekviena karta tiktais reikalingas tekstas butu
os.system("cls")
saldytuvas = {}
meniu = """
 1 - pridėti naują produktą 
 2 - papildyti produkto kiekį
 3 - ištraukti produktą nurodant kiekį
 4 - peržiūrėti produktus
 5 - ieškoti produktų 
 0 - išėjimas  """
while True:
    pasirinkimas = input("Pasirinkite: ")
    if pasirinkimas == "0":
        break
    elif pasirinkimas == "1":
        produktas = input('Iveskite produkta: ')
        kiekis = input('Iveskite kieki: ')
        saldytuvas[produktas] = kiekis
    elif pasirinkimas == "2":
        os.system("cls")
        
        #kintamosios - "saldytuvas" galima istrinti
        saldytuvas = {
                    "Mesa" : 4,
                    "Gerimai" : 1,
                    "Specijos" : 5,
                }
        indeksas = 0
        produktai_saldytuve = list(saldytuvas.keys())

        #Lentele kas yra saldytuve
        print("Saldytuve yra tokie produktai: ", "\n")
        print(f"{'Nr.':3s} | {'Maisto produktas':15s} | {'Produkto kiekis':10s}", end="\n")
        for produktas in saldytuvas:
            print(f"{indeksas+1:>3d} | {produktas:<16s} | {saldytuvas[produktas]:<5d}")
            indeksas += 1

        #Vartotojo ivestis
        pasirinktas_indeksas = int(input("Parasykite norimo produkto numeri: ")) -1
        prideti = int(input("Parasykite kiek norite prideti produkto: "))

        #Maisto papildymas
        pasirinktas_produktas = produktai_saldytuve[pasirinktas_indeksas]
        saldytuvas[pasirinktas_produktas] += prideti


        break
    elif pasirinkimas == "3":
        # Ištraukti produktą nurodant kiekį
        produktas = input("Įveskite produkto pavadinimą, kurį norite ištraukti: ")
        if produktas in saldytuvas:
            kiekis = int(input(f"Įveskite kiekį, kurį norite ištraukti (turimas kiekis: {saldytuvas[produktas]}): "))
            if kiekis <= saldytuvas[produktas]:
                saldytuvas[produktas] -= kiekis
                print(f"{produktas} ištraukta {kiekis} vnt. Dabartinis kiekis: {saldytuvas[produktas]}")
            else:
                print("Nepakankamas kiekis šaldytuve.")
        else:
            print(f"{produktas} nėra šaldytuve.")
    elif pasirinkimas == "4":
        print(saldytuvas)
    elif pasirinkimas == "5":
        pass
