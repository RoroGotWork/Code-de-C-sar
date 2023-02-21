phrase_correcte = False

while not(phrase_correcte):
    phrase_correcte = True
    phrase = input("Veuillez saisir une phrase : ")

    caractere_correctes = 0

    for caractere in phrase:
        for i in range(128):
            if chr(i) == caractere:
                caractere_correctes += 1
                break
    
    if caractere_correctes != len(phrase):
        phrase_correcte = False


decalage = 0

while not(decalage > 1 and decalage < 10):
    decalage = int(input("Veuillez saisir un nombre compris entre 1 et 9 : "))

lettre_minuscule = "abcdefghijklmnopqrstuvwxyz"
lettre_majuscule = lettre_minuscule.upper()
nombres = "0123456789"

nouvelle_phrase = ""

for caractere in phrase:
    nouveau_caractere = ''

    if caractere in lettre_minuscule:

        for i in range(len(lettre_minuscule)):
            if caractere == lettre_minuscule[i]:
                if i + decalage >= len(lettre_minuscule):
                    nouveau_caractere = lettre_minuscule[i + decalage - len(lettre_minuscule)]
                else:
                    nouveau_caractere = lettre_minuscule[i + decalage]
    
    elif caractere in lettre_majuscule:
        for i in range(len(lettre_majuscule)):
            if caractere == lettre_majuscule[i]:
                if i + decalage >= len(lettre_majuscule):
                    nouveau_caractere = lettre_majuscule[i + decalage - len(lettre_majuscule)]
                else:
                    nouveau_caractere = lettre_majuscule[i + decalage]
    
    elif caractere in nombres:
            if int(caractere) + decalage >= len(nombres):
                nouveau_caractere = str(int(caractere) + decalage - len(nombres))
            else:
                nouveau_caractere = str(int(caractere) + decalage)

    else:
        nouveau_caractere = caractere
    
    nouvelle_phrase += nouveau_caractere

print(f"Phrase avant le codage  :\"{phrase}\" ")
print(f"Valeur du décalage : {decalage}")
print(f"Phrase codée : \"{nouvelle_phrase}\"")
