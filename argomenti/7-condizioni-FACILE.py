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
EMAIL = "studente@example.com"
PASSWORD = "Python123"
email = input("inserire email\n")
password = input("inserire password\n")
if email == EMAIL and password == PASSWORD:
    print("Accesso consentito")
elif email != EMAIL:
    print("Email non riconosciuta")
else:
    print("Password errata")