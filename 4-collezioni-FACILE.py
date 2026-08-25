"""
1. Crea una lista di cinque nomi di tuoi amici e stampala.
2. Modifica il terzo nome nella lista con un altro nome a tua scelta e mostra la lista aggiornata.
3. Crea una tupla con tre numeri interi a tua scelta e stampala.
4. Prova a modificare un elemento della tupla (anche se non è permesso) e osserva cosa succede.
5. Crea un set contenente i seguenti elementi: 1, 2, 2, 3, 3, 3, 4. Stampa il set e osserva come i duplicati sono stati rimossi automaticamente.
6. Aggiungi un elemento (ad esempio 5) al set e stampalo nuovamente.
7. Crea un dizionario che rappresenti una semplice rubrica telefonica: le chiavi sono i nomi delle persone, i valori i loro numeri di telefono (come stringhe).
8. Aggiungi una nuova persona con relativo numero al dizionario.
9. Modifica il numero di telefono di una persona già presente.
10. Stampa le chiavi (nomi) e i valori (numeri) del dizionario usando metodi appositi.

Esempio:

1. ['Luca', 'Marco', 'Anna', 'Giulia', 'Sara']
2. ['Luca', 'Marco', 'Francesca', 'Giulia', 'Sara']
3. (1, 5, 9)
4. (TypeError o errore di tipo modificando tupla)
5. {1, 2, 3, 4}
6. {1, 2, 3, 4, 5}
7. {'Luca': '1234567890', 'Marco': '0987654321'}
8. {'Luca': '1234567890', 'Marco': '1112223333', 'Anna': '5556667777'}
9. Chiavi: ['Luca', 'Marco', 'Anna']
10. Valori: ['1234567890', '1112223333', '5556667777']

"""
amici = ["Elio", "Manlio", "Giorgio", "Gabriele", "Davide"]
print(amici)
amici[2] = "Daniele"
print(amici)
eta_ragazzi = (19, 18, 30)
#eta_ragazzi[2]= 15
print(eta_ragazzi)
ordine_grandezza ={1, 2, 2, 3, 3, 3, 4}
print(ordine_grandezza)
ordine_grandezza.add(5)
print(ordine_grandezza)
amiconi ={
    "Elio": 3045033309,
    "Manlio": 3021034420, 
}
amiconi["Gabriele"] = 301604993
amiconi["Manlio"] = 993221667
print(list(amiconi.keys()))
print(list(amiconi.values()))