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
poser_question(" Quelle est la capitale du Maroc ?", "Marakech", "Meknès", "Rabat", "Oujda", "c")

print("Score final :", score)
