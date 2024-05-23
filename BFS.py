import pandas as pd
from collections import deque
############################################################################################################################
d_df = pd.read_excel('Province_Center_Distance.xlsx')
a_df = pd.read_excel('Adjacent_Cities.xlsx')
############################################################################################################################
class Node:
    
    def __init__(self,name,parent):                                             #type(name)=string   type(parent=object)
        self.name = name
        self.parent = parent
            
  ###########################################          
    def __eq__(self, o):
        return self.name == o.name
    
  ###########################################  
    def get_neighbours(self):                                                   # returns a list of neighbors name
        index=0
        l = []
        
        for i in a_df[self.name]:
            if i==1:
                l.append(a_df.columns[index+1])
            index +=1
            
        return l
   
    
############################################################################################################################
def distance(city1,city2):
    for idex,item in enumerate(d_df.columns):
        if item == city1:
            return d_df[city2][idex-1]  


############################################################################################################################
def expand(open_list,current_node,closed_list,target):

    children_list = current_node.get_neighbours()
               
    closed_list_name = []
    for node in closed_list:
        closed_list_name.append(node.name)

            
    for i in children_list:   
        child= Node(i,current_node)
        open_list.append(child)
      
        
############################################################################################################################
def BFS_Search(start, target):        # start and target are the name of the cities
    
    open_list = deque([])                        
    closed_list = []               
    
    start_node = Node(start,None)
    target_node = Node(target,None)
    
    open_list.append(start_node)
    
    
    
    while len(open_list) > 0:
        
####################################################  Selecting best node for expansion

        current_node = open_list.popleft()
        
        closed_list.append(current_node)

####################################################  Goal Test

        if current_node == target_node:
            
            Solution = []
            Solution.append(current_node.name)
            target_node = current_node
            while current_node.parent is not None:
                current_node = current_node.parent
                Solution.append(current_node.name)
                
            d = 0
            
            for i in range(len(Solution)-1):
                d = d + distance( Solution[i] , Solution[i+1] )
                
                
            return Solution[::-1] , d
                                        
#################################################### finding children of current_node        
        expand(open_list,current_node,closed_list,target)
        
    return False
############################################################################################################################      

start = input('naame shahre shoroe safar: ')
target = input('naame shahre maghsad: ')

print(BFS_Search(start , target))
























