
def est_majeur(age: int):
    if age <= 0:
        return False
    if age >= 18:
        return True
    return False


def recuperer_info_personne(numero_personne):
    nom_personne = input("Nom de la personne " + str(numero_personne) + ":")
    age_personne = input("Age de la personne " + str(numero_personne) + ":")
    return nom_personne, int(age_personne)

def afficher_infos_personne(numero_personne,nom, age: int):
    print("La personne ", numero_personne, "est", nom, "son age est", age, "ans")
    print("Le nom comporte", len(nom), "lettres")
    if est_majeur(age):
        print("Vous etes majeur")
    else:
        print("Vous etes mineur")


def recuperer_et_afficher_info( numero_personne):
    nom, age = recuperer_info_personne(numero_personne)
    afficher_infos_personne(numero_personne, nom, age)


nb_personnes = 3
for i in range(nb_personnes):
    recuperer_et_afficher_info(i + 1)



