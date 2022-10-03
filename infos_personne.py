
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



"""nom1= input("Nom de la personne 1 : ")
age1 = input( "Age de la personne 1 : ")
print(" La personne 1 est " + nom1 + " et son age est : " + age1 + " ans ")


nom2 = input("Nom de la personne 2 : ")
age2 = input( "Age de la personne 2 : ")
print(" La personne 2 est " + nom2 + " et son age est : " + age2 + " ans ")
print(" Le nom de la personne comporte ", len(nom2) , " lettre ")"""


"""def affiche_info_personne(nom="", age=0):
    if nom == "":
        print("Pas de nom rentré", "l'age vaut ", age)
        return
    if age == 0:
        print("Vous n'avez pas donné d'age ")
        return
    if age == 0:
        print (" Le prenom est ", nom)
    else:
         print(" Bonjour", nom + " tu as : ", age , "ans")
    print("Le mot comporte", len(nom), "caractère ")
    if est_majeur(age):
        print("Il est majeur")
    else:
        print("Il est mineur ")


age = 18


if age == 0:
    exit(255)

    print("La personne a", age, "ans")
    majeur_ou_non = est_majeur(age)
    if majeur_ou_non:
        print("Il est majeur")
    else:
        print( "Il est mineur ") """
