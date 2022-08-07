
from cgi import test
from copy import deepcopy
import os
from random import randrange
from wsgiref import headers
import numpy
import pickle
import heapq
class Individual:
    def __init__(self,maxnum,dis):
        self.gene=numpy.arange(maxnum)
        self.siz=maxnum
        self.dis=dis
        numpy.random.shuffle(self.gene)
        #print(self.gene)
    def value(self):
        assert(self.siz>0)
        cost=0
        for i in range(self.siz-1):
            cost+=self.dis[(self.gene[i],self.gene[i+1])]
        cost+=self.dis[(self.gene[self.siz-1],self.gene[0])]
        return cost
    def change(self,t1,t2):
        self.gene[t1],self.gene[t2]=self.gene[t2],self.gene[t1]
    def evolve(self):
        t1=numpy.random.randint(0,self.siz)
        t2=numpy.random.randint(0,self.siz)
        self.change(t1,t2)
        return
    def __lt__(self,other):
        return self.value()<other.value()

    def mate(self):
        st=numpy.random.randint(1,self.siz-1)
        arr=numpy.zeros(self.siz,dtype=numpy.int_)
        arr[0:self.siz-st]=self.gene[st:self.siz]
        arr[self.siz-st:self.siz]=self.gene[0:st]
        son=Individual(self.siz,self.dis)
        son.gene=arr
        return son
class herd:
    Evolve_Chance=0.5
    INF=10000000
    def generate_possibility(self):
        sum=0
        for indv in self.herds:
            sum+=indv[1]
        print(sum)
        self.possibility=[]
        for indv in self.herds:
            self.possibility.append(indv[1]/sum)
        return
    def __init__(self,initnum,maxnum,dis) -> None:
        self.herds=[]
        self.herdsiz=initnum
        self.ans=herd.INF
        self.roundcnt=0
        print("Initing... Herdsiz:{} scale:{}".format(initnum,maxnum))
        for i in range(initnum):
            tmp=Individual(maxnum,dis)
            self.herds.append((tmp.value(),tmp))
            #print(tmp.value())
        heapq.heapify(self.herds)
    def upd(self,for_test=False):
        for i in range(self.herdsiz//2):
            birth=self.herds[i][1].mate()
            if numpy.random.random()<herd.Evolve_Chance:
                birth.evolve()
            heapq.heappush(self.herds,(birth.value(),birth))
        self.ans=min(self.ans,self.herds[0][0])
        self.roundcnt+=1
        if for_test:
            print("round{}".format(self.roundcnt))
            for i in self.herds:
                print(i[1].gene)
                print("value:{}".format(i[0]))
        del self.herds[self.herdsiz:]
def solve(config,herdsize=20000,round=200,for_test=False):
    file=open(config+"\input.pkl","rb")
    dis={}
    targetans,n=pickle.load(file)
    dis=pickle.load(file)
    if for_test:
        print("Targetans:{}\nproblem scale:{}".format(targetans,n))
    for i in range(n):
        dis[(i,i)]=100000
        for j in range(i+1,n):
            dis[(i,j)]=dis[(j,i)]
    print(n)
    divs=herd(herdsize,n,dis)
    upperbound=2.0
    tolerence=1e-4
    fg=False
    maxround=round
    for i in range(maxround):
        divs.upd()
        if(divs.ans<targetans*upperbound):
            upperbound=(upperbound+1)/2
            if for_test:
                print("In round {}:Ans {:.3f} limited to targetans*{:.5f} ".format(i,divs.ans,divs.ans/targetans))
            if(divs.ans<targetans+tolerence):
                if for_test:
                    print("Found Optimized Ans {} at Round {} \n Terminated".format(divs.ans,i))
                fg=True
                break
    if fg==False:
        if for_test:
            print("Unable to Find Optimized Ans within {} rounds\n Final ans:{}".format(maxround,divs.ans))
        return divs.ans,False
    return divs.ans,True
if __name__=="__main__":
    solve("d:\\VS_C",True)