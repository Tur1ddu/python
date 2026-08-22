"""
Scrivi un programma che simuli un semplice sistema di login.

Il programma deve chiedere all'utente di inserire un'email e una password.

Il programma deve controllare se l'email inserita corrisponde a quella registrata
(usiamo come email registrata "studente@example.com") e, solo se l'email è corretta,
verificare se la password inserita corrisponde a quella registrata (usiamo come password "Python123").

Se entrambe le credenziali sono corrette, stampa il messaggio "Accesso consentito";
se l'email è errata, stampa "Email non riconosciuta";
se l'email è corretta ma la password è sbagliata, stampa "Password errata".


Esempio:
input:
studente@example.com
Python123

output:
Accesso consentito

input:
juan@example.com
qualsiasi

output:
Email non riconosciuta

input:
studente@example.com
passwordsbagliata

output:
Password errata
"""

email="ciaomamma@gmail.com"
password="Python123"

print("richiesto accesso con credenziali ")
emailUtente = input("inserisci l'email ")
passwordUtente = input("inserisci la password ")
if email == emailUtente and password == passwordUtente :
    print("accesso eseguito correttamente ")
elif password == passwordUtente :
    print("email corretta password errata riprova")
elif email == emailUtente :
    print("password corretta email errata riprova")
else:
    print("credenziali incorrette riprova ")