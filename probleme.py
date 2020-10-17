# 1 / ON IMPORTE LE MODULE random AVEC UN ALIAS => rd
import random as rd


# FONCTION DU NOMBRE D'ENFANTS
def nb_enfant(): 

   # ON DEFINIT LE RESULTAT DU NOMBRE D'ENFANTS
   # SOUS FORME D 'UNE VARIABLE A ZERO
   nb_enfants = int()

   a = round(rd.random() * 100)

   # ON RECREE LE DIAGRAMME
   # ET DETERMINE EN UTILISANT LA CONDITION SUIVANTE

   if 0 <= a <= 6.3:
      nb_enfants = 0

   elif 6.3 < a <= 49.6:
      nb_enfants = 1

   elif 49.6 < a <= 84.1:
      nb_enfants = 2

   elif 84.1 < a <= 96:
      nb_enfants = 3

   else:
      nb_enfants = 4

   return nb_enfants 


# NOMBRE ALEATOIRE DE GARCONS(fonction)
def garcon_aleat():

   # NOMBRE DE GARCONS   
   result = int()

   # LE POURCENTAGE D 'AVOIR UN GARCON 
   pourcentage_garcon = 52.5

   # ON RAPPEL LA FONCTION POUR AVOIR LE NOMBRE D'ENFANTS
   enfants = nb_enfant()

   # POUR CHAQUE ENFANT VOIR SI C 'EST UN GARCON
   for x in range(0, enfants):
      if round(rd.random() * 100) < pourcentage_garcon:
         
         result += 1

   return result


def end_generation(): 
   
   nb_garcons = 0
   
   # ON COMMENCE AVEC 2 PARENTS (EXEMPLE - PERES)
   nb_parents = 2

   # ON INITIALISE LE NOMBRE DE GENERATIONS
   nb_generations = 0

   # TANT QU'IL Y A DES PARENTS (PERE)
   while nb_parents != 0:
       
       nb_garcons = 0

       #ON GENERE LE NOMBRE DE GARCONS SELON LE CONTEXTE
       for x in range(0,nb_parents):
           nb_garcons = nb_garcons + garcon_aleat()
           
       nb_generations += 1

       #LES GARCONS DEVIENNENT DES PARENTS (PERE)
       nb_parents = nb_garcons

   return nb_generations     

# MOYENNE GENERATIONS
def moyenne_generation(): 

   somme = 0
   moyenne = 0

   for x in range(0, 100000): 
      somme = somme + end_generation()

   moyenne = somme / 100000

   return "La moyenne des generations est de : " + str(round(moyenne))

#DEBUG
# print(end_generation())
# print(garcon_aleat())
# print(moyenne_generation())
# print(nb_enfant())
