voto1 = int(input("Inserisci il voto:"))
n_crediti1 = int(input("Inserisci il numero di crediti:"))

voto2 = int(input("Inserisci il secondo voto:"))
n_crediti2 = int(input("Inserisci il secondo numero di crediti"))

voto3 = int(input("Inserisci il terzo voto:"))
n_crediti3 = int(input("Inserisci il terzo numero di crediti:"))

media_ponderata = (voto1 * n_crediti1 + voto2 * n_crediti2 + voto3 * n_crediti3) / (n_crediti1 + n_crediti2 + n_crediti3)

if voto1 > 30 and voto2 > 30 and voto3 > 30 and n_crediti1 > 12 and n_crediti2 > 12 and n_crediti3 > 12:
    print ("ERROR")
    
    
    
    