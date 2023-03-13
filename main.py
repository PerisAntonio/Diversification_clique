import pandas as pd
import numpy as np
import networkx as nx
import random

def run(input_data, solver_params, extra_arguments):
    corr = np.array(input_data['corr'])
    names = input_data["labels"]
    threshold = input_data["threshold"]
    df=pd.DataFrame(corr,columns=names,index=names)
    df[df<-threshold]=np.nan
    df[df>threshold]=np.nan
    
    G=nx.Graph()
    d={c:[x for x in df[c].dropna().index if c<x] for c in df.columns}
    for t in d:
        for u in d[t]:
            G.add_edge(t,u)
    r=[]
    otras=[]
    res=nx.enumerate_all_cliques(G)
    for x in res:
        if(len(x)>len(r)):
            r=x
            otras=[]
        elif (len(x)==len(r)):
            otras.append(x)
    otras.append(r)
    result={}
    result['Labels']=random.choice(otras)
    result['Length']=len(result['Labels']

    return result
