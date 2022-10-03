"""
Consigne Projet questionnaire :

Question : Quelle est la capitale de la France ?
(a) Marseille
(b) Nice
(c) Paris
(d) Nantes

Votre réponse :
Bonne réponse / Mauvaise réponse


.....
Capitale de l'Italie ?
....
4 Questions




"""
"""def reponse_client_france():


    a = "Marseille"
    b = "Nice"
    c = "Paris"
    d = "Nantes"

    reponse = input(" Quelle est la capitale de la France :  a = " + a +  " b = " + b + " c = " + c + " d= " + d)
    if reponse == "c":
        print(" Bonne réponse ")
    else:
        print(" Mauvaise reposne ! ")

def reponse_client_italie():


    a = "Venise"
    b = "Rome"
    c = "Milan"
    d = "Napoli"

    reponse = input(" Quelle est la capitale de l'Italie :  a = " + a +  " b = " + b + " c = " + c + " d= " + d)
    if reponse == "b":
        print(" Bonne réponse ")
    else:
        print(" Mauvaise reposne ! ")


def reponse_client_maroc():


    a = "Marakech"
    b = "Mèknes"
    c = "Oujda"
    d = "Rabbat"

    reponse = input(" Quelle est la capitale du Maroc :  a = " + a +  " b = " + b + " c = " + c + " d= " + d)
    if reponse == "d":
        print(" Bonne réponse ")
    else:
        print(" Mauvaise reposne ! ")

def reponse_client_espagne():


    a = "Barcelone"
    b = "Madrid"
    c = "Bilbao"
    d = "Séville"

    reponse = input(" Quelle est la capitale du Maroc :  a = " + a +  " b = " + b + " c = " + c + " d= " + d)
    if reponse == "b":
        print(" Bonne réponse ")
    else:
        print(" Mauvaise reposne ! ")"""


def poser_question(question, r1, r2, r3, r4, choix_bonne_reponse):
    global score
    print(   "Question : ", question  )
    print(" (a)  ", r1)
    print(" (b)  ", r2)
    print(" (c)  ", r3)
    print(" (d)  ", r4)
    print()
    reponse = input(" Votre reponse : ")


    if reponse == choix_bonne_reponse:
        print("Bonne réponse ! ")
        score += 1
    else:
        print("Mauvaise réponse ! ")




score = 0
poser_question(" Quelle est la capitale de la France ?", "Marseille", " Nice", " Paris", " Nantes", "c")
poser_question(" Quelle est la capitale de L'Italie ?", " Rome", " Venise", " Turin", " Napoli", "a")

print("Score final :", score)