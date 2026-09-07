credenziali = {
        
    }


def credenziali_viaggiatore():
    try:
        grav = 1.9
        sconto = 30
        tariffa = 100
        print("==== TERMINALE AUTOMATICO DI SBARCO - NEO-VENEZIA ====")
        nome = str(input("inserire nome\n"))
    except ValueError:
        print("[AVVISO] Rilevata anomalia nei dati inseriti! Non hai inserito un nome.\n")
        print("--> Attivazione protocollo di sicurezza e assegnazione parametri di backup")
        if type(nome) != str(nome):
            nome = "John Doe"
            print(f"Assegnazione nome temporaneo {nome}")
        eta = int(input("inserire eta galattica\n"))
    except ValueError:
        print("[AVVISO] Rilevata anomalia nei dati inseriti! Non hai inserito un numero.\n")
        print("--> Attivazione protocollo di sicurezza e assegnazione parametri di backup")
        pianeta = input("inserire pianeta di provenienza\n")
    except ValueError:
        print("[AVVISO] Rilevata anomalia nei dati inseriti! Non hai inserito un numero.\n")
        print("--> Attivazione protocollo di sicurezza e assegnazione parametri di backup")
    
        tolleranza_grav = float(input("inserire tolleranza gravitazionale\n"))
    except ValueError:
        print("[AVVISO] Rilevata anomalia nei dati inseriti! Non hai inserito un numero.\n")
        print("--> Attivazione protocollo di sicurezza e assegnazione parametri di backup")
                
    print(f"ID Viaggiatore confermato: {nome} (Origine: {pianeta})")
    try:
        if eta < 18:
            print("Imbarco automatico negato, si prega di contattare l'assistenza consolare\n")
        else:
            print("Idonieta' biologica confermata")
        if tolleranza_grav < 9.8:
            print("Tolleranza gravitazionale inferiore rilevata\n")
            print("Assegnazione zona protetta a gravita' standard\n")
        else:
            print("Tolleranza gravitazionale elevata")
            print("Assegnazione logistica: SETTORE ALTA GRAVITA'")
        if pianeta == "Terra":
            print("Per i viaggiatori proveniente dalla Terra verrà applicato uno sconto sulla tariffa di sbarco\n")
            sconto = tariffa - sconto 
            print(f"Tariffa di sbarco calcolata : {sconto}")
    except ValueError:
        print("Errore di sistema, inserire correttamente il pianeta di provenienza")
        if pianeta != "Terra":
            sconto = tariffa + 50
            print("Per i viaggiatori provenienti da altri pianeti dovranno pagare una quota aggiuntiva per coprire i costi di pressurizzazione dell'atmosfera\n")
            print(f"Tariffa di sbarco calcolata: {sconto}")  
credenziali_viaggiatore()