# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 11:37:54 2021

@author: rayan
"""

import numpy as np
import pandas as pd
import time
pi = np.pi

class knn:
    
    
    
        
    
    def distancefonction(self,ind): #ind est un individu
        # self.distance_classA = [] #Correspond aux distance de l'individu à la liste classA1
        # self.distance_classB = []
        # self.distance_classC = []
        # self.distance_classD = []
        # self.distance_classE = []
        self.distance_classA1 = [] #Correspond aux distance de l'individu à la liste classA1
        self.distance_classB1 = []
        self.distance_classC1 = []
        self.distance_classD1 = []
        self.distance_classE1 = []
        res = 0
        # self.classA = []
        # self.classB = []
        # self.classC = []
        # self.classD = []
        # self.classE = []
        self.classA1 = []
        self.classB1 = []
        self.classC1 = []
        self.classD1 = []
        self.classE1 = []
        self.class2 = [] #Contient les données de finalTest.csv
        
        
        
        
        #### On remplit une liste de liste, chaque sous liste contient les caractéristiques d'un individu
        
        f1 = open("D:\\IA\\data.csv",'r')#fichier contenant les valeurs observées des valeurs ci-dessus.
        df1 = pd.read_csv(r"D:\IA\data.csv", names = ["x1", "x2", "x3", "x4", "x5", "x6", "label"])
        lines = f1.readlines()
        for l in lines:
            x = l.split(",")#liste contenant 7 chaines de caractères     
            z = x[6]
            x = [ float(y) for y in x[:6] ]#liste contenant 6 float et un string
            x.append(z)
            if ( x[6] == "classA\n"):
                self.classA1.extend([x])
                res += 1
            else :
                if ( x[6] == "classB\n"):
                        self.classB1.extend([x])
                        res += 1
                else:
                    if ( x[6] == "classC\n"):
                        self.classC1.extend([x])
                        res += 1
                    else:
                        if ( x[6] == "classD\n"):
                            self.classD1.extend([x])
                            res += 1
                        else:
                            if ( x[6] == "classE\n"):
                                self.classE1.extend([x])
                                res += 1
               
        f1.close()
        
        f2 = open("D:\\IA\\preTest.csv",'r')#fichier contenant les valeurs observées des valeurs ci-dessus.
        df2 = pd.read_csv(r"D:\IA\preTest.csv", names = ["x1", "x2", "x3", "x4", "x5", "x6", "label"])
        lines = f2.readlines()
        for l in lines:
            x = l.split(",")#liste contenant 7 chaines de caractères     
            z = x[6]
            x = [ float(y) for y in x[:6] ]#liste contenant 6 float et un string
            x.append(z)
            if ( x[6] == "classA\n"):
                self.classA1.extend([x])
                res += 1
            else :
                if ( x[6] == "classB\n"):
                        self.classB1.extend([x])
                        res += 1
                else:
                    if ( x[6] == "classC\n"):
                        self.classC1.extend([x])
                        res += 1
                    else:
                        if ( x[6] == "classD\n"):
                            self.classD1.extend([x])
                            res += 1
                        else:
                            if ( x[6] == "classE\n"):
                                self.classE1.extend([x])
                                res += 1
                                
        f2.close()
        
        f3 = open("D:\\IA\\finalTest.csv",'r')#fichier contenant les valeurs observées des valeurs ci-dessus.
        df3 = pd.read_csv(r"D:\IA\finalTest.csv", names = ["x1", "x2", "x3", "x4", "x5", "x6"])
        lines = f3.readlines()
        for l in lines:
            x = l.split(",")#liste contenant 6 chaines de caractères     
            x = [ float(y) for y in x ]#liste contenant 6 float
            self.class2.extend([x])
                                
        f3.close()
        
        #Partie utile pour tester les données ( en splitant un set connue )
        
        # self.classA1 = self.classA[:int(0.7*len(self.classA))] #Liste que l'algorithme va prendre en mémoire
        # self.classB1 = self.classB[:int(0.7*len(self.classB))]
        # self.classC1 = self.classC[:int(0.7*len(self.classC))]
        # self.classD1 = self.classD[:int(0.7*len(self.classD))]
        # self.classE1 = self.classE[:int(0.7*len(self.classE))]
        
        # self.classA2 = self.classA[int(0.7*len(self.classA)):] #Liste pour tester l'algorithme sur des valeurs qu'il ne connait pas
        # self.classB2 = self.classB[int(0.7*len(self.classB)):]
        # self.classC2 = self.classC[int(0.7*len(self.classC)):]
        # self.classD2 = self.classD[int(0.7*len(self.classD)):]
        # self.classE2 = self.classE[int(0.7*len(self.classE)):]
        
        
        #### On calcul les coefficients pour pouvoir normaliser les distances
        
        #On remarque que, en général, il y a plus d'erreurs en normalisant
        a = 1 #Permettent de ne pas normaliser
        b = 1
        c = 1
        d = 1
        e = 1
        f = 1
        # a = max(df["x1"]) #Correspond à x1 définit dans df
        # b = max(df["x2"]) 
        # c = max(df["x3"]) 
        # d = max(df["x4"]) 
        # e = max(df["x5"]) 
        # f = max(df["x6"]) 
        
        #### On calcul la distance
        
        for i in range(len(self.classA1)):
            #Calcul de la valeur de la distance de la fleur en paramètre à la ième fleur de classA
            y1 = self.classA1[i][0] #Premier attribut (première colonne) de l'individu self.classA[i]
            y2 = self.classA1[i][1] 
            y3 = self.classA1[i][2] 
            y4 = self.classA1[i][3] 
            y5 = self.classA1[i][4] 
            y6 = self.classA1[i][5] 
            self.distance_classA1.append(  ( ((y1-ind[0])/a)**2 + ((y2-ind[1])/b)**2 + ((y3-ind[2])/c)**2 + ((y4-ind[3])/d)**2 + ((y5-ind[4])/e)**2 + ((y6-ind[5])/f)**2 ) ** (1/2)  )
            
        for i in range(len(self.classB1)):
            #Calcul de la valeur de la distance de la fleur en paramètre à la ième fleur de classB
            y1 = self.classB1[i][0] #Premier attribut (première colonne) de l'individu self.classB[i]
            y2 = self.classB1[i][1] 
            y3 = self.classB1[i][2] 
            y4 = self.classB1[i][3] 
            y5 = self.classB1[i][4] 
            y6 = self.classB1[i][5] 
            self.distance_classB1.append(  ( ((y1-ind[0])/a)**2 + ((y2-ind[1])/b)**2 + ((y3-ind[2])/c)**2 + ((y4-ind[3])/d)**2 + ((y5-ind[4])/e)**2 + ((y6-ind[5])/f)**2 ) ** (1/2)  )
            
        for i in range(len(self.classC1)):
            #Calcul de la valeur de la distance de la fleur en paramètre à la ième fleur de classC
            y1 = self.classC1[i][0] #Premier attribut (première colonne) de l'individu self.classC[i]
            y2 = self.classC1[i][1] 
            y3 = self.classC1[i][2] 
            y4 = self.classC1[i][3] 
            y5 = self.classC1[i][4] 
            y6 = self.classC1[i][5] 
            self.distance_classC1.append(  ( ((y1-ind[0])/a)**2 + ((y2-ind[1])/b)**2 + ((y3-ind[2])/c)**2 + ((y4-ind[3])/d)**2 + ((y5-ind[4])/e)**2 + ((y6-ind[5])/f)**2 ) ** (1/2)  )
            
        for i in range(len(self.classD1)):
            #Calcul de la valeur de la distance de la fleur en paramètre à la ième fleur de classD
            y1 = self.classD1[i][0] #Premier attribut (première colonne) de l'individu self.classD[i]
            y2 = self.classD1[i][1] 
            y3 = self.classD1[i][2] 
            y4 = self.classD1[i][3] 
            y5 = self.classD1[i][4] 
            y6 = self.classD1[i][5] 
            self.distance_classD1.append(  ( ((y1-ind[0])/a)**2 + ((y2-ind[1])/b)**2 + ((y3-ind[2])/c)**2 + ((y4-ind[3])/d)**2 + ((y5-ind[4])/e)**2 + ((y6-ind[5])/f)**2 ) ** (1/2)  )
            
        for i in range(len(self.classE1)):
            #Calcul de la valeur de la distance de la fleur en paramètre à la ième fleur de classE
            y1 = self.classE1[i][0] #Premier attribut (première colonne) de l'individu self.classE[i]
            y2 = self.classE1[i][1] 
            y3 = self.classE1[i][2] 
            y4 = self.classE1[i][3] 
            y5 = self.classE1[i][4] 
            y6 = self.classE1[i][5] 
            self.distance_classE1.append(  ( ((y1-ind[0])/a)**2 + ((y2-ind[1])/b)**2 + ((y3-ind[2])/c)**2 + ((y4-ind[3])/d)**2 + ((y5-ind[4])/e)**2 + ((y6-ind[5])/f)**2 ) ** (1/2)  )
        
        
        # self.distance_classA1 = self.distance_classA[:int(0.7*len(self.distance_classA))] #Liste que l'algorithme va prendre en mémoire
        # self.distance_classB1 = self.distance_classB[:int(0.7*len(self.distance_classB))]
        # self.distance_classC1 = self.distance_classC[:int(0.7*len(self.distance_classC))]
        # self.distance_classD1 = self.distance_classD[:int(0.7*len(self.distance_classD))]
        # self.distance_classE1 = self.distance_classE[:int(0.7*len(self.distance_classE))]
        
        # self.distance_classA2 = self.distance_classA[int(0.7*len(self.distance_classA)):] #Liste pour tester l'algorithme sur des valeurs qu'il ne connait pas
        # self.distance_classB2 = self.distance_classB[int(0.7*len(self.distance_classB)):]
        # self.distance_classC2 = self.distance_classC[int(0.7*len(self.distance_classC)):]
        # self.distance_classD2 = self.distance_classD[int(0.7*len(self.distance_classD)):]
        # self.distance_classE2 = self.distance_classE[int(0.7*len(self.distance_classE)):]
    
    
    
    def rankDistance(self,liste,distance_liste):#liste est setosa ou versicolor ou virginica
        nStruct = list(zip(liste, distance_liste))
        nStruct.sort(key = lambda tup : tup[1])
        liste = []
        for elem in nStruct:
            #print(elem[0][0],elem[1])
            liste.append(elem[0])
        return liste
    
    
            
    def kMeilleurIndividu(self,k): #Permet de trouver les k plus proche voisins(appartenant à self.classX1) d'un individu de self.classX2, 
        self.listekMeilleurInd = []

        self.distance = [] #On créé une liste distance qui contiendra les distances des individus gardés en mémoire
        self.distance.extend(self.distance_classA1)
        self.distance.extend(self.distance_classB1)
        self.distance.extend(self.distance_classC1)
        self.distance.extend(self.distance_classD1)
        self.distance.extend(self.distance_classE1)
        
        self.listIndividu = [] #On créé une liste listIndividu qui contient les éléments de toutes les liste self.classX1
        #Elle contient ainsi les candidats aux k plus proche voisins
        self.listIndividu.extend(self.classA1)
        self.listIndividu.extend(self.classB1)
        self.listIndividu.extend(self.classC1)
        self.listIndividu.extend(self.classD1)
        self.listIndividu.extend(self.classE1)
        
        self.listIndividuVerification = [] #On créé une liste listIndividu qui contient les éléments de toutes les liste self.classX2
        #Elle contient ainsi les individus pour lesquels on cherche leur nom.
        # self.listIndividuVerification.extend(self.classA2)
        # self.listIndividuVerification.extend(self.classB2)
        # self.listIndividuVerification.extend(self.classC2)
        # self.listIndividuVerification.extend(self.classD2)
        # self.listIndividuVerification.extend(self.classE2)
        self.listIndividuVerification.extend(self.class2)
        
        nStruct = list(zip(self.listIndividu,self.distance))
        nStruct.sort(key = lambda tup : tup[1])
        for elem in nStruct:       
            self.listekMeilleurInd.append(elem[0])
            
        return self.listekMeilleurInd[:k]
        
    
    def classLaPlusFrequente(self,k):
        nbclassA = 0
        nbclassB = 0
        nbclassC = 0
        nbclassD = 0
        nbclassE = 0
        for x in self.listekMeilleurInd[:k]:
            if ( x[6] == "classA\n"):
                nbclassA += 1
            else :
                if ( x[6] == "classB\n"):
                        nbclassB += 1
                else:
                    if ( x[6] == "classC\n"):
                        nbclassC += 1
                    else:
                        if ( x[6] == "classD\n"):
                            nbclassD += 1
                        else:
                            if ( x[6] == "classE\n"):
                                nbclassE += 1
        if ( max(nbclassA,nbclassB,nbclassC,nbclassD,nbclassE) == nbclassA ):
            res = "classA\n"
        else :
            if ( max(nbclassA,nbclassB,nbclassC,nbclassD,nbclassE) == nbclassB ):
                res = "classB\n"
            else :
                if ( max(nbclassA,nbclassB,nbclassC,nbclassD,nbclassE) == nbclassC ):
                    res = "classC\n"
                else :
                    if ( max(nbclassA,nbclassB,nbclassC,nbclassD,nbclassE) == nbclassD ):
                        res = "classD\n"
                    else :
                        res = "classE\n"
        
        return res
    
        
    def matriceConfusionFonction(self,k) :
        count = 0
        self.distancefonction([6.1, 3.0, 4.9, 1.8, 2, 16, 'ClassE\n']) #permet de remplir self.classA,...,self.classE
        #Le choix de l'individu n'importe pas, les valeurs des distances seront écrasées pas la suite.
        self.matriceConfusion = []
        self.kMeilleurIndividu(k) #On initialise self.listIndividu contenant tous les individus candidats à être les plus proche voisins, les autres valeurs seront écrasées par la suite
        for ind in self.listIndividuVerification:
            self.distancefonction(ind)
            self.kMeilleurIndividu(k)
            if ( ind[6] == self.classLaPlusFrequente(k) ):
                self.matriceConfusion.append("+")
            else :
                self.matriceConfusion.append("-")
                count += 1
        return count/len(self.listIndividuVerification)
    
    def matricePredictionClassFonction(self,k) :
        self.matricePredictionClass = []
        count = 0
        self.distancefonction([6.1
                               , 3.0, 4.9, 1.8, 2, 16, 'ClassE\n']) #permet de remplir self.classA,...,self.classE
        #Le choix de l'individu n'importe pas, les valeurs des distances seront écrasées pas la suite.
        self.matriceConfusion = []
        self.kMeilleurIndividu(k) #On initialise self.listIndividu contenant tous les individus candidats à être les plus proche voisins, les autres valeurs seront écrasées par la suite
        for ind in self.listIndividuVerification:
            self.distancefonction(ind)
            self.kMeilleurIndividu(k)
            self.matricePredictionClass.append(self.classLaPlusFrequente(k))
            
    def ecritureFichierReponse(self):
        f = open("D:\\IA\\finalTest.txt",'r')
        fi =  open("D:\\IA\\messaoudi_rayan_sample.txt",'w')
        lines = f.readlines()
        i = 0
        for l in lines:
            fi.write(self.matricePredictionClass[i])
            i += 1

        f.close()
        fi.close()
        
        
        
    
    
    def run(self):
        
        temps1 = time.time()
        
        k = 1
        # self.matriceConfusionFonction(k)
        self.matricePredictionClassFonction(k)
        # print(self.matriceConfusionFonction(k))
        # print(self.matriceConfusion)
        print(self.matricePredictionClass)
        #print(self.listIndividu)
        self.ecritureFichierReponse()
        
        
        #print(self.classB2)
        # ind = [6, 11, 0, 2, 3, 5, 'classA']
        # self.distancefonction(ind)
        
        # a = self.kMeilleurIndividu(k)
        # print(a)
        # print(self.classLaPlusFrequente(k))
        # print(sorted(self.distance_virginica))
        # print(sorted(self.distance_versicolor))
        # print(sorted(self.distance_setosa))
        


       
        temps2 = time.time()
        
        print("Temps d'execution :",temps2-temps1)


        
    
    

    
    





if __name__ == '__main__' :
    knn = knn()
    #pour générer un problème
    knn.run()
