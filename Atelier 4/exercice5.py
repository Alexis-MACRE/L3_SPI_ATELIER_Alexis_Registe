# Auteur(s) : MACRE Alexis & DJESSOU Registe
# Date : 20/09/2020
# Version : 1.0
# Description : Atelier de programmation 4 Exo 5 Python

from fonctions_persos import test_fonction

char_ouvrant = ['(','[','{']
char_fermant = [')',']','}']
char_operateurs = ['+','-','*','/','%','^']

def ouvrante(car:str)->bool:
     """Retourne True si le caractère en paramètre est un caractère ouvrant: ( ou [ ou { et False dans le cas contraire"""
     return (car in char_ouvrant)

def fermante(car:str)->bool:
     """Retourne True si le caractère en paramètre est un caractère fermante: ) ou ] ou } et False dans le cas contraire"""
     return (car in char_fermant)

def renverse(car:str)->str:
     """Transforme les caractères ouvrants en caractère fermants et vice-versa, retourne le caractère si il est normal"""
     if ouvrante(car):
          pos = char_ouvrant.index(car)
          car = char_fermant[pos]

     elif fermante(car):
          pos = char_fermant.index(car)
          car = char_ouvrant[pos]

     return car
     
def operateur(car:str)->bool:
     """Retourne True si le caractère en paramètre est un opérateur et False dans le cas contraire"""
     return (car in char_operateurs)

def nombre(car:str)->bool:
     """Retourne True si le caractère en paramètre est un nombre et False dans le cas contraire"""
     return car.isdigit()

def caractere_valide(car:str)->bool:
     """Retourne True si le caractère en paramètre un caractère ouvrant/fermant ou un operateur ou un nombre ou un espace
     et False dans le cas contraire"""
     valide = (ouvrante(car) or fermante(car) or operateur(car) or nombre(car) or car == ' ')

     return valide


def verif_parenthese(expression:str)->bool:
     """Retourne True si l'expression en paramètre a ses caractères ouvrants bien refermés et False dans le cas contraire"""
     liste_ouvrants = []
     liste_fermants = []
     valide = False

     for char in expression:
          if ouvrante(char):
               liste_ouvrants+=char
          if fermante(char):
               liste_fermants.insert(0,renverse(char))

     if liste_ouvrants == liste_fermants:
          valide = True

     return valide


#test_fonction(ouvrante,["(","{","+","-"," ","270","ç","}","}"],[True,True,False,False,False,False,False,False,False])
#test_fonction(fermante,["(","{","+","-"," ","270","ç","}","}"],[False,False,False,False,False,False,False,True,True])
#test_fonction(operateur,["(","{","+","-"," ","270","ç","}","}"],[False,False,True,True,False,False,False,False,False])
#test_fonction(nombre,["(","{","+","-"," ","270","ç","}","}"],[False,False,False,False,False,True,False,False,False])
#test_fonction(caractere_valide,["(","{","+","-"," ","270","ç","}","}"],[True,True,True,True,True,True,False,True,True])
#test_fonction(renverse,["}","]",")","(","[","{","a","b"],["{","[","(",")","]","}","a","b"])
#test_fonction(verif_parenthese,["ax2+(b*c)","[(a+b)2","{7+[2*(1+1)]}^2"],[True,False,True])