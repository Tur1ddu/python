def credenziali_viaggiatore():
    grav = 9.8
    sconto = 30
    print("benvenuti allo spazioporto di Neo-Venezia")
    nome = input("inserire nome\n")
    eta = int(input("inserire eta galattica\n"))
    pianeta = input("inserire pianeta di provenienza\n")
    tolleranza_grav = float(input("inserire tolleranza gravitazionale\n"))
    print(f"ID Viaggiatore confermato: {nome} (Origine: {pianeta})")

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
        tariffa = 100 - sconto
        print(sconto)
    else:
        print("Per i viaggiatori provenienti da altri pianeti dovranno pagare una quota aggiuntiva per coprire i costi di pressurizzazione dell'atmosfera\n")
        
credenziali_viaggiatore()