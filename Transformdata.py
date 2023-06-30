import Data as dt

class Transform():
    
    def __init__(self,distrito) -> None:
        self.data= dt.Data(distrito)
        self.nodes= self.create_id(self.data.get_nodes())
        self.listadjacency=self.create_adjacencylist(self.nodes,self.data.get_edges())
        self.nodes_coordenadas=self.data.get_data()
    
    def create_id(self,nodes):
         nodos={value:i for i,value in enumerate(nodes)}
         return nodos
    
    def  create_adjacencylist(self,nodes,edges):
         lista =[]
         fil=[]   
         for v in nodes.keys():
             for edge in edges:
                 if v == edge[0]:
                    fil.append(nodes[edge[1]])
             lista.append(fil.copy())
             fil.clear()    
         return lista
    
    def get_listadjancecy(self):
        return self.listadjacency
    
    def get_nodes(self):
        return self.nodes
    
    def get_coordenadas(self):
        return self.nodes_coordenadas   