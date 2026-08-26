"""
In questo esercizio dovrai creare gerarchie annidate e operare conversioni tra collezioni per simulare una gestione complessa di informazioni.

1. Definisci una lista annidata chiamata `orario_settimanale` che rappresenti l'orario di 5 giorni (dal lunedì al venerdì) di una classe scolastica.
Ogni giorno è una lista di 6 ore.
Inserisci almeno 4 materie differenti (ad esempio: "matematica", "italiano", "storia", "inglese")
distribuite nei giorni e ore in modo arbitrario.

2. Definisci una tupla `docenti` con almeno 5 nomi di docenti,
alcuni dei quali ripetuti (es. "Rossi", "Verdi", "Bianchi", "Rossi", "Neri").

3. Definisci un set `materie_set` contenente le materie senza duplicati,
ricavandolo dalla lista annidata `orario_settimanale` (devi estrarre le materie da tutte le sottoliste).

4. Crea un dizionario `docente_per_materia` che associa ogni materia ad uno dei docenti
(assegna arbitrariamente, scegliendo 4 docenti dalla tupla).

5. Stampa, per ogni giorno (lunedì, martedì, ..., venerdì), la lista delle materie con i relativi docenti.

6. Aggiungi una funzione che,
dato un nome di docente, restituisce in stampa tutti i giorni e le ore in cui quel docente insegna,
indicando materia, giorno e ora.

Esempio:
    
input:
(orario_settimanale è inserito nel codice, non richiesto in input)
docenti = ("Rossi", "Verdi", "Bianchi", "Rossi", "Neri")
docente_per_materia = {"matematica": "Rossi", "italiano": "Verdi", "storia": "Bianchi", "inglese": "Neri"}

richiesta: stampa giornaliera del lunedì e mercoledì

output:
Lunedì: matematica (Rossi), italiano (Verdi), storia (Bianchi), inglese (Neri), matematica (Rossi), italiano (Verdi)
Mercoledì: inglese (Neri), storia (Bianchi), matematica (Rossi), italiano (Verdi), inglese (Neri), storia (Bianchi)

input:
richiesta: docente "Rossi"

output:
Rossi insegna:
- Lunedì ora 0: matematica
- Lunedì ora 4: matematica
- Mercoledì ora 2: matematica

input:
richiesta: docente "Verdi"

output:
Verdi insegna:
- Lunedì ora 1: italiano
- Lunedì ora 5: italiano
- Martedì ora 0: italiano
- Mercoledì ora 3: italiano
"""