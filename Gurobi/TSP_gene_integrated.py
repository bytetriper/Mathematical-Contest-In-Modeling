from sys import argv
import TSP_gene
assert(len(argv)>1)
bestans=100000
for i in range(int(argv[1])):
    tmp=fg=0
    if(len(argv)!=4):
        tmp,fg=TSP_gene.solve("d:\\VS_C",20000,200,True)
    else:
        tmp,fg=TSP_gene.solve("d:\\VS_C",int(argv[2]),int(argv[3]),True)
    bestans=min(bestans,tmp)
    if fg:
        print("Found Optimized Ans {} on {}th run".format(tmp,i))
        exit(0)
print("Current Bestans:{}".format(bestans))
