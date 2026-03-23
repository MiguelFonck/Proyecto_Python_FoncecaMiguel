from datetime import datetime

def listar_gastos (gastos):
    
    if not gastos:
        print("No hay gastos registrados")
        return
    
    print("="*35)
    print ("LISTAR GASTOS".center(35))
    print("="*35)
    print ("""Ingrese una opcion para filtrar los gastos:
            1. Ver todos los gastos
            2. Filtrar por categoría
            3. Filtrar por rango de fechas
            4. Regresar al menú principal""")
    print("="*35)
    
    try:
        opcion = int(input(""))
    except ValueError:
        print("Entrada no válida")
        return
    
    
    

    if opcion == 1:
        
        for i in gastos:
            print(f"Fecha      : {i['fecha']}")
            print(f"Monto      : ${i['monto']}")
            print(f"Categoría  : {i['categoria']}")
            print(f"Descripción: {i['descripcion']}")
            print("-" * 30)
        
        
            
             
    elif opcion ==2: 
        
        print("="*35)
        print("FILTRAR POR CATEGORIA".center(35))
        print ("""Seleccione categoría:
        1. Comida
        2. Transporte
        3. Entretenimiento
        4. Otros""")
        print("="*35)
        
        try:
            opcion2 = int(input(""))
        except ValueError:
            print("Entrada no válida")
            return
        
        
        if opcion2==1:
            categoria_final= "comida" 

        elif opcion2==2: 
            categoria_final="transporte"      
                       
        elif opcion2==3: 
            categoria_final="entretenimiento"
               
        elif opcion2==4:
            categoria_final="otros"
               
        else:
            print ("Opcion no valida")
            return
        
            
        encontrado=False  
            
        for o in gastos:
            if o["categoria"] == categoria_final:
                
                encontrado = True
                
                print(f"Fecha      : {o['fecha']}")
                print(f"Monto      : ${o['monto']}")
                print(f"Categoría  : {o['categoria']}")
                print(f"Descripción: {o['descripcion']}")
                print("-" * 30)
        
        if not encontrado:
            print("No hay gastos en esta categoría.")
            
            
            
            
            
            
    elif opcion==3:
       
        fecha_inicio=input("""Digite la fecha inicial:
                           Ejemplo:
                           YYYY-MM-DD""")
        fecha_final=input("""Digite la fecha final:
                           Ejemplo:
                           YYYY-MM-DD""")
        
        print("="*35)
        print("FILTRO POR FECHA") 
        print("="*35)
         
        try:
            fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
            fecha_final=datetime.strptime(fecha_final, "%Y-%m-%d")
        except ValueError:
            print("Entrada no válida")
            return
        if fecha_inicio>fecha_final:
            print ("La fecha inicial no puede ser mayor a la fecha final")
            return
        
        encontrado=False
            
        for i in gastos:
            fecha_gasto=datetime.strptime(i["fecha"], "%Y-%m-%d")
            if fecha_inicio <= fecha_gasto <= fecha_final:
                encontrado=True
                print(f"Fecha      : {i['fecha']}")
                print(f"Monto      : ${i['monto']}")
                print(f"Categoría  : {i['categoria']}")
                print(f"Descripción: {i['descripcion']}")
                print("-" * 30)
            
        if not encontrado: 
                print ("No hay gastos en este rango de fechas")
        
        
        
        
        
    elif opcion==4:
        
        print("Regresando al menu principal...")
        return
    
    
    else: 
        print("Opcion no valida")
        return