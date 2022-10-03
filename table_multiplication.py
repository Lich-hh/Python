# table multiplication

def afficher_table_multiplication(n, min=1, max=10):
    if min > max:
        print(" ERREUR : le minimum est supérieur au maximum ! ")
        return

    for i in range(min, max + 1):
        print(i, "x", n, "=", i*n)


afficher_table_multiplication(5, 7, 2)



