import os
scale,targetround=input("scale,targetround:").split(' ')
size,round=input("herdsize,round:").split(' ')
print("EXECUTING...\n python d:\\gurobi\\win64\\examples\\python\\tsp.py {}".format(scale))
os.system("python d:\\gurobi\\win64\\examples\\python\\tsp.py {}".format(scale))
print("EXECUTING...\n python d:\VS_C\Projects\Math_model\Gurobi\TSP_gene_integrated.py {}".format(targetround))
os.system("python d:\VS_C\Projects\Math_model\Gurobi\TSP_gene_integrated.py {} {} {}".format(targetround,size,round))
