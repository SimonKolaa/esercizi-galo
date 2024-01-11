museo = {'stanze': []}

while True:
    print("\nMenu:")
    print("1. Creare una nuova stanza")
    print("2. Aggiungere un'opera ad una stanza")
    print("3. Consultare le opere presenti in una stanza")
    print("4. Consultare le stanze presenti")
    print("5. Cercare le informazioni su un'opera")
    print("6. Cancellare un'opera")
    print("7. Cancellare una stanza solo se vuota")
    print("8. Esci")

    scelta = input("Inserisci il numero corrispondente all'azione desiderata: ")

    if scelta == '1':
        nuova_stanza = {'id': input("ID: "), 'denominazione': input("Denominazione: "), 'metratura': input("Metratura: "), 'opere': []}
        museo['stanze'].append(nuova_stanza)
        print(f"Stanza {nuova_stanza['denominazione']} creata con successo.")

    elif scelta == '2':
        id_stanza = input("ID della stanza: ")
        stanza = next((s for s in museo['stanze'] if s['id'] == id_stanza), None)
        
        if stanza:
            nuova_opera = {'titolo': input("Titolo: "), 'artista': input("Artista: "), 'anno': input("Anno: ")}
            stanza['opere'].append(nuova_opera)
            print(f"Opera {nuova_opera['titolo']} aggiunta alla stanza {id_stanza}.")
        else:
            print(f"Stanza con ID {id_stanza} non trovata.")

    elif scelta == '3':
        id_stanza = input("ID della stanza: ")
        stanza = next((s for s in museo['stanze'] if s['id'] == id_stanza), None)
        
        if stanza:
            print(f"\nOpere nella stanza {id_stanza}:")
            for opera in stanza['opere']:
                print(f"Titolo: {opera['titolo']}, Artista: {opera['artista']}, Anno: {opera['anno']}")
        else:
            print(f"Stanza con ID {id_stanza} non trovata.")

    elif scelta == '4':
        print("\nStanze presenti nel museo:")
        for stanza in museo['stanze']:
            print(f"ID: {stanza['id']}, Denominazione: {stanza['denominazione']}, Metratura: {stanza['metratura']}")

    elif scelta == '5':
        titolo = input("Titolo dell'opera: ")
        opera_trovata = next((opera for stanza in museo['stanze'] for opera in stanza['opere'] if opera['titolo'] == titolo), None)
        
        if opera_trovata:
            print(f"\nInformazioni sull'opera {titolo}:")
            print(f"Stanza: {stanza['id']}, Artista: {opera_trovata['artista']}, Anno: {opera_trovata['anno']}")
        else:
            print(f"Opera con titolo {titolo} non trovata nel museo.")

    elif scelta == '6':
        titolo = input("Titolo dell'opera da cancellare: ")
        
        for stanza in museo['stanze']:
            for opera in stanza['opere']:
                if opera['titolo'] == titolo:
                    stanza['opere'].remove(opera)
                    print(f"Opera {titolo} cancellata con successo.")
                    break
        else:
            print(f"Opera con titolo {titolo} non trovata nel museo.")

    elif scelta == '7':
        id_stanza = input("ID della stanza da cancellare: ")
        stanza = next((s for s in museo['stanze'] if s['id'] == id_stanza), None)

        if stanza and not stanza['opere']:
            museo['stanze'].remove(stanza)
            print(f"Stanza {id_stanza} cancellata con successo.")
        elif not stanza:
            print(f"Stanza con ID {id_stanza} non trovata.")
        else:
            print(f"Impossibile cancellare la stanza {id_stanza} poiché non è vuota.")

    elif scelta == '8':
        break

    else:
        print("Scelta non valida. Riprova.")
