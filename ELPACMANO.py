import random
import time
from re import A
import tkinter as tk
from tkinter import font  as tkfont
import numpy as np
from sounds import SoundManagement
s = SoundManagement()

##########################################################################
#
#   Partie I : variables du jeu  -  placez votre code dans cette section
#
#########################################################################

# Plan du labyrinthe

# 0 vide
# 1 mur
# 2 maison des fantomes (ils peuvent circuler mais pas pacman)

def CreateArray(L):
   T = np.array(L,dtype=np.int32)
   T = T.transpose()  ## ainsi, on peut écrire TBL[x][y]
   return T

TBL = CreateArray([
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
        [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,1,0,1,1,0,0,1,1,0,1,1,0,1,0,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
        [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ]);

HAUTEUR = TBL.shape [1]
LARGEUR = TBL.shape [0]



# grille determinant si il y a un couloir ou non
TBL_corridor = CreateArray([
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,2,2,0,1,0,2,2,2,2,2,2,0,1,0,2,2,0,1],
        [1,2,1,1,2,1,2,1,1,1,1,1,1,2,1,2,1,1,2,1],
        [1,2,1,0,0,2,0,2,2,0,0,2,2,0,2,0,0,1,2,1],
        [1,2,1,2,1,1,2,1,1,0,0,1,1,2,1,1,2,1,2,1],
        [1,0,2,0,2,2,0,1,0,0,0,0,1,0,2,2,0,2,0,1],
        [1,2,1,2,1,1,2,1,1,1,1,1,1,2,1,1,2,1,2,1],
        [1,2,1,0,0,2,0,2,2,2,2,2,2,0,2,0,0,1,2,1],
        [1,2,1,1,2,1,2,1,1,1,1,1,1,2,1,2,1,1,2,1],
        [1,0,2,2,0,1,0,2,2,2,2,2,2,0,1,0,2,2,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ]);

MUR=1000
CHE=220
GHO=2000

#grille des distance pour les fantomes
Grille_Fantome = CreateArray([
        [MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR],
        [MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR],
        [MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR,MUR,GHO,GHO,MUR,MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR],
        [MUR,CHE,CHE,CHE,CHE,CHE,CHE,MUR,GHO,GHO,GHO,GHO,MUR,CHE,CHE,CHE,CHE,CHE,CHE,MUR],
        [MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR],
        [MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR],
        [MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR]]);

#grille des distance pour les pacgums
Grille_Distance = CreateArray([
        [MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR],
        [MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR],
        [MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR,MUR,GHO,GHO,MUR,MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR],
        [MUR,CHE,CHE,CHE,CHE,CHE,CHE,MUR,GHO,GHO,GHO,GHO,MUR,CHE,CHE,CHE,CHE,CHE,CHE,MUR],
        [MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR],
        [MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR],
        [MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR]]);

Grille_Blinky = CreateArray([
        [MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR],
        [MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR],
        [MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR,MUR,CHE,CHE,MUR,MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR],
        [MUR,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,MUR],
        [MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR],
        [MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR],
        [MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR]]);

Grille_Pinky = CreateArray([
        [MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR],
        [MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR],
        [MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR,MUR,CHE,CHE,MUR,MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR],
        [MUR,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,MUR],
        [MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR],
        [MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR],
        [MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR]]);

Grille_Inky = CreateArray([
        [MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR],
        [MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR],
        [MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR,MUR,CHE,CHE,MUR,MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR],
        [MUR,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,MUR],
        [MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR],
        [MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR],
        [MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR] ]);

Grille_Clyde = CreateArray([
        [MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR],
        [MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR],
        [MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR,MUR,CHE,CHE,MUR,MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR],
        [MUR,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,MUR],
        [MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR],
        [MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR],
        [MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR] ]);

Grille_Clyde_distancePacMan = CreateArray([
        [MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR],
        [MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR],
        [MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR,MUR,CHE,CHE,MUR,MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR],
        [MUR,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,MUR],
        [MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,MUR],
        [MUR,CHE,MUR,MUR,CHE,MUR,CHE,MUR,MUR,MUR,MUR,MUR,MUR,CHE,MUR,CHE,MUR,MUR,CHE,MUR],
        [MUR,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,CHE,CHE,CHE,CHE,MUR,CHE,CHE,CHE,CHE,MUR],
        [MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR,MUR] ]);



LARGEUR_grille = Grille_Distance.shape [1]
LARGEUR_grille = Grille_Distance.shape [0]

debug = False

# placements des pacgums et des fantomes

def PlacementsGUM():  # placements des pacgums
   GUM = np.zeros(TBL.shape,dtype=np.int32)
   for x in range(LARGEUR):
      for y in range(HAUTEUR):
         if ( TBL[x][y] == 0):
            GUM[x][y] = 1
         if ( Grille_Distance[x][y] == 2000):
            GUM[x][y] = 0
   return GUM


nb_gum = 100
gum_eaten = 0

GUM = PlacementsGUM()

# vérification de la position des pacgum si il n'y a plus de pacgum alors met à jour la grille des distances
def Verif_GUM():
   for x in range(LARGEUR):
      for y in range(HAUTEUR):
         if Grille_Distance[x][y] < 999:
            if( GUM[x][y] == 1 ):
               Grille_Distance[x][y] = 0
            else:
               Grille_Distance[x][y] = 220

# calcul le chemin le plus court vers la pacgum la plus proche
def pathfinder():
   maj = False
   for x in range(LARGEUR):
      for y in range(HAUTEUR):
         valeur_précedente = Grille_Distance[x][y]
         if Grille_Distance[x][y] < 999:
            valeur = 1 + min(Grille_Distance[x][y-1], Grille_Distance[x+1][y],Grille_Distance[x][y+1],Grille_Distance[x-1][y])
            if Grille_Distance[x][y] > valeur:
               Grille_Distance[x][y] = valeur
            if valeur_précedente != Grille_Distance[x][y]:
               maj = True
   return maj

# rafraichissement de la grille des distances
def refresh():
   while True:
      maj = pathfinder()
      if maj == False:
         break
   while True:
      maj = Ghosts_finder()
      if maj == False:
         break
   while True:
      maj = PacMan_finder()
      if maj == False:
         break

score = 0
Time = 0
# initialisation du mode chasse
Hunt = False
fuite = False
# compte combien de frame pacman passe en mode chasse
def Chrono():
   global Time, Hunt, escape
   if( Time < 15 ):
      Time += 1
   else:
       Hunt = False
       escape = False
       Time = 0

#supprime les pacgums de la map lorsque pacman passe sur les pacgums
def Mange_GUM():
   global score, Hunt, gum_eaten, escape, Time
   if GUM[PacManPos[0]][PacManPos[1]] == 1:
      GUM[PacManPos[0]][PacManPos[1]] = 0
      score += 100
      s.play('eat')
      gum_eaten +=1
      if(PacManPos[0] == 1 and PacManPos[1] == 1):
         Hunt = True
         Time = 0
         s.play('eat_super')
         escape = True
         print("haut gauche")
      if(PacManPos[0] == 18 and PacManPos[1] == 1):
         Hunt = True
         Time = 0
         s.play('eat_super')
         escape = True
         print("haut droit")
      if(PacManPos[0] == 1 and PacManPos[1] == 9):
         Hunt = True
         Time = 0
         s.play('eat_super')
         escape = True
         print("bas gauche")
      if(PacManPos[0] == 18 and PacManPos[1] == 9):
         Hunt = True
         Time = 0
         s.play('eat_super')
         escape = True
         print("bas droit")
#[x,y,vecteur_orientation]
PacManPos = [5,5,[0,0]]
#création des fantomes
Ghosts  = []
#[x,y,couleur,vecteur_orientation,grille_distance,scatter]
Ghosts.append([LARGEUR//2, (HAUTEUR // 2)-2 ,  "red"   ,(0,0),Grille_Blinky,False])
Ghosts.append([LARGEUR//2, HAUTEUR // 2     ,  "pink"  ,(0,0),Grille_Pinky ,False])
Ghosts.append([LARGEUR//2, HAUTEUR // 2     ,  "cyan"  ,(0,0),Grille_Inky  ,False])
Ghosts.append([LARGEUR//2, HAUTEUR // 2     ,  "orange",(0,0),Grille_Clyde ,False,Grille_Clyde_distancePacMan])
escape = False



#détermine les valeurs de la grille des distances des fantomes
def Ghosts_finder():
   maj = False
   for x in range(LARGEUR):
      for y in range(HAUTEUR):
         valeur_précedente = Grille_Fantome[x][y]
         if Grille_Distance[x][y] < 999:
            valeur = 1 + min(Grille_Fantome[x][y-1], Grille_Fantome[x+1][y],Grille_Fantome[x][y+1],Grille_Fantome[x-1][y])
            if (Grille_Fantome[x][y] > valeur):
               Grille_Fantome[x][y] = valeur
            if Grille_Fantome[x][y] != valeur_précedente:
               maj = True
   return maj

# c'est la version verif_GUM des fantomes
def verif_Ghosts():
    for x in range(LARGEUR):
        for y in range(HAUTEUR):
            if(Grille_Fantome[x][y] < 999):
               if( (x == Ghosts[0][0] and y == Ghosts[0][1]) or (x == Ghosts[1][0] and y == Ghosts[1][1]) or (x == Ghosts[2][0] and y == Ghosts[2][1]) or (x == Ghosts[3][0] and y == Ghosts[3][1])):
                  Grille_Fantome[x][y] = 0
               else: Grille_Fantome[x][y] = 220

def verif_PacMan():
   global escape, Ghosts
   xx, yy = 0, 0
   for F in Ghosts:

      if F[2]=="red" and escape==False:
         if F[5]==True:
            xx,yy = 1,1
         if F[5]==False:
            xx = PacManPos[0]
            yy = PacManPos[1]

      if F[2]=="pink" and escape==False:
         x_pinky = PacManPos[0]
         y_pinky = PacManPos[1]
         if F[5]==False:
            for i in range(4,-1,-1):
               try:
                  if x_pinky+PacManPos[2][0]*i < 0 or y_pinky+PacManPos[2][1]*i < 0:
                     continue
                  if F[4][x_pinky+PacManPos[2][0]*i][y_pinky+PacManPos[2][1]*i]<999:
                     x_pinky +=PacManPos[2][0]*i
                     y_pinky +=PacManPos[2][1]*i
                     break
               except:
                  continue
            xx, yy = x_pinky, y_pinky
         if F[5]==True:
            xx, yy = LARGEUR - 2, 1

      if F[2]=="cyan" and escape==False:
         x_cyan = PacManPos[0]
         y_cyan = PacManPos[1]
         if F[5]==False:
            x_red, y_red = Ghosts[0][0], Ghosts[0][1]
            x_pacman = PacManPos[0]+2*PacManPos[2][0]
            y_pacman = PacManPos[1]+2*PacManPos[2][1]
            vecteur = [2*(x_pacman-x_red),2*(y_pacman-y_red)]
            step, stop = 1, 1
            if vecteur[0]>0:
               step, stop = -1, -1
            for x in range(vecteur[0],stop,step):
               try:
                  y = round(x*(vecteur[1]/vecteur[0]))
                  if x+x_red<0 or y+y_red<0:
                     continue
                  if F[4][x+x_red][y+y_red] < 999:
                     x_cyan = x+x_red
                     y_cyan = y+y_red
                     break
               except:
                  continue
            xx, yy = x_cyan, y_cyan
         if F[5]==True:
            xx, yy = LARGEUR - 2, HAUTEUR - 2

      if F[2]=="orange" and escape==False:
         if F[5]==False:
            xx = PacManPos[0]
            yy = PacManPos[1]
         if F[5]==True:
            xx, yy = 1, HAUTEUR - 2

      if F[2]=="orange":
         for x in range(LARGEUR):
            for y in range(HAUTEUR):
               if x == PacManPos[0] and y == PacManPos[1]:
                  F[6][x][y]=0
               elif F[4][x][y] < 999:
                  F[6][x][y]=220

      if escape == True:
         xx, yy = PacManPos[0], PacManPos[1]

      for x in range(LARGEUR):
         for y in range(HAUTEUR):
            if x == xx and y == yy:
               F[4][x][y]=0
            elif F[4][x][y] < 999:
               F[4][x][y]=220





def PacMan_finder():
   global Ghosts
   maj = False
   for F in Ghosts:
      for x in range(LARGEUR):
         for y in range(HAUTEUR):
            valeur_précedente = F[4][x][y]
            if F[4][x][y] < 999:
               valeur = 1 + min(F[4][x][y-1],F[4][x+1][y],F[4][x][y+1],F[4][x-1][y])
               if (F[4][x][y] > valeur):
                  F[4][x][y] = valeur
            if valeur_précedente != F[4][x][y]:
               maj = True

      if F[2]=="orange":
         for x in range(LARGEUR):
            for y in range(HAUTEUR):
               valeur_précedente = F[6][x][y]
               if F[6][x][y] < 999:
                  valeur = 1 + min(F[6][x][y-1],F[6][x+1][y],F[6][x][y+1],F[6][x-1][y])
                  if (F[6][x][y] > valeur):
                     F[6][x][y] = valeur
               if valeur_précedente != F[6][x][y]:
                  maj = True
   return maj

##############################################################################
#
#   Partie II :  AFFICHAGE -- NE PAS MODIFIER  jusqu'à la prochaine section
#
##############################################################################



ZOOM = 40   # taille d'une case en pixels
EPAISS = 8  # epaisseur des murs bleus en pixels

screeenWidth = (LARGEUR+1) * ZOOM
screenHeight = (HAUTEUR+2) * ZOOM

Window = tk.Tk()
Window.geometry(str(screeenWidth)+"x"+str(screenHeight))   # taille de la fenetre
Window.title("ESIEE - PACMAN")

# gestion de la pause

PAUSE_FLAG = False
STOP_FLAG = False

def keydown(e):
   global PAUSE_FLAG
   if e.char == ' ' :
      PAUSE_FLAG = not PAUSE_FLAG

Window.bind("<KeyPress>", keydown)


# création de la frame principale stockant plusieurs pages

F = tk.Frame(Window)
F.pack(side="top", fill="both", expand=True)
F.grid_rowconfigure(0, weight=1)
F.grid_columnconfigure(0, weight=1)


# gestion des différentes pages

ListePages  = {}
PageActive = 0

def CreerUnePage(id):
    Frame = tk.Frame(F)
    ListePages[id] = Frame
    Frame.grid(row=0, column=0, sticky="nsew")
    return Frame

def AfficherPage(id):
    global PageActive
    PageActive = id
    ListePages[id].tkraise()


def WindowAnim():
    MainLoop()
    Window.after(100,WindowAnim)

Window.after(100,WindowAnim)

# Ressources

PoliceTexte = tkfont.Font(family='Arial', size=22, weight="bold", slant="italic")

# création de la zone de dessin

Frame1 = CreerUnePage(0)

canvas = tk.Canvas( Frame1, width = screeenWidth, height = screenHeight )
canvas.place(x=0,y=0)
canvas.configure(background='black')


#  FNT AFFICHAGE


def To(coord):
   return coord * ZOOM + ZOOM

# dessine l'ensemble des éléments du jeu par dessus le décor

anim_bouche = 0
animPacman = [ 5,10,15,10,5]


def Affiche(PacmanColor,data1,data2):
   global anim_bouche

   def CreateCircle(x,y,r,coul):
      canvas.create_oval(x-r,y-r,x+r,y+r, fill=coul, width  = 0)

   canvas.delete("all")


   # murs

   for x in range(LARGEUR-1):
      for y in range(HAUTEUR):
         if ( TBL[x][y] == 1 and TBL[x+1][y] == 1 ):
            xx = To(x)
            xxx = To(x+1)
            yy = To(y)
            canvas.create_line(xx,yy,xxx,yy,width = EPAISS,fill="blue")

   for x in range(LARGEUR):
      for y in range(HAUTEUR-1):
         if ( TBL[x][y] == 1 and TBL[x][y+1] == 1 ):
            xx = To(x)
            yy = To(y)
            yyy = To(y+1)
            canvas.create_line(xx,yy,xx,yyy,width = EPAISS,fill="blue")

   # pacgum
   for x in range(LARGEUR):
      for y in range(HAUTEUR):
         if ( GUM[x][y] == 1):
            xx = To(x)
            yy = To(y)
            e = 5
            canvas.create_oval(xx-e,yy-e,xx+e,yy+e,fill="orange")

            if(x == 1 and y == 1): canvas.create_oval(xx-e,yy-e,xx+e,yy+e,fill="red")
            if(x == 1 and y == 9): canvas.create_oval(xx-e,yy-e,xx+e,yy+e,fill="red")
            if(x == 18 and y == 1): canvas.create_oval(xx-e,yy-e,xx+e,yy+e,fill="red")
            if(x == 18 and y == 9): canvas.create_oval(xx-e,yy-e,xx+e,yy+e,fill="red")

   if debug == True:
      for x in range(LARGEUR):
         for y in range(HAUTEUR):
            xx = To(x)
            yy = To(y) -11
            txt = str(Ghosts[3][4][x][y])
            if Ghosts[2][4][x][y] >999:
               txt = "∞"
            canvas.create_text(xx,yy, text = txt, fill ="white", font=("Purisa", 8))

      #for x in range(LARGEUR):
      #   for y in range(HAUTEUR):
      #      xx = To(x)
      #      yy = To(y) - 11
      #      txt = data1[x][y]
      #      if Grille_Distance[x][y] < 999:
      #         canvas.create_text(xx,yy, text = txt, fill ="white", font=("Purisa", 8))

      #for x in range(LARGEUR):
      #   for y in range(HAUTEUR):
      #      xx = To(x) + 10
      #      yy = To(y)
      #      txt = (str(data2[x][y]) + "/" + str(data1[x][y]))
      #      canvas.create_text(xx,yy, text = txt, fill ="yellow", font=("Purisa", 8))


   # dessine pacman
   xx = To(PacManPos[0])
   yy = To(PacManPos[1])
   e = 20
   anim_bouche = (anim_bouche+1)%len(animPacman)
   ouv_bouche = animPacman[anim_bouche]
   tour = 360 - 2 * ouv_bouche
   if( Hunt ):
      PacmanColor = "red"
   canvas.create_oval(xx-e,yy-e, xx+e,yy+e, fill = PacmanColor)
   if PacManPos[2][1]==0:
      canvas.create_polygon(xx,yy,xx+e*PacManPos[2][0],yy+ouv_bouche,xx+e*PacManPos[2][0],yy-ouv_bouche, fill="black")  # bouche
   if PacManPos[2][0]==0:
      canvas.create_polygon(xx,yy,xx-ouv_bouche,yy+e*PacManPos[2][1],xx+ouv_bouche,yy+e*PacManPos[2][1], fill="black")
   #dessine les fantomes
   dec = -3
   for P in Ghosts:
      xx = To(P[0])
      yy = To(P[1])
      e = 16

      coul = P[2]
      if Hunt:
         coul = "blue"
      # corps du fantome
      CreateCircle(dec+xx,dec+yy-e+6,e,coul)
      canvas.create_rectangle(dec+xx-e,dec+yy-e,dec+xx+e+1,dec+yy+e, fill=coul, width  = 0)

      # oeil gauche
      CreateCircle(dec+xx-7,dec+yy-8,5,"white")
      CreateCircle(dec+xx-7,dec+yy-8,3,"black")

      # oeil droit
      CreateCircle(dec+xx+7,dec+yy-8,5,"white")
      CreateCircle(dec+xx+7,dec+yy-8,3,"black")

      dec += 3

   # texte

   canvas.create_text(screeenWidth // 2, screenHeight- 50 , text = "PAUSE : PRESS SPACE", fill ="yellow", font = PoliceTexte)
   canvas.create_text(screeenWidth // 2, screenHeight- 20 , text = score, fill ="yellow", font = PoliceTexte)
   if (STOP_FLAG):
       canvas.create_text(screeenWidth // 2, screenHeight // 2, text="GAME OVER", fill="yellow", font=(PoliceTexte, 30))
   if (nb_gum==0):
       canvas.create_text(screeenWidth // 2, screenHeight // 2, text="PACMAN WINS !", fill="yellow",
                          font=(PoliceTexte, 30))

AfficherPage(0)

#########################################################################
#
#  Partie III :   Gestion de partie   -   placez votre code dans cette section
#
#########################################################################


def PacManPossibleMove():
    L = []
    x,y = PacManPos[0],PacManPos[1]
    if ( Hunt ):
         Chrono()
         minimum = min(Grille_Fantome[x][y-1],Grille_Fantome[x+1][y],Grille_Fantome[x][y+1],Grille_Fantome[x-1][y])
         if ( Grille_Fantome[x  ][y-1] == minimum ): L.append((0,-1))
         if ( Grille_Fantome[x  ][y+1] == minimum ): L.append((0, 1))
         if ( Grille_Fantome[x+1][y  ] == minimum ): L.append(( 1,0))
         if ( Grille_Fantome[x-1][y  ] == minimum ): L.append((-1,0))

    else:

         if( Grille_Fantome[x][y] > 3 ):
            minimum = min(Grille_Distance[x][y-1],Grille_Distance[x+1][y],Grille_Distance[x][y+1],Grille_Distance[x-1][y])
            if ( Grille_Distance[x  ][y-1] == minimum ): L.append((0,-1))
            if ( Grille_Distance[x  ][y+1] == minimum ): L.append((0, 1))
            if ( Grille_Distance[x+1][y  ] == minimum ): L.append(( 1,0))
            if ( Grille_Distance[x-1][y  ] == minimum ): L.append((-1,0))
         else:
            v1 = 0
            v2 = 0
            v3 = 0
            v4 = 0
            if(Grille_Fantome[x][y-1] < 500):
                  v1 = Grille_Fantome[x][y-1]
            if(Grille_Fantome[x+1][y] < 500):
                  v2 = Grille_Fantome[x+1][y]
            if(Grille_Fantome[x][y+1] < 500):
                  v3 = Grille_Fantome[x][y+1]
            if(Grille_Fantome[x-1][y] < 500):
                  v4 = Grille_Fantome[x-1][y]
            maxi = max( v1, v2, v3, v4)
            if ( Grille_Fantome[x  ][y-1] == maxi ): L.append((0,-1))
            if ( Grille_Fantome[x  ][y+1] == maxi ): L.append((0, 1))
            if ( Grille_Fantome[x+1][y  ] == maxi ): L.append(( 1,0))
            if ( Grille_Fantome[x-1][y  ] == maxi ): L.append((-1,0))

    return L

def det_couloir(x,y):
    if (TBL_corridor[x][y] == 0 ): return True
    else: return False

def det_colli():
    global STOP_FLAG, score
    x,y = PacManPos[0],PacManPos[1]

    for Z in Ghosts:
        if( x == Z[0] ):
            if( y == Z[1] ):
                if( Hunt ):
                   score += 2000
                   Z[0] = LARGEUR//2
                   Z[1] = HAUTEUR // 2
                   s.play('eatf')
                else:
                   STOP_FLAG = True
                   s.play('game_over')


def GhostsPossibleMove(Fantome):
   L = []
   x = Fantome[0]
   y = Fantome[1]
   if Fantome[4][x][y]==0:
      L.append((0,0))
      return L
   if Fantome[2]=="cyan" and gum_eaten < 30:
      L.append((0,0))
      return L
   if Fantome[2]=="orange" and gum_eaten < int(nb_gum/3):
      L.append((0,0))
      return L

   if escape == False:
      minimum = min(Fantome[4][x][y-1],Fantome[4][x+1][y],Fantome[4][x][y+1],Fantome[4][x-1][y])
      if (Fantome[4][x  ][y-1] == minimum ): L.append((0,-1))
      if (Fantome[4][x  ][y+1] == minimum ): L.append((0, 1))
      if (Fantome[4][x+1][y  ] == minimum ): L.append(( 1,0))
      if (Fantome[4][x-1][y  ] == minimum ): L.append((-1,0))

   if escape == True:
      v1,v2,v3,v4=0,0,0,0
      if(Fantome[4][x][y-1] < 999):
         v1 = Fantome[4][x][y-1]
      if(Fantome[4][x+1][y] < 999):
         v2 = Fantome[4][x+1][y]
      if(Fantome[4][x][y+1] < 999):
            v3 = Fantome[4][x][y+1]
      if(Fantome[4][x-1][y] < 999):
            v4 = Fantome[4][x-1][y]
      maximum = max(v1,v2,v3,v4)
      if (Fantome[4][x  ][y-1] == maximum ): L.append((0,-1))
      if (Fantome[4][x  ][y+1] == maximum ): L.append((0, 1))
      if (Fantome[4][x+1][y  ] == maximum ): L.append(( 1,0))
      if (Fantome[4][x-1][y  ] == maximum ): L.append((-1,0))
   if len(L)==0:
      L.append((0,0))

    #if det_couloir(x,y):
    #    if ( TBL[x  ][y-1] == 0 ): L.append((0,-1))
    #    if ( TBL[x  ][y+1] == 0 ): L.append((0, 1))
    #   if ( TBL[x+1][y  ] == 0 ): L.append(( 1,0))
    #    if ( TBL[x-1][y  ] == 0 ): L.append((-1,0))
    #else:
    #    L.append(C)



   return L



def IA():
    if not PAUSE_FLAG:
        global PacManPos, Ghosts, fuite
        #deplacement Pacman
        det_colli()
        L = PacManPossibleMove()
        choix = random.randrange(len(L))
        PacManPos[0] += L[choix][0]
        PacManPos[1] += L[choix][1]
        PacManPos[2][0] = L[choix][0]
        PacManPos[2][1] = L[choix][1]

        for f in Ghosts:
           if f[2]=="orange" and escape == False:
              if f[6][f[0]][f[1]]>8:
                 f[5]=False
              if f[6][f[0]][f[1]]<=8:
                 f[5]=True
              break

        det_colli()
        Mange_GUM()
        Verif_GUM()
        verif_PacMan()

        refresh()
        #print(Ghosts[1][4])
    if not PAUSE_FLAG:
        #deplacement Fantome
        det_colli()
        for F in Ghosts:
           if( (not Hunt) or fuite ):
            L = GhostsPossibleMove(F)
            choix = random.randrange(len(L))
            F[0] += L[choix][0]
            F[1] += L[choix][1]
            F[3] = (L[choix][0],L[choix][1])


            verif_Ghosts()
            det_colli()
            refresh()
        fuite = not fuite


def reinit() :

   global PacManPos, Ghosts, MODE, score, gameover, win, GUM, tour,MUR ,CHE ,GHO,fuite , Time,nb_gum , gum_eaten,debug,Hunt , STOP_FLAG


   HAUTEUR = TBL.shape[1]
   LARGEUR = TBL.shape[0]

   nb_gum = 100
   gum_eaten = 0

   GUM = PlacementsGUM()
   # [x,y,vecteur_orientation]
   PacManPos = [5, 5, [0, 0]]

   # création des fantomes
   Ghosts = []
   # [x,y,couleur,vecteur_orientation,grille_distance,scatter]
   Ghosts.append([LARGEUR // 2, (HAUTEUR // 2) - 2, "red", (0, 0), Grille_Blinky, False])
   Ghosts.append([LARGEUR // 2, HAUTEUR // 2, "pink", (0, 0), Grille_Pinky, False])
   Ghosts.append([LARGEUR // 2, HAUTEUR // 2, "cyan", (0, 0), Grille_Inky, False])
   Ghosts.append([LARGEUR // 2, HAUTEUR // 2, "orange", (0, 0), Grille_Clyde, False,Grille_Clyde_distancePacMan])
   escape = False

   score = 0
   Time = 0
   # initialisation du mode chasse
   Hunt = False
   fuite = False
   nb_gum = 100
   gum_eaten = 0
   STOP_FLAG = False





#  Boucle principale de votre jeu appelée toutes les 500ms

def MainLoop():
   if STOP_FLAG == False:
      IA()
   else:
        time.sleep(3.0)
        reinit()
   Affiche(PacmanColor = "yellow", data1=Grille_Fantome, data2=Grille_Distance)


###########################################:
#  demarrage de la fenetre - ne pas toucher

Window.mainloop()