prodotti = ["laptop", "mouse", "tastiera"]
prezzi = [1000, 50, 70]
quantità = [5, 10, 8]

print("Inventario corrente:")
for i in range(len(prodotti)):
    print(f"Prodotto: {prodotti[i]}, Prezzo: {prezzi[i]}, Quantità: {quantità[i]}")

prodotto = input("Inserisci il nome del prodotto: ")
prezzo = float(input("Inserisci il prezzo del prodotto: "))
quantità_prodotto = int(input("Inserisci la quantità del prodotto: "))

if prodotto in prodotti:
    prezzi = prezzo
    quantità = quantità_prodotto
else:
    prodotti.append(prodotto)
    prezzi.append(prezzo)
    quantità.append(quantità_prodotto)
prodotto_da_rimuovere = input("Inserisci il nome del prodotto da rimuovere: ")
if prodotto_da_rimuovere in prodotti:
    del prodotti
    del prezzi
    del quantità
else:
    print("Il prodotto specificato non esiste nell'inventario.")
inventario_totale = sum(quantità)
valore_totale_scorte = sum([prezzi[i] * quantità[i] for i in range(len(prodotti))])
print("Inventario aggiornato:")
for i in range(len(prodotti)):
    print(f"Prodotto: {prodotti[i]}, Prezzo: {prezzi[i]}, Quantità: {quantità[i]}")
print(f"Inventario totale: {inventario_totale}")
print(f"Valore totale delle scorte: {valore_totale_scorte}")
