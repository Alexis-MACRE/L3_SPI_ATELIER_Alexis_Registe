# Auteur(s) : MACRE Alexis & DJESSOU Registe
# Date : 20/09/2020
# Version : 1.0
# Description : Atelier de programmation 4 Exo 4 Python

from fonctions_persos import test_fonction
from exercice2 import mots_Nlettres
from exercice3 import dictionnaire

def mot_correspond(mot:str,motif:str)->bool:
     test_mot = list(mot)
     longueur_mot = len(mot)

     correspond = False

     if len(motif)==longueur_mot:
          for i in range(longueur_mot):
               if motif[i]==".":
                    test_mot[i]="."
          if test_mot == list(motif):
               correspond = True
     
     
     return correspond

def presente(lettre:str,mot:str)->int:
     return mot.find(lettre)


def nombre_apparitions(char:str,mot:str)->int:
          
          compteur = 0

          for lettre in mot:
               if lettre == char:
                    compteur+=1

          return compteur   


def mot_possible(mot:str,lettres:str)->bool:
     
     possible = False
     compteur = 0

     for lettre in mot:
          if presente(lettre,lettres)!=-1 and nombre_apparitions(lettre,mot)<=nombre_apparitions(lettre,lettres):
               compteur+=1
          
     if compteur == len(mot):
          possible = True
     
     return possible

def mot_optimaux(dico:list,lettres:str)->list:
     liste_longueur_max = []
     liste_possible = []

     record_longueur=0

     for i in range(len(lettres)+1):
          liste_longueur_max+=mots_Nlettres(dico,i)
     
     for mot in liste_longueur_max:
          if mot_possible(mot,lettres):
               liste_possible+=[mot]
               record_longueur = max(record_longueur,len(mot))
     
     return mots_Nlettres(liste_possible,record_longueur)
          


dico = dictionnaire("littre.txt")

print(mot_optimaux(dico,"chapeauoptty"))

#test_fonction(mot_correspond,[["salut","s..u."],["mauvais","..m.."]],[True,False],2)
#test_fonction(presente,[["t","salut"],["m","mauvais"]],[4,0],2)
#test_fonction(nombre_apparitions,[["a","ananas"],["a","palace"],["a","pile"]],[3,2,0],2)
#test_fonction(mot_possible,[["salut","asultazre"],["mauvais","oopipok"],["chapeau","chapeu"],["chapeau","uaepahc"]],[True,False,False,True],2)
