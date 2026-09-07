# Risultato atteso:
#   La funzione "cifra_cesare" deve cifrare una stringa
#   spostando ogni lettera di "shift" posizioni nell'alfabeto
#   (cifrario di Cesare). Le lettere maiuscole restano maiuscole,
#   le minuscole restano minuscole. I caratteri non alfabetici
#   (spazi, punteggiatura) restano invariati.
#   Esempio:
#       cifra_cesare("abc", 3)    → "def"
#       cifra_cesare("xyz", 3)    → "abc"   (ritorna dall'inizio)
#       cifra_cesare("Hello!", 3) → "Khoor!"
#       cifra_cesare("ABC", 1)    → "BCD"

def cifra_cesare(testo, shift):
    risultato = ""
    for ch in testo:
        if ch.isalpha():
            base = ord("a") if ch.islower() else ord("A")
            risultato += chr((ord(ch) + shift - base) % 26 + base)
        else:
            risultato += ch
    return risultato


def decifra_cesare(testo, shift):
    return cifra_cesare(testo, shift)


print(cifra_cesare("abc", 3))
print(cifra_cesare("xyz", 3))
print(cifra_cesare("Hello!", 3))
cifrato = cifra_cesare("Messaggio segreto", 7)
print(cifrato)
print(decifra_cesare(cifrato, 7))