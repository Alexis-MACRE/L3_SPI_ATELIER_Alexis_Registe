# Auteur(s) : MACRE Alexis & DJESSOU Registe
# Date : 15/09/2020
# Version : 1.0
# Description : Atelier de programmation 4 Exo 1 Python

from fonctions_persos import test_fonction

def full_name (str_arg:str)->str:
    """Prends une chaine "nom prenom" et la formate en "NOM Prenom"
    
    Arguments:
    str_arg -- la chaine "non prenom"
    
    Retourne la chaine formatée
    """   
    chaine_separee = str_arg.split()
    nom = chaine_separee[0]
    prenom = chaine_separee[1]
    nom = nom.upper()
    prenom = prenom.capitalize()
    
    str_arg = nom + " " + prenom
    
    return str_arg

def is_mail(str_arg:str)->(int,int):
     """Fonction de test de validité d'une adresse mail sous le format xxxxxx@univ-corse.fr
     
     Arguments:
     str_arg -- la chaine de caractère à tester
     
     Retourne le couple (validité de l'adresse, code d'erreur)
     """
     erreur = 0

     position_arobase = str_arg.find("@")

     position_espace = str_arg.find(" ")

     domaine_avec_point = str_arg.split("@")

     if(len(domaine_avec_point)>=2):
          domaine_avec_point = domaine_avec_point[1]
          domaine = domaine_avec_point.split(".")[0]
     else:
          domaine = ""

     if position_arobase==0 or (position_espace>=0 and position_espace<position_arobase):
          erreur = 1

     elif position_arobase==-1:
          erreur = 2

     elif domaine_avec_point.find(".")==-1:
          erreur = 4

     elif domaine != "univ-corse":
          erreur = 3


     validite = (erreur==0)

     return (validite,erreur)


def message_erreur_exo1(code_erreur:int)->str:
     """Fonction qui retourne le message d'erreur correspondant au code d'erreur"""
     message_erreur = ["le mail est valide", "le corps n'est pas valide","il manque l'arobase","le domaine n'est pas valide","il manque le point après le domaine"]
     return message_erreur[code_erreur]

#test_fonction(full_name,["aa bb","cc dd"],["AA Bb","CC Dd"])
#test_fonction(is_mail,["a aa@univ-corse.fr","aaaaauniv-corse.fr","aaaaaa@gmail.com","aaaa@univ-corsefr","valide@univ-corse.fr"],[(0,1),(0,2),(0,3),(0,4),(1,0)],2)

#retour = is_mail("aaa@univ-corse.fr")

#print(message_erreur_exo1(retour[1]))