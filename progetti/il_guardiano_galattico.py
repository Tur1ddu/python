def credenziali_viaggiatore():
    try:
        verifica = ""
        grav = 1.9
        tariffa = 100
        sconto = 30
        quota_aggiuntiva = 50
        print("==== TERMINALE AUTOMATICO DI SBARCO - NEO-VENEZIA ====")
        pianeta = str(input("inserire pianeta di provenienza\n"))
        nome = str(input("inserire nome\n"))
        eta = int(input("inserire eta galattica\n"))
        tolleranza_grav = float(input("inserire tolleranza gravitazionale\n"))
    except ValueError:
        print("[AVVISO] Rilevata anomalia nei dati inseriti! Non hai inserito un numero.\n-> Attivazione protocollo di sicurezza e assegnazione parametri di backup.")
        print("-> Impostazione automatica: Nome = BIRBION Eta' = 18 anni, Tolleranza = 1.9G")
        if ValueError:
            nome = "BIRBION"
            eta = 18
            tolleranza_grav = 1.9
        if eta < 18:
            print("Imbarco automatico negato, si prega di contattare l'assistenza consolare\n")
        else:
            print("Idonieta' biologica confermata")
        if tolleranza_grav < 1.9:
            print("Tolleranza gravitazionale inferiore rilevata\n")
            print("Assegnazione zona protetta a gravita' standard\n")
        else:
            print("Tolleranza gravitazionale elevata")
            print("Assegnazione logistica: SETTORE ALTA GRAVITA'")
        if pianeta != "Terra":
            tariffa = tariffa + quota_aggiuntiva
            print("Per i viaggiatori provenienti da altri pianeti dovranno pagare una quota aggiuntiva per coprire i costi di pressurizzazione dell'atmosfera\n")
            print(f"Tariffa di sbarco calcolata: {tariffa}")
        if pianeta == "Terra":
            print("Per i viaggiatori proveniente dalla Terra verrà applicato uno sconto sulla tariffa di sbarco\n")
            tariffa = tariffa - sconto 
            print(f"Tariffa di sbarco calcolata : {tariffa}")
    except ValueError:
        print("Errore di sistema, inserire correttamente il pianeta di provenienza")
    while ValueError:
        pianeta = input("reinserire il pianeta di provenienza, per eventuali errori\n")
        verifica = input("scrivere fine per terminare la registrazione \n")
        
        if verifica == "fine":
            break
        if pianeta == "Terra":
            print("Per i viaggiatori proveniente dalla Terra verrà applicato uno sconto sulla tariffa di sbarco\n")
            tariffa = tariffa - sconto 
            print(f"Tariffa di sbarco calcolata : {tariffa}")
        if pianeta != "Terra":
            tariffa = tariffa + quota_aggiuntiva
            print("Per i viaggiatori provenienti da altri pianeti dovranno pagare una quota aggiuntiva per coprire i costi di pressurizzazione dell'atmosfera\n")
            print(f"Tariffa di sbarco calcolata: {tariffa}") 

    print(f"Credenziali registrate: Nome = {nome}  Eta' = {eta}  Pianeta = {pianeta}  Tolleranza = {tolleranza_grav}G  Tariffa = {tariffa} ")
    print(f"BENVENUTO A NEO-VENEZIA!")
credenziali_viaggiatore()