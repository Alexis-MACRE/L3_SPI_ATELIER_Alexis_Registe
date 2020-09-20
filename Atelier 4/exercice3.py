from fonctions_persos import test_fonction
from random import randint

LONGUEUR_MOT_MINIMUM = 3
LONGUEUR_MOT_MAXIMUM = 23

def placesLettre(char:str,mot:str)->list:
     """Fonction qui indique la liste des positions de la lettre char dans le string mot.
     
     Arguments:
     char -- la lettre que le joueur a rentré
     mot -- mot dans lequel on souhait connaître la présence la lettre char
     
     Retourne la liste finale, si jamais la lettre n'était pas dans le mot, alors on retourne une liste vide.
     """
     liste_index = []
     for i in range(len(mot)):
          if mot[i] == char:
               liste_index.append(i)     

     return liste_index

def outputStr(mot:str,lpos:list)->str:
     """Transforme un mot donné en sa version pendu ex: salut -> ' _ _ _ _ _ '
     Si le joueur a déjà trouvé des lettres, alors on les affiche à leurs emplacements.
     Note: On ne peut pas modifier les lettres d'un string une à une, on est obligé de
     le transformer d'abord en liste, d'où la variable "liste_cara"
     
     Arguments:
     mot -- le mot utilisé lors du jeu
     lpos -- liste des positions des lettres que le joueur à trouvé

     Retourne le string version pendu à afficher.
     """
     liste_cara = list("' "  +  "_ "*len(mot)  +  "'")

     for position in lpos:
          liste_cara[2+2*position] = mot[position]

     output = "".join(liste_cara)

     return output

def dictionnaire(fichier:str)->list:
    """Transforme un fichier donné en un tableau de str qui correspondent à chacune des lignes. 
    Note: Le fichier doit être dans le même dossier que ce code

    Arguments:
    fichier -- nom du fichier à ouvrir

    Retourne la liste de str.
    """
    mon_fichier = open(fichier, 'r', encoding='utf8')
    liste_lignes = mon_fichier.readlines()
    return [ligne.strip("\n") for ligne in liste_lignes]


def bonhomme_pendu(nombre_erreurs:int)->str:
     """Fonction qui prend le nombre d'erreurs et qui retourne le str correspondant au pendu à afficher.
     
     Arguments:
     nombre_erreurs -- nombre d'erreurs que le joueur à commise
     
     Retourne le str à afficher.
     """
     affichage = [""]
     affichage.append("\n\n\n\n________")
     affichage.append("\n  |\n  |\n  |\n__|_____")
     affichage.append("-----------\n  |\n  |\n  |\n__|_____")
     affichage.append("-----------\n  |     |\n  |\n  |\n__|_____")
     affichage.append("-----------\n  |     |\n  |     o\n  |   --O--\n__|____/ \\")
     
     return affichage[nombre_erreurs]

def build_dict(lst:list)->dict:
     """Transforme une liste de mots en un dictionnaire qui regroupe tous les mots par leurs nombre de lettres.
     longueur : liste_de_mots_de_cette_longueur
     
     Arguments:
     lst -- liste de mots
     
     Retourne le dictionnaire rangé.
     """

     dictionnaire_retour = { i : [] for i in range(LONGUEUR_MOT_MINIMUM,LONGUEUR_MOT_MAXIMUM+1)}
     
     for mot in lst:
          liste_mot = dictionnaire_retour[len(mot)]
          liste_mot += [mot]
          dictionnaire_retour[len(mot)] = liste_mot

     return dictionnaire_retour

def selec_word(sorted_words:dict,word_len:int)->str:
     """Prend le dictionnaire trié par longueur et choisi un mot au hasard de la longueur word_len.
     
     Arguments:
     sorted_words -- dictionnaire trié par longueur de mot retourné par la fonction build_dict
     word_len -- longueur du mot que l'on souhaite tirer
     
     Retourne le mot de longueur word_len choisi aléatoirement
     """
     nombre_random = randint(0,len(sorted_words[word_len])-1)
     mot_random = sorted_words[word_len][nombre_random]

     return mot_random

def runGame():
     """Programme principal du jeu du pendu"""

     MIN_FACILE = LONGUEUR_MOT_MINIMUM
     MAX_FACILE = 7

     MIN_NORMAL = 6
     MAX_NORMAL = 9

     MIN_DIFFICILE = 8
     MAX_DIFFICILE = LONGUEUR_MOT_MAXIMUM

     liste_dico = dictionnaire("littre.txt")
     mon_dictionnaire = build_dict(liste_dico)
     liste_random = []

     difficulte = input("Veillez sélectionner la difficulté (E / N / H) : ")

     if difficulte == "E" or difficulte == "e":
          borne_min = MIN_FACILE
          borne_max = MAX_FACILE

     elif difficulte == "N" or difficulte == "n":
          borne_min = MIN_NORMAL
          borne_max = MAX_NORMAL
     
     else:
          borne_min = MIN_DIFFICILE
          borne_max = MAX_DIFFICILE

     for i in range(borne_min,borne_max):
          liste_random += [selec_word(mon_dictionnaire,i)]
     chiffre_random = randint(0,len(liste_random)-1)

     mot_random = liste_random[chiffre_random]     
     nombre_erreurs=0
     index_apparitions = []
     lettre_sauvegarde = []

     print(outputStr(mot_random,index_apparitions),"\n")

     while nombre_erreurs<5 and len(index_apparitions)!=len(mot_random):
          lettre_choisie = input("Veillez rentrer une lettre: ")

          if placesLettre(lettre_choisie,mot_random)==[] or (lettre_choisie in lettre_sauvegarde):
               nombre_erreurs+=1
          else:
               index_apparitions+=placesLettre(lettre_choisie,mot_random) 

          mot_affiche = outputStr(mot_random,index_apparitions)

          lettre_sauvegarde.append(lettre_choisie)

          print(mot_affiche)
          print(bonhomme_pendu(nombre_erreurs))
          print("\nNombre d'erreurs :",nombre_erreurs,"\n")
     
     if(nombre_erreurs!=5):
          print("Gagné ! Vous avez bien trouvé le mot",mot_random)
     else:
          print("Perdu ! le mot était",mot_random)


runGame()


#test_fonction(placesLettre,[["a","apparaître"]],[[0,3,5]],2)

#test_fonction(outputStr,[["salut",[0]]],["' s _ _ _ _ '"],2)

#print(build_dict(["motdeneuf","autreneuf","sixlet","letsix"]))
#liste_dico = dictionnaire("littre.txt")
#mon_dictionnaire = { len(mot) : (list(mon_dictionnaire[len(mot)])+[mot]) for mot in liste_dico }