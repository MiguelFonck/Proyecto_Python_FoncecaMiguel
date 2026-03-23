import os
import json


ARCHIVO="simulador_de_gastos_diarios.json"


def cargar_gastos():
    if os.path.exists(ARCHIVO): 
        with open (ARCHIVO,"r") as file:
            return json.load(file)
    else:
        return[]
    
def guardar_gastos (gastos):
    with open (ARCHIVO, "w") as file:
        json.dump(gastos,file,indent=4)
        

