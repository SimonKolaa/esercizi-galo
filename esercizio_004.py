costo_adulto = 10
costo_minorenne = 6

costoadulto = float(costo_adulto)
costominorenne = float(costo_minorenne)

n_adulti = float(input("Inserisci il numero di adulti: "))
n_minorenni = float(input("Inserisci il numero di minorenni: "))

costo = (costo_adulto * n_adulti)+(costo_minorenne * n_minorenni)

print(f"Il costo totale è di {costo}€")