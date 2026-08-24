"""
Il programma dovrà seguire i seguenti punti obbligatori:

1. Chiedi all'utente di inserire la sua email registrata e la password.

2. Se l'email non corrisponde all'unica email registrata (ad es. "studente@istituto.it"),
il programma deve segnalare "Email non riconosciuta" e terminare l'esecuzione.

3. Se l'email è corretta, verifica la password (ad es. "Passw0rd!*" esatta).
Se la password è errata, stampa "Password errata" e termina.

4. Se l'accesso è consentito (email e password corrette), prosegui chiedendo all'utente di inserire tre numeri interi: 
   - Età
   - Numero di anni di esperienza in programmazione
   - Numero di corsi di programmazione già seguiti

5. Valuta e stampa:
   - Se l'età è minore di 18 anni, stampa "Utente minorenne".
   - Se l'età è tra 18 e 30 anni (inclusi), stampa "Utente giovane adulto".
   - Se l'età è sopra i 30 anni, stampa "Utente adulto".

6. Valuta combinazioni dei due altri numeri:
   - Se l'esperienza è almeno 5 anni E i corsi seguiti sono almeno 3, stampa "Utente esperto".
   - Se l'esperienza è meno di 5 anni O i corsi seguiti sono meno di 3, stampa "Utente in formazione".

7. Infine, se l'utente è "Utente esperto" E ha più di 25 anni, stampa anche "Profilo senior confermato".

Esempio:

input:
studente@istituto.it
Passw0rd!*
22
6
4

output:
Utente giovane adulto
Utente esperto
Profilo senior confermato

input:
studente@istituto.it
Passw0rd!*
17
2
1

output:
Utente minorenne
Utente in formazione

input:
studente@istituto.it
......
output:
Password errata

input:
user@esempio.com
Passw0rd!*

output:
Email non riconosciuta
"""
