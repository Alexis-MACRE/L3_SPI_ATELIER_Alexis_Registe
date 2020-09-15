from fonctions_persos import test_fonction
from random import randint

def placesLettre(char:str,mot:str)->list:
     liste_index = []
     for i in range(len(mot)):
          if mot[i] == char:
               liste_index.append(i)     

     return liste_index

def outputStr(mot:str)->str:
     output = "' "  +  "_ "*len(mot)  +  "'"
     return output

def dictionnaire(fichier:str):
    mon_fichier = open(fichier, 'r', encoding='utf8')
    liste_lignes = mon_fichier.readlines()
    return [ligne.strip("\n") for ligne in liste_lignes]

def runGame():
     liste_dico = dictionnaire("littre.txt")
     mon_dictionnaire = { mot : len(mot) for mot in liste_dico }

     nombre_random = randint(0,len(mon_dictionnaire))

     mot_random = liste_dico[nombre_random]

     liste_chara = list(outputStr(mot_random))
     i=0

     while i<5:
          lettre_choisie = input("Veillez rentrer une lettre: ")

          index_apparitions = placesLettre(lettre_choisie,mot_random)     

          for emplacements in index_apparitions:
               test = 2+2*emplacements
               liste_chara[test] = lettre_choisie
          
          mot_affiche = "".join(liste_chara)

          print(mot_affiche)
          i+=1

runGame()
#test_fonction(placesLettre,[["a","apparaître"]],[[0,3,5]],2)