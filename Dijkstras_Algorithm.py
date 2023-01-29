# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 07:52:46 2023

@author: Sriram Ananthakrishna
"""



def addEdge(adj, u, v, wt):
    
    if u not in adj:
        adj[u] = []
    if v not in adj:
        adj[v] = []
    
    adj[u].append([v, wt])
    return adj


adj = {}
    
adj = addEdge(adj,1, 2,4)
adj = addEdge(adj,1, 4, 7)
adj = addEdge(adj,1, 6, 8)
adj = addEdge(adj,1, 8, 9)
adj = addEdge(adj,2, 4, 7)
adj = addEdge(adj,4, 6, 12)
adj = addEdge(adj,8, 6, 6)
adj = addEdge(adj,2, 3, 11)
adj = addEdge(adj,4, 3, 5)
adj = addEdge(adj,4, 5, 10)
adj = addEdge(adj,6, 5, 16)
adj = addEdge(adj,6, 7, 15)
adj = addEdge(adj,7, 8, 11)
adj = addEdge(adj,8, 9, 12)
adj = addEdge(adj,3, 5, 10)
adj = addEdge(adj,9, 7, 9)
adj = addEdge(adj,3, 10, 16)
adj = addEdge(adj,5, 10, 8)
adj = addEdge(adj,7, 10, 4)
adj = addEdge(adj,9, 10, 14)

visited = []
unvisited = [1,2,3,4,5,6,7,8,9,10]

start_node = 1
end_node = 10

import pandas as pd
import numpy as np
from copy import deepcopy



# iteration 1

# from start node, see the adjacent nodes




def Dijkstras(start_node, end_node):
    
    table = pd.DataFrame({'Nodes':unvisited})
    table['shortest'] = [np.inf]*len(unvisited)
    table['previous'] = [np.nan]*len(unvisited)
    table["shortest"][table.loc[table['Nodes'] == start_node].index] = 0
    
    
    table2 = deepcopy(table)
    
    in_process = list(table['Nodes'][table.loc[table['shortest'] == min(table['shortest'])].index])[0]
    
    # loop through unvisited nodes
    while unvisited:
        # looping through the adjacent nodes
        for i in range(len(adj[in_process])):
        
            # updating the distance if and only if the distance is greater
            if adj[in_process][i][0] not in visited:
                if float(table['shortest'][table.loc[table['Nodes'] == adj[in_process][i][0]].index]) > int(table['shortest'][table.loc[table['Nodes'] == in_process].index] + adj[in_process][i][1]):
                    table['shortest'][table.loc[table['Nodes'] == adj[in_process][i][0]].index] = table['shortest'][table.loc[table['Nodes'] == in_process].index]+ adj[in_process][i][1]
                    table2['shortest'][table2.loc[table['Nodes'] == adj[in_process][i][0]].index] = table['shortest'][table.loc[table['Nodes'] == in_process].index]+ adj[in_process][i][1]
        
                # # updating the prev node if and only if the distance is greater
                    table['previous'][table.loc[table['Nodes'] == adj[in_process][i][0]].index] = in_process
                
        # update the visited nodes
        visited.append(in_process)
        
        
        
        # update the table2
        table2 = table2[table2.Nodes != in_process]
        
        
        unvisited.remove(in_process)    
        
        # update the in_process node (if 2 or more nodes with the same dist exist, choose the first one) 
        if len(table2) != 0:
            in_process = list(table['Nodes'][table.loc[table['shortest'] == min(table2['shortest'])].index])[0]
        
    
    return int(table["shortest"][table.loc[table['Nodes'] == end_node].index])

Dijkstras(start_node, end_node)
