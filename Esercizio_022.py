libro = {
    "titolo": "Le avventure del Mancio",
    "autore": "Armando Lorenzo Mancini",
    "anno": 2023,
}

#Aggiungo un elemento
libro["genere"] = "Pornografico"

#Modifico un elemento
libro["anno"] = 1922

#Elimino un elemento
del libro["autore"]

#Itero attraverso il dizionario
#Stampo tutte le chiavi
for key in libro.keys():
    print(key)

#Stampo tutti i valori
for value in libro.values():
    print(value)

#Stampo tutte le coppie chiave-valore
for key, value in libro.items():
    print(key, "in", value)
