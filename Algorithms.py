
class Algorithms():
    
    def __init__(self,g,s) -> None:
        self.route_dfs= self.dfs(g,s)
        self.route_bfs=self.bfs(g,s)
    
    def dfs(self,G,s):
        n=len(G)
        parent=[-1]*n
        visited=[False]*n
        visited[s]=True
        def _dfs(G,s,parents,visiteds):
          for value in G[s]:
            if not visited[value]:
              visiteds[value]=True
              parents[value]=s
              _dfs(G,value,parents,visiteds)
          return parents    
        return _dfs(G,s,parent,visited)

    def bfs(self,G,s):
        n=len(G)
        parent=[-1]*n
        visited=[False]*n
        visited[s]=True
        cola=[s]
        while cola:
          nodo=cola.pop(0)
          for value in G[nodo]:
            if not visited[value]:
              visited[value]=True
              parent[value]=nodo
              cola.append(value)
        return parent
    
    def get_route_dfs(self):
        return self.route_dfs
    
    def get_route_bfs(self):
        return self.route_bfs
    