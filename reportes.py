import json
import os
from datetime import datetime, timedelta

def generar_reporte(gastos): 
    
    if not gastos:
        print("No hay gastos registrados")
        return   
      
    fechas_diarias=[]
    fechas_semana=[]
    fechas_mensual=[]

      
    print("="*35)
    print ("Generar Reporte de Gastos".center(35))
    print("="*35)
    print ("""Seleccione el tipo de reporte:
           1. Reporte diario
           2. Reporte semanal
           3. Reporte mensual
           4. Regresar al menú principal""")
    print("="*35)
    
    
    try:
        opcion = int(input(""))
    except ValueError:
        print("Entrada no válida")
        return
    
    
#REPORTE DIARIO################################################################################################################################
   
               
    if opcion ==1:
        nombre_reporte="reporte_diario"
        suma_total=0
        totales_categoria={"comida":0,
                           "transporte":0,
                           "entretenimiento":0,
                               "otros":0}
        
        fecha_hoy=datetime.now()
        fecha_hoy_str= fecha_hoy.strftime("%Y-%m-%d")
        for i in gastos:
            categoria=i["categoria"]
            monto=i["monto"]
            fecha_gastos = i["fecha"]
            if fecha_hoy_str==fecha_gastos:
            
               fechas_diarias.append(i)
               totales_categoria[categoria] += monto
               suma_total=suma_total+monto
        
        if not fechas_diarias:
                    print("No hay gastos en estas fechas")
                        
        reporte={"tipo_reporte":nombre_reporte,
             "cantidad_gastos":len(fechas_diarias),
             "total_gastado":suma_total,
             "total_gastado_categoria":totales_categoria,
             "gastos":fechas_diarias
        }
        
        
        print("="*45)
        print("OPCIONES REPORTE".center(35))
        print("="*45)
        print("Seleccione una opcion")
        print("""1.Ver reporte en pantalla
2.Guardar reporte en archivo json
              """)
        
          
        try:
            opcion2 = int(input(""))
        except ValueError:
            print("Entrada no válida")
            return
               
        if opcion2 ==1:
            print(f"Tipo de reporte:{reporte['tipo_reporte']}")
            print(f"Cantidad de gastos:{reporte['cantidad_gastos']}")
            print(f"Total gastado:{reporte['total_gastado']}")
            print("Total gastado por categoria")
            for i in totales_categoria:
                print(f"{i}:${totales_categoria[i]}")
            print("-" * 30)
            print(f"Total gastado:{reporte['total_gastado']}")
            
            for i in fechas_diarias:
                print(f"Fecha      : {i['fecha']}")
                print(f"Monto      : ${i['monto']}")
                print(f"Categoría  : {i['categoria']}")
                print(f"Descripción: {i['descripcion']}")
                print("-" * 30)
        
            
        if opcion2 ==2: 
            ARCHIVO="reporte_diario.json"
            with open (ARCHIVO, "w") as file:
                json.dump(reporte,file,indent=4)
        
            print("Archivo creado con exito")
            
        
            
#REPORTE SEMANAL################################################################################################################################   
    
    elif opcion==2:
        nombre_reporte="reporte_semanal"
        suma_total=0
        totales_categoria={"comida":0,
                           "transporte":0,
                           "entretenimiento":0,
                               "otros":0}
    
        fecha_semana=datetime.now()
        fecha_inicio=fecha_semana-timedelta(days=7)
        
        for i in gastos:
            categoria=i["categoria"] 
            monto=i["monto"]
            fecha_gastos=datetime.strptime(i["fecha"],"%Y-%m-%d")
    
            if fecha_inicio.date() <= fecha_gastos.date() <= fecha_semana.date():
                totales_categoria[categoria] += monto 
                fechas_semana.append(i)
                suma_total=suma_total+monto
        if not fechas_semana:
                    print("No hay gastos en estas fechas")
                
        
        reporte={"tipo_reporte":nombre_reporte,
             "cantidad_gastos":len(fechas_semana),
             "total_gastado":suma_total,
             "total_gastado_categoria":totales_categoria,
             "gastos":fechas_semana
        }
            
            
            
        
        print("="*45)
        print("OPCIONES REPORTE".center(35))
        print("="*45)
        print("Seleccione una opcion")
        print("""1.Ver reporte en pantalla
2.Guardar reporte en archivo json
              """)
        
      
            
        try:
            opcion3 = int(input(""))
        except ValueError:
            print("Entrada no válida")
            return
        
        if opcion3==1:
            print(f"Tipo de reporte:{reporte['tipo_reporte']}")
            print(f"Cantidad de gastos:{reporte['cantidad_gastos']}")
            print(f"Total gastado:{reporte['total_gastado']}")
            print("Total gastado por categoria")
            for i in totales_categoria:
                print(f"{i}:${totales_categoria[i]}")
            print("-" * 30)
            print(f"Total gastado:{reporte['total_gastado']}")
            
            for i in fechas_semana:
                print(f"Fecha      : {i['fecha']}")
                print(f"Monto      : ${i['monto']}")
                print(f"Categoría  : {i['categoria']}")
                print(f"Descripción: {i['descripcion']}")
                print("-" * 30)
        
            
        if opcion3 ==2: 
            ARCHIVO="reporte_semanal.json"
            with open (ARCHIVO, "w") as file:
                json.dump(reporte,file,indent=4)
        
            print("Archivo creado con exito")
            
            
               
                
#REPORTE MENSUAL################################################################################################################################
    
    elif opcion==3:
        
        nombre_reporte="reporte_mensual"
        suma_total=0
        totales_categoria={"comida":0,
                           "transporte":0,
                           "entretenimiento":0,
                               "otros":0}
        
        fecha_mes=datetime.now().date()
        fecha_inicio=fecha_mes-timedelta(days=30)
        
        for i in gastos: 
            categoria=i["categoria"]
            monto=i["monto"]
            fecha_gastos=datetime.strptime(i["fecha"],"%Y-%m-%d").date()
    
            if fecha_inicio <= fecha_gastos <= fecha_mes:
                 totales_categoria[categoria] += monto
                 suma_total += monto 
                 fechas_mensual.append(i)
                
        if not fechas_mensual:
            print("No hay gastos en estas fechas")
            
        reporte={"tipo_reporte":nombre_reporte,
             "cantidad_gastos":len(fechas_mensual),
             "total_gastado":suma_total,
             "total_gastado_categoria":totales_categoria,
             "gastos":fechas_mensual
        }
            
            
        print("="*45)
        print("OPCIONES REPORTE".center(35))
        print("="*45)
        print("Seleccione una opcion")
        print("""1.Ver reporte en pantalla
2.Guardar reporte en archivo json
              """)
        
        
        try:
            opcion4 = int(input(""))
        except ValueError:
            print("Entrada no válida")
            return
        
        if opcion4==1:
            print(f"Tipo de reporte:{reporte['tipo_reporte']}")
            print(f"Cantidad de gastos:{reporte['cantidad_gastos']}")
            print(f"Total gastado:{reporte['total_gastado']}")
            print("Total gastado por categoria")
            for i in totales_categoria:
                print(f"{i}:${totales_categoria[i]}")
            print("-" * 30)
            print(f"Total gastado:{reporte['total_gastado']}")
            
            for i in fechas_mensual:
                print(f"Fecha      : {i['fecha']}")
                print(f"Monto      : ${i['monto']}")
                print(f"Categoría  : {i['categoria']}")
                print(f"Descripción: {i['descripcion']}")
                print("-" * 30)
        
            
        if opcion4 ==2: 
            ARCHIVO="reporte_mensual.json"
            with open (ARCHIVO, "w") as file:
                json.dump(reporte,file,indent=4)
        
            print("Archivo creado con exito")
    
    #SALIR################################################################################################################################
    
    elif opcion==4:
        
        print("Regresando al menu principal...")
        return
     
    
    else: 
        print("Opcion no valida")
        return
    
    
