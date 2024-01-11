IVA = 0.22 

parco_auto = []

while True:
    print("\nMenu:")
    print("1. Aggiunta di un veicolo")
    print("2. Rimozione di un veicolo")
    print("3. Calcolo del bollo di un veicolo")
    print("4. Profitto di un veicolo")
    print("5. Profitto totale del parco auto")
    print("6. Esci")

    scelta = input("Inserisci il numero corrispondente all'azione desiderata: ")

    if scelta == '1':
        veicolo = {
            'marca': input("Marca: "),
            'modello': input("Modello: "),
            'cilindrata': float(input("Cilindrata (in kW): ")),
            'potenza_kw': float(input("Potenza (in kW): ")),
            'anno_immatricolazione': int(input("Anno di immatricolazione: ")),
            'costo_gestione': float(input("Costo di gestione annuale: ")),
            'giorni_affitto': int(input("Numero di giorni di affitto: ")),
            'prezzo_giornaliero': float(input("Prezzo giornaliero di noleggio: "))
        }
        parco_auto.append(veicolo)
        print("Veicolo aggiunto con successo.")

    elif scelta == '2':
        if parco_auto:
            indice_rimozione = int(input("Inserisci l'indice del veicolo da rimuovere: "))
            if 0 <= indice_rimozione < len(parco_auto):
                veicolo_rimosso = parco_auto.pop(indice_rimozione)
                print(f"Veicolo {veicolo_rimosso['marca']} {veicolo_rimosso['modello']} rimosso con successo.")
            else:
                print("Indice non valido.")
        else:
            print("Il parco auto è vuoto.")

    elif scelta == '3':
        if parco_auto:
            indice_calcolo_bollo = int(input("Inserisci l'indice del veicolo per il calcolo del bollo: "))
            if 0 <= indice_calcolo_bollo < len(parco_auto):
                veicolo_calcolo_bollo = parco_auto[indice_calcolo_bollo]
                bollo = 2.58 * min(100, veicolo_calcolo_bollo['potenza_kw'])
                bollo += 3.87 * max(0, veicolo_calcolo_bollo['potenza_kw'] - 100)
                bollo += 20 * max(0, veicolo_calcolo_bollo['potenza_kw'] - 185)
                print(f"Il bollo per il veicolo {veicolo_calcolo_bollo['marca']} {veicolo_calcolo_bollo['modello']} è: {bollo} euro.")
            else:
                print("Indice non valido.")
        else:
            print("Il parco auto è vuoto.")

    elif scelta == '4':
        if parco_auto:
            indice_profitto_veicolo = int(input("Inserisci l'indice del veicolo per il calcolo del profitto: "))
            if 0 <= indice_profitto_veicolo < len(parco_auto):
                veicolo_profitto = parco_auto[indice_profitto_veicolo]
                profitto = veicolo_profitto['giorni_affitto'] * (veicolo_profitto['prezzo_giornaliero'] * (1 - IVA) - veicolo_profitto['costo_gestione'] - bollo)
                print(f"Il profitto (prima delle tasse) per il veicolo {veicolo_profitto['marca']} {veicolo_profitto['modello']} è: {profitto} euro.")
            else:
                print("Indice non valido.")
        else:
            print("Il parco auto è vuoto.")

    elif scelta == '5':
        if parco_auto:
            profitto_totale = 0
            for veicolo in parco_auto:
                bollo = 2.58 * min(100, veicolo['potenza_kw'])
                bollo += 3.87 * max(0, veicolo['potenza_kw'] - 100)
                bollo += 20 * max(0, veicolo['potenza_kw'] - 185)
                profitto_veicolo = veicolo['giorni_affitto'] * (veicolo['prezzo_giornaliero'] * (1 - IVA) - veicolo['costo_gestione'] - bollo)
                profitto_totale += profitto_veicolo
            print(f"Il profitto totale (prima delle tasse) del parco auto è: {profitto_totale} euro.")
        else:
            print("Il parco auto è vuoto.")

    elif scelta == '6':
        break

    else:
        print("Scelta non valida. Riprova.")
