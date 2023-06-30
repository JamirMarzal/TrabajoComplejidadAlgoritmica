from tkinter import messagebox, ttk
import tkinter as tk
import Transformdata as td
import Algorithms as alg
import folium
from webbrowser import open_new_tab

class Application(ttk.Frame):
    
    def __init__(self):
        self.window=tk.Tk()   
       
    def create_interface(self,window):
        super().__init__(window)
        window.title("Generador de Rutas")
        window['background']='#856ff8'
        self.combo = ttk.Combobox(
           self,
           state="readonly",
           values=["Lince", "San Borja", "San Luis", "Surquillo"]
        )
        self.combo.place(x=85, y=50)
        self.button1 = ttk.Button(
            text="route dfs",
            command=lambda: self.draw_map_factory(self.combo.get(),True)
        )
        self.button1.place(x=50, y=120)
        self.button2 = ttk.Button(
            text="route bfs",
            command=lambda: self.draw_map_factory(self.combo.get(),False)
        )
        self.button2.place(x=180, y=120)       
        self.button3 = ttk.Button(
            text="cerrar",
            command=self.window.quit
        )
        self.button3.place(x=110, y=170)
        window.config(width=300, height=200)
        self.place(width=300, height=200)
        window.mainloop()
            
    def draw_map_factory(self,distrito,dfs):
        if distrito != '':
            if distrito =='Lince':
                self.draw_map((-12.0831811,-77.0273030),'Lince, Lima, Perú','Comisaria Lince',dfs)
            elif distrito == 'San Borja':
                self.draw_map((-12.1054560,-76.9990935),'San Borja, Lima, Perú','Comisaria San Borja',dfs)
            elif distrito == 'San Luis':
                self.draw_map((-12.0730224,-76.9996050),'San Luis, Lima, Perú','Comisaria San Luis',dfs)       
            else:
                self.draw_map((-12.1187129,-77.0221336),'Surquillo, Lima, Perú','Comisaria Surquillo',dfs)
            open_new_tab('map.html')    
    
    def  run(self):       
        self.create_interface(self.window)        
    
    def draw_map(self,coordenadas,distrito,marcador,dfs):
        grafo= td.Transform(distrito)
        route = alg.Algorithms(grafo.get_listadjancecy(),5)
        data= grafo.get_coordenadas()
        orig_coord = coordenadas
        m = folium.Map(location=[orig_coord[0], orig_coord[1]], zoom_start=15, control_scale=True)
        folium.Marker(
        [orig_coord[0],orig_coord[1]], popup=marcador).add_to(m)
        if dfs: lista= route.get_route_dfs()
        else: lista=route.get_route_bfs()
        for u, v in enumerate(lista):
            if v > 0:
                folium.PolyLine(locations=[(data[u]['y'], data[u]['x']), (data[v]['y'], data[v]['x'])],
                        color='red').add_to(m)
        m.save('map.html')
            