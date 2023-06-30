import osmnx as ox
import networkx as nx

class Data():
    
    def __init__(self,distrito) -> None:        
        self.G = ox.graph_from_place(distrito, network_type="drive")
        self.info = nx.node_link_data(self.G)
        self.data=self.info['nodes']
    
    def get_data(self):
        return self.data
    
    def get_nodes(self):
        return self.G.nodes()
    
    def get_edges(self):
        return self.G.edges()
            