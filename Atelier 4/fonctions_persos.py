# import sys
# sys.path.append('../L3')
# import testfonction

def test_fonction(fonction:callable,valeurs:list,valeurs_attendues:list,nb_param:int=1) -> None :
     """Permet de tester une fonction avec une liste de valeurs et celle des resultats attendus"""

     for i in range(len(valeurs)) :
          if nb_param == 1:
               if fonction(valeurs[i])!=valeurs_attendues[i]:
                    print("Test pour",valeurs[i],": Resultat Incorrect",fonction(valeurs[i]),"au lieu de",valeurs_attendues[i])
               else:
                    print("Test pour",valeurs[i],": Resultat Correct",fonction(valeurs[i]))

          elif nb_param == 2:
               if fonction(valeurs[i][0],valeurs[i][1])!=valeurs_attendues[i]:
                    print("Test pour",valeurs[i],": Resultat Incorrect",fonction(valeurs[i][0],valeurs[i][1]),"au lieu de",valeurs_attendues[i])
               else:
                    print("Test pour",valeurs[i],": Resultat Correct",fonction(valeurs[i][0],valeurs[i][1]))
          
          elif nb_param == 3:
               if fonction(valeurs[i][0],valeurs[i][1],valeurs[i][2])!=valeurs_attendues[i]:
                    print("Test pour",valeurs[i],": Resultat Incorrect",fonction(valeurs[i][0],valeurs[i][1],valeurs[i][2]),"au lieu de",valeurs_attendues[i])
               else:
                    print("Test pour",valeurs[i],": Resultat Correct",fonction(valeurs[i][0],valeurs[i][1],valeurs[i][2]))

          elif nb_param == 4:
               if fonction(valeurs[i][0],valeurs[i][1],valeurs[i][2],valeurs[i][3])!=valeurs_attendues[i]:
                    print("Test pour",valeurs[i],": Resultat Incorrect",fonction(valeurs[i][0],valeurs[i][1],valeurs[i][2],valeurs[i][3]),"au lieu de",valeurs_attendues[i])
               else:
                    print("Test pour",valeurs[i],": Resultat Correct",fonction(valeurs[i][0],valeurs[i][1],valeurs[i][2],valeurs[i][3]))