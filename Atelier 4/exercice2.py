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

def commence_par(mot:str,prefixe:str)->bool:
    return (mot.find(prefixe) == 0)

def finit_par(mot:str,suffixe:str)->bool:
    index_suffixe = len(mot) - len(suffixe)
    return (mot.rfind(suffixe) == index_suffixe)

def finissent_par(lst_mot:str,suffixe:str)->list:
    liste_retour = []
    for mot in lst_mot:
        if finit_par(mot,suffixe):
            liste_retour.append(mot)
    
    return liste_retour

def commencent_par(lst_mot:str,prefixe:str)->list:
    liste_retour = []
    for mot in lst_mot:
        if commence_par(mot,prefixe):
            liste_retour.append(mot)
    
    return liste_retour


def liste_mots(lst_mot:str,prefixe:str,suffixe:str,n:int)->list:
    liste_commencent = commencent_par(lst_mot,prefixe)
    liste_finissent = finissent_par(liste_commencent,suffixe)
    liste_retour = mots_Nlettres(liste_finissent,n)

    return liste_retour

def dictionnaire(fichier:str):
    mon_fichier = open(fichier, 'r', encoding='utf8')
    liste_lignes = mon_fichier.readlines()
    return [ligne.strip("\n") for ligne in liste_lignes]

#print(liste_mots(["jouer","bonjour","punir","jour","aurevoir","revoir","pouvoir","cour","abajour","finir","aimer"],"a","r",8))