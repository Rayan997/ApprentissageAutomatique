# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 10:50:43 2021

@author: rayan
"""

import numpy as np
from random import uniform
from random import randint
import time
pi = np.pi

class algoG:
    
    
    
    
    def genere_individu(self):
        L = [] #Liste contenant les coordonnées d'un individu
        a = uniform(0,1)
        b = randint(1,20)
        c = randint(1,20)
        L.extend([a,b,c])
        return L
    
    
    def printInd(self,ind):
        print("a =",ind[0],"b =",ind[1],"c =",ind[2])
        
        
    def cross_over(self,ind1,ind2):
        L = [] #Liste contenant les coordonnées du nouvel individu
        a = (ind1[0] + ind2[0])/2
        b = int((ind1[1] + ind2[1])/2)
        c = int((ind1[2] + ind2[2])/2)
        L.extend([a,b,c])
        return L
    
    
    def mutation(self,ind):
        x = randint(0,2) #permet de changer a,b ou c en fonction de si x égal 0,1 ou 2
        y = randint(0,1) #permet de savoir si l'on augmente ou diminue cette valeur
        if ( x == 0 ):
            if ( ind[0] >= 0.95 ):
                ind[0] -= 0.05
            else :
                if ( ind[0] <= 0.05 ):
                    ind[0] += 0.05
                else :
                    if ( y == 0 ):
                        ind[0] -= 0.05
                    else :
                        ind[0] += 0.05
        elif ( x == 1 ):
            if ( ind[1] == 20 ):
                ind[1] -= 1
            else :
                if ( ind[1] == 1 ):
                    ind[1] += 1
                else :
                    if ( y == 0 ):
                        ind[1] -= 1
                    else :
                        ind[1] += 1
        else :
            if ( ind[2] == 20 ):
                ind[2] -= 1
            else :
                if ( ind[2] == 1 ):
                    ind[2] += 1
                else :
                    if ( y == 0 ):
                        ind[2] -= 1
                    else :
                        ind[2] += 1
        return ind
    
    
    def fitness(self,ind):
        liste = []
        res = 0
        a = ind[0]
        b = ind[1]
        c = ind[2]
        
        #### On remplit une liste de liste, chaque sous liste contient un instant i et et la température le l'étoile à cette instant
        
        f = open("D:\\IA\\temperature_sample.csv",'r')#fichier contenant les valeurs observées de la température de l'étoile aux instants i.
        lines = f.readlines()
        lines_with_no_first_line = lines[1:]
        for l in lines_with_no_first_line:
            x = l.split(";")#liste contenant 2 chaines de caractères, i et t(i)
            x = [float(y) for y in x]#liste contenant 2 float, i et t(i)
            liste.extend([x])
        f.close()
        
        #### On calcul la fitness
        
        for j in range(len(liste)):
            ti = 0
            i = liste[j][0]
            vi = liste[j][1]
            for n in range(c+1):#Calcul de la valeur de t(i) pour i = liste[j][0]
                ti += (a**n) * np.cos(pi * i * b**n)
            res += (ti - vi)**2
                
        return res
    
    
    def generePop(self,n):
        for i in range(n):
            ind = self.genere_individu()
            self.population.extend([ind])
            
    
    def printPop(self):
        for i in self.population:
            self.printInd(i)
            print("fitness :",self.fitness(i))
            print()
        
    def moyFitnessPop(self): #Moyenne de la fitness de la population
        moy = 0
        i = 0
        for ind in self.population:
            moy += self.fitness(ind)
            i += 1
        return moy/i
    
    def varFitnessPop(self): #Variance de la fitness de la population
        var = 0
        i = 0
        for ind in self.population:
            var += self.fitness(ind)**2
            i += 1
        return var/i - self.moyFitnessPop()**2
    
    def rankPop(self):
        score = []
        for i in self.population:
            score.append(self.fitness(i))
        nStruct = list(zip(self.population, score))
        nStruct.sort(key = lambda tup : tup[1])
        self.population = []
        for elem in nStruct:
            #print(elem[0][0],elem[1])
            self.population.append(elem[0])
    
    def selectionPop(self):
        L = []
        n = len(self.population)
        m = int(n/5) #On sélectionne 1/5 de la population
        for i in range(m):
            L.append(self.population[i])
        self.population = L
        
    def mutationPop(self):
        for ind in self.population: #1/2 des individus mute
            if (randint(0,1) == 0 ):
                ind = self.mutation(ind)
    
    def cross_overPop(self):
        L = []
        n = len(self.population)
        for j in range(5):
            for i in range(j,n):
                ind1 = self.population[j]
                ind2 = self.population[i]
                L.append(self.cross_over(ind1,ind2))
        self.population = L
            
        
    def ajout_hasard(self,n):
        for i in range(n):
            ind = self.genere_individu()
            self.population.append(ind)
        
            
        
        
        
            
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    def run(self):
        
        temps1 = time.time()
        N = 100
        drapeau = 0 #Pour éviter que la boucle while plus tard soit une boucle infinie
        liste_meilleur_individu = []
        #print("Population triée pas fitness croissante","\n")    
        self.population = []
        self.generePop(N)
        self.rankPop()
        #self.printPop()
        liste_meilleur_individu = [self.population[0]]
        
        #p = int(input("Saisir le nombre de générations souhaité"))
        #on peut remplacer la boucle while par :
        for i in range(10): #On peut remplacer 3 par p
        #while ( self.fitness(self.population[0]) > 0.033 and drapeau < 15):
            
            drapeau += 1
            #print("\n","Sélection des individus ","\n")
            
            self.selectionPop()
            #self.printPop()
            #print("Moyenne fitness =",self.moyFitnessPop())
            
            #print("\n","Cross over ,mutation de la population et ajout de hasard","\n")
            self.ajout_hasard(int(N/3))
            self.mutationPop()
            self.cross_overPop()
            self.rankPop()
            #self.printPop()
            #print("\n","Moyenne fitness =",self.moyFitnessPop(),"\n")
            #print("\n","Meilleur individu :","\n")
            #print(self.population[0])
            #print("Fitness du meilleur individu",self.fitness(self.population[0]))
            
            liste_meilleur_individu.append(self.population[0])
        
        self.population = liste_meilleur_individu
        self.rankPop()
        self.printInd(self.population[0])
        print("Fitness du meilleur individu",self.fitness(self.population[0]))
        
    
        
        # for h in range(0,21):          
        #     print(self.fitness([0.34,15,h]))
        
        temps2 = time.time()
        
        print("Temps d'execution :",temps2-temps1)


        
    
    

    
    





if __name__ == '__main__' :
    algoG = algoG()
    #pour générer un problème
    algoG.run()