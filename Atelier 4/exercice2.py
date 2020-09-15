
def mots_Nlettres(lst_mot:list, n:int)->list:
    taille = len(lst_mot)
    i = 0
    lst_final = []
    for i in range(taille):
        if(len(lst_mot[i]) == n):
            lst_final.append(lst_mot[i])

    return lst_final


def text_exercice1():
    lst_mot = ["jouer","bonjour","punir","jour","aurevoir","revoir","pouvoir","cour","abajour","finir","aimer"]
    return mots_Nlettres(lst_mot,5)
    
print(text_exercice1())