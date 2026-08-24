"""

1. Data una lista contenente dizionari, ognuno con le chiavi "nome" e "voti" (voti è una lista di interi),
calcola la media dei voti per ogni studente e
crea una nuova lista di tuple dove ogni tupla contiene il nome dello studente e la sua media.

2. Dalla lista di tuple ottenuta, crea un set con i nomi degli studenti che hanno una media superiore o uguale a 6.

3. Infine, crea un dizionario che abbia come chiave il nome dello studente e
come valore la lista ordinata dei suoi voti (in ordine crescente).

4. Stampa in maniera chiara:
- La lista di tuple con nome e media
- Il set degli studenti con media >= 6
- Il dizionario con voti ordinati

input:
students = [
  {"nome": "Anna", "voti": [7, 8, 6, 5]},
  {"nome": "Luca", "voti": [5, 4, 5, 6]},
  {"nome": "Marta", "voti": [9, 9, 10, 8]},
  {"nome": "Paolo", "voti": [6, 6, 6, 6]}
]

output:
Lista di tuple (nome, media): [('Anna', 6.5), ('Luca', 5.0), ('Marta', 9.0), ('Paolo', 6.0)]
Set di studenti con media >= 6: {'Anna', 'Marta', 'Paolo'}
Dizionario con voti ordinati:
Anna: [5, 6, 7, 8]
Luca: [4, 5, 5, 6]
Marta: [8, 9, 9, 10]
Paolo: [6, 6, 6, 6]

Esempio:

input:
students = [
  {"nome": "Giulia", "voti": [4,7,8]},
  {"nome": "Marco", "voti": [5,5,5]},
  {"nome": "Elena", "voti": [10,9,10]},
]

output:
Lista di tuple (nome, media): [('Giulia', 6.333333333333333), ('Marco', 5.0), ('Elena', 9.666666666666666)]
Set di studenti con media >= 6: {'Giulia', 'Elena'}
Dizionario con voti ordinati:
Giulia: [4, 7, 8]
Marco: [5, 5, 5]
Elena: [9, 10, 10]

"""
