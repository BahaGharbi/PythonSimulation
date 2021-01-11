#Baha Gharbi 03/19/2020
#Link:https://youtu.be/MI65xLMDEW8
#"I have not given or received any unauthorized assistance on this assignment.”
import numpy as np
import random
import matplotlib.pyplot as plt
class Island():
        'creating an island'
        global d,RainToday,Area,RainChance
        def __init__(self):
            pass
        def rain(self):
            'rain in the island'
            ProbRain=random.random()
            if ProbRain<=RainChance:
               self.RainToday= np.random.normal(RainMean, RainStd) #normal distribution
            else:
              self.RainToday=0
            return self.RainToday 
class Berry():
    'planting berries'
    global BerrDic,berriNum
    def __init__(self):
         pass
    def plant(self):
                'growing berries'
                i=Island()
                self.berriNum=int(i.rain()*Area*BerriesCoff) #number of berries
                return self.berriNum
    def Berrdic(self):
         'creating a dict of berries'
         for i in range(0, self.berriNum):
           BerrDic[len(BerrDic)]=1
         return BerrDic  #dict of berries
    def BerrAge(self):
      'tracking the age of berries'
      for i in list(BerrDic.keys()):
            if BerrDic[i]==BerrLifSpan: 
                BerrDic.pop(i)#throw away if rotten
            else:
               BerrDic[i]+=1  #add 1 to its age
      return BerrDic
class Rats():
    'creating rats'
    global RatNum,RatAge
    def __init__(self):
        pass
    def RatDic(self):
        ' creating a dict of Rats'
        for i in range(RatNum):
            self.RatAge=random.randint(1,RatageMax)
            RatDic[len(RatDic)]=[self.RatAge,0,0] #dict of rats with one key and 3 values: age, berries eaten, dayswithoutfood
        return RatDic  
    def RatsAge(self):
      'tracking the age of the rats'
      for i in list(RatDic.keys()):
            RatDic[i][0]+=1 #modifying the age
      return RatDic 
    def RatEat(self):
        'tracking the number of berries the rats ate'
        self.ratate=[]
        for j in list(RatDic.keys()):
                if len(RatDic)>0:
                   rat=random.choice(list(RatDic.keys())) #randomly choose a rat to eat a berry
                   if len(BerrDic)>0:
                        RatDic[rat][1]+=1
                        RatDic[rat][2]=0
                        self.ratate.append(rat)
                        BerrDic.popitem() #remove a berry from the dict
        for i in list(RatDic.keys()):
            if i not in self.ratate:
                  RatDic[j][2]+=1 #modifying the dayswithoutfood parameter
        return RatDic
    def RatDie(self):
        'tracking how the rats die'
        for i in list(RatDic.keys()):
             if RatDic[i][2]==RatnoFood: 
                del RatDic[i]  #removing the rats that went 3 consecutive days without food
             elif RatDic[i][0]>=RatOld:
                probtoDie=((RatDic[i][0]-RatOld)+1)*0.05
                if probtoDie>=random.random():
                    del RatDic[i]  #removing the rats that die of old age
        return RatDic
    def RatReproduce(self):
        'reproducing more rats'
        for i in list(RatDic.keys()):
            if RatDic[i][1]>RatBerrMin: 
                if (RatDic[i][1]-RatBerrMin)%RatBerrProd==0: 
                    RatLitter=random.randint(RatLittMin,RatLittMax) #reproducing a litter between 6 and 10 everytime a rat eat 8 berries after 10
                    for i in range(RatLitter):
                       RatDic[len(RatDic)]=[1,0,0]
        return RatDic
class Cats():
    'creating cats'
    global RatNum,CatAge
    def __init__(self):
            pass
    def CatDic(self):
        'creating a dict of cats'
        for i in range(CatNum):
            CatAge=random.randint(1,CatageMax)
            CatDic[len(CatDic)]=[CatAge,0,0] # dict of cats with one key and 3 values: age, rats eaten, dayswithoutfood
        return CatDic
    def CatsAge(self):
        'tracking the age of the cats'
        for i in list(CatDic.keys()):
            CatDic[i][0]+=1 #modifying the age
        return CatDic
    def CatEat(self):
        'tracking the number of rats cats ate'
        global RatNum
        self.Catate=[]
        for j in list(CatDic.keys()):
                cat=random.choice(list(CatDic.keys())) #randomly choose a cat to eat a rat
                Hunt=0
                Exp=CatDic[cat][0]*Addprob
                if Hunt<1 and Exp<1:
                    Hunt=(RatNum/Area)*probtoCatch+Exp
                else:
                    Hunt=1
                if Hunt>random.random():
                        CatDic[cat][1]+=1 
                        CatDic[cat][2]=0
                        self.Catate.append(cat)
                        if len(RatDic)>0:
                           RatDic.popitem()
        for i in list(CatDic.keys()):
          if i not in self.Catate:
                CatDic[i][2]+=1  #modifying the dayswithoutfood parameter
        return CatDic
    def CatDie(self):
        'tracking how the cats die'
        for i in list(CatDic.keys()):
             if CatDic[i][2]==CatnoFood: 
                del CatDic[i]  #removing the cats that went 5 consecutive days without food
             elif CatDic[i][0]>=CatOld:

                probtoDie1=(CatDic[i][0]-CatOld)*0.1+0.01
                if probtoDie1>=random.random():
                    del CatDic[i]  #removing the cats that die of old age
        return RatDic
    def CatReproduce(self):
        'reproducing more cats'
        for i in list(CatDic.keys()):
            if CatDic[i][1]>CatRatMin:
                if (CatDic[i][1]-CatRatMin)%CatRatProd==0:
                    CatLitter=random.randint(CatLittMin,CatLittMax)
                    for i in range(CatLitter): #reproducing a litter between 3 and 6 everytime a rat eat 35 berries after 50
                        CatDic[len(CatDic)]=[1,0,0]  
        return CatDic
def IslandofRatsandCats():
        Readfile()
        SurvivalIsland()
        plot()
def SurvivalIsland():
 ' playing the survival island game'
 global d, BerrDic,RatDic,CatDic, RatNum, Area, RainToday,RainList,berriNum
 global RainChance,RainMean,RainStd, BerriesCoff,BerrLifSpan,RatNum,RatageMax
 global RatnoFood,RatOld,RatBerrMin,RatBerrProd,RatLittMin,RatLittMax,CatNum,CatageMax,probtoCatch
 global Addprob, CatnoFood, CatOld ,CatRatMin, CatRatProd, CatLittMin, CatLittMax
 global DayList, RainList,BerryList,RatList,CatList
 d=0
 RainToday=0
 berriNum=0
 BerrDic={}
 RatDic={}
 CatDic={}
 RainList=[]
 BerryList=[]
 RatList=[]
 CatList=[]
 DayList=[]
 i=Island()
 b=Berry()
 r=Rats()
 c=Cats()
 r.RatDic()
 c.CatDic()
 while d<100: #simulating the experience d days
    DayList.append(d)
    BerryList.append(len(BerrDic))
    RatList.append(len(RatDic))
    CatList.append(len(CatDic))
    berriNum=int(b.plant())
    if berriNum>0:
            b.Berrdic()
            r.RatEat()
            b.BerrAge()
    if len(RatDic)>0:
        r.RatsAge()
        r.RatDie()
        r.RatReproduce()
        c.CatEat()
    if len(CatDic)>0:
       c.CatsAge()
       c.CatDie()
       c.CatReproduce()
    RainToday=i.rain()
    RainList.append(RainToday)
    d+=1
def plot():
 'ploting a graph of the rain, numbers of berries, number of rats, and number of cats throught the simulation period'
 plt.figure(1)
 plt.subplot(111)
 plt.plot(DayList, RainList,'r--')
 plt.figure(2)
 plt.plot( DayList,BerryList,'y--')
 plt.figure(3)
 plt.subplot(111)
 plt.plot(DayList,RatList,'bs')
 plt.figure(4)
 plt.subplot(111)
 plt.plot(DayList,CatList,'b--')
 plt.show()
def Readfile():
   'reading the file of the parameters'
   global d, BerrDic,RatDic,CatDic, RatNum, Area, RainToday,berriNum
   global RainChance,RainMean,RainStd, BerriesCoff,BerrLifSpan,RatNum,RatageMax
   global RatnoFood,RatOld,RatBerrMin,RatBerrProd,RatLittMin,RatLittMax,CatNum,CatageMax,probtoCatch
   global Addprob, CatnoFood, CatOld ,CatRatMin, CatRatProd, CatLittMin, CatLittMax
   infile=open('Parameters.txt','r')
   NumList=[]
   m=1
   while infile and m>0:
         lineList=infile.readline()
         lineList=str(lineList.split(' \n'))
         lineList= lineList.replace(' ', '')[:-4]
         lineList = lineList.replace(' ', '')[2:]
         m=lineList.find('=')
         NumList.append(lineList[m+1:])
   Area=int(NumList[0])
   RainChance=float(NumList[1])
   RainMean=int(NumList[2])
   RainStd=int(NumList[3])
   BerriesCoff=int(NumList[4])
   BerrLifSpan=int(NumList[5])
   RatNum=int(NumList[6])
   RatageMax=int(NumList[7])
   RatnoFood=int(NumList[8])
   RatOld=int(NumList[9])
   RatBerrMin=int(NumList[10])
   RatBerrProd=int(NumList[11])
   RatLittMin=int(NumList[12])
   RatLittMax=int(NumList[13])
   CatNum=int(NumList[14])
   CatageMax=int(NumList[15])
   probtoCatch=float(NumList[16])
   Addprob=float(NumList[17])
   CatnoFood=int(NumList[18])
   CatOld=int(NumList[19])
   CatRatMin=int(NumList[20])
   CatRatProd=int(NumList[21])
   CatLittMin=int(NumList[22])
   CatLittMax=int(NumList[23])


    
