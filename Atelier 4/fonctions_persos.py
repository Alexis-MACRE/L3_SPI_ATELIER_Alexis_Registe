# Auteur(s) : MACRE Alexis
# Date : 21/09/2020
# Version : 3.0
# Description : Fonction pour tester une fonction donnée


def test_fonction(fonction:callable,valeurs:list,valeurs_attendues:list,nb_param:int=1,affichage_variable:bool=True) -> None :
     """Fonction qui permet de tester une fonction pour chacune des valeurs passées en paramètre.
     Elle compare les valeurs que la fonction retourne à celles qui sont attendues, puis affiche les résultats du test.
     Obligation de préciser le nombre de paramètres de la fonction testée quand ils sont >=2.
     Possibilité de désactiver l'affichage des valeurs d'entrées, dans le cas par exemple où cette dernière est très 
     volumineuse (comme une liste de 15000 mots)
     
     Arguments:
     fonction            -- la fonction à tester
     valeurs             -- liste des paramètres en entrée pour chacun des tests
     valeurs_attendues   -- liste des valeurs de retour attendues
     nb_param            -- nombre de paramètres de la fonction, par défaut = 1
     affichage           -- affichage ou non de la valeur en entrée
     """

     for i in range(len(valeurs)):                                              

          if nb_param == 1:
               resultat = fonction(valeurs[i]) 


          elif nb_param == 2:
               
               resultat = fonction(valeurs[i][0],valeurs[i][1])


          elif nb_param == 3:
               resultat = fonction(valeurs[i][0],valeurs[i][1],valeurs[i][2])


          elif nb_param == 4:
               resultat = fonction(valeurs[i][0],valeurs[i][1],valeurs[i][2],valeurs[i][3])


          if resultat!=valeurs_attendues[i]:
               if affichage_variable:
                    print("Test pour",valeurs[i],": Resultat Incorrect",resultat,"au lieu de",valeurs_attendues[i])
               else:
                    print("Test numero",i,": Resultat Incorrect",resultat,"au lieu de",valeurs_attendues[i])
          else:
               if affichage_variable:
                    print("Test pour",valeurs[i],": Resultat Correct",resultat)
               else:
                    print("Test numero",i,": Resultat Correct",resultat) 



# import sys
# sys.path.append('../L3')
# import testfonction