
# while True : - True
# 1 - pridėti naują produktą - Ilya

# 2 - papildyti produkto kiekį - Igoris

# 3 - ištraukti produktą nurodant kiekį -Eimantas

# 4 - peržiūrėti produktus - Einaras

# 5 - ieškoti produktų - Arnoldas

# 0 - išėjimas - Ilya
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
        pass
    elif pasirinkimas == "2":
        #pasirinkti produkta
        #parasyti kiek kg/l prideti (skaicius)
        print("Saldytuve yra tokie produktai: ")
        print(saldytuvas.keys(), enumerate(saldytuvas.keys()) sep="\n")
        produkto_pasirinkimas = input("Parasykite norimo produkto numeri: ")
        prideti = input("Parasykite kiek norite prideti produkto: ")




    elif pasirinkimas == "3":
        pass
    elif pasirinkimas == "4":
        pass
    elif pasirinkimas == "5":
        pass
