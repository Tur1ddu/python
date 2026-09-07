def idoneata_sbarco(eta):
    '''
    Restituisce vero se sei idoneo allo sbarco
    pertanto se sei maggiorenne oppure no
    '''
    idoneo = False
    if eta > 18:
        idoneo = True
    return idoneo
    
def soglia_tolleranza(tolleranza_grav):
    '''
    decidere se la tolleranza gravirazione è STANDARD o ALTA
    '''
    tolleranza = "ALTA"
    if tolleranza_grav < 1.9:
        tolleranza = "STANDARD"
    return tolleranza


def calcolo_tariffa(pianeta, tolleranza):
    '''
    Serve per calcolare la tariffa.
    tariffa senza calcolo (di partenza) 100
    gli sconti sono tutti da 30
    le quote aggiuntive sono tutti da 50
    le tolleranze critiche sono tutte da aggiungere 20
    '''
    TARIFFA_BASE = 100
    SCONTO = 30
    QUOTA_AGGIUNTIVA = 50
    
    tariffa = TARIFFA_BASE
    
    if pianeta == "Terra":
        tariffa = TARIFFA_BASE - SCONTO
    else:
        tariffa = TARIFFA_BASE + QUOTA_AGGIUNTIVA

    if tolleranza == "ALTA":
        tariffa += 20
    
    return tariffa
    


print("==== TERMINALE AUTOMATICO DI SBARCO - NEO-VENEZIA ====")


#pianeta e nome per me è una stringa pertanto basta input (senza gestione degli errori)
nome = str(input("inserire nome\n"))
pianeta = input("inserire pianeta di provenienza\n")

#gestione eta perchè se va in errore devo impostare 18 anni
try:
    eta = int(input("inserire eta galattica\n"))
except ValueError:
    print("[AVVISO] Rilevata anomalia nei dati inseriti! Non hai inserito un numero.\n-> Attivazione protocollo di sicurezza e assegnazione parametri di backup.")
    print("Impostazione automatica: Eta' = 18 anni")
    eta = 18

try:
    tolleranza_grav = float(input("inserire tolleranza gravitazionale\n"))
except ValueError:
    print("[AVVISO] Rilevata anomalia nei dati inseriti! Non hai inserito una tolleranza compatibile.\n-> Attivazione protocollo di sicurezza e assegnazione parametri di backup.")
    print("Impostazione automatica: Eta' = 18 anni")
    tolleranza_grav = 18


print("--- ELABORAZIONE PROTOCOLLO DI SBARCO ---")
print(f"ID Viaggiatore confermato: {nome} (Origine: {pianeta})")

#controllo idoneatà
idoneo = idoneata_sbarco(eta)

if idoneo:
    tolleranza = soglia_tolleranza(tolleranza_grav)
    
    #controllo tolleranza
    if tolleranza == "STANDARD":
        print("Tolleranza gravitazionale inferiore rilevata\n")
        print("Assegnazione zona protetta a gravita' standard\n")
    else:
        print("Tolleranza gravitazionale elevata")
        print("Assegnazione logistica: SETTORE ALTA GRAVITA'")
    
    #calcolo tariffa
    tariffa = calcolo_tariffa(pianeta, tolleranza)
    
    print(f"Tariffa di sbarco calcolata: {tariffa}") 
    print("=== PROCEDURA COMPLETATA CON SUCCESSO. BENVENUTO A NEO-VENEZIA! ===")
else:
    print("Imbarco automatico negato, si prega di contattare l'assistenza consolare\n")