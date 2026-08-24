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
nomi = ['Vito', 'Alessio', 'Anna', 'Maria', 'Sara']
print(nomi)

nomi[2]="Filippo"
print(nomi)


tupla_strana=(1,2,3)
print(tupla_strana)

"""
tupla_strana[2]=5
print(tupla_strana)

"""

elementi = {1, 2, 2, 3, 3, 3, 4}
print(elementi)

elementi.add(5)
print(elementi)

rubrica ={
 "Paolo": "393270555",
 "Vincenzo":"393370555"
}
print(rubrica)


rubrica["Mauro"]="393370599"
print(rubrica)

"""
rubrica.pop("Mauro")
print(rubrica)

"""

rubrica["Mauro"]="666"
print(rubrica)

listaC=rubrica.keys()

print(list(rubrica.values()))
print(list(listaC))