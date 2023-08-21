
# while True : - True
# 1 - pridėti naują produktą - Ilya

# 2 - papildyti produkto kiekį - Igoris

# 3 - ištraukti produktą nurodant kiekį -Eimantas

# 4 - peržiūrėti produktus - Einaras

# 5 - ieškoti produktų - Arnoldas

# 0 - išėjimas - Ilya
saldytuvas = {
    "apelsinai": 1.5,
    "bananai" : 2,
    "mesa" : 3,
    "pienas" : 0.9}
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
        pass
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
         print("Saldytuve esantys produktai:")
         print("{:<15} {:<10}".format("Produktas", "Kiekis"))
         print("-" * 25)
         for produktas, kiekis in saldytuvas.items():
          print("{:<15} {:<10}".format(produktas, kiekis))
    elif pasirinkimas == "5":
        pass
