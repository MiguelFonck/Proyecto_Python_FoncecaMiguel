from datetime import datetime,date, timedelta
from funciones import guardar_gastos

def calculador(gastos): 
    
    fechas_diarias=[]
    fechas_semana=[]
    fechas_mensual=[]

    
    if not gastos:
        print("No hay registro de datos")
        return
    
    print("="*35)
    print ("CALCULAR TOTAL DE GASTOS".center(35))
    print("="*35)
    print ("Seleccione el periodo del calculo:")
    print ("1.Calcular total diario")
    print ("2.Calcular total semanal")
    print ("3.Calcular total mensual")
    print ("4.Salir al menu principal")
    print("="*35)
    
    try:
        opcion = int(input(""))
    except ValueError:
        print("Entrada no válida")
        return
    
    #DIARIO==========================================================================================================================================
    if opcion ==1:
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
        for i in fechas_diarias:
            print(f"Fecha      : {i['fecha']}")
            print(f"Monto      : ${i['monto']}")
            print(f"Categoría  : {i['categoria']}")
            print(f"Descripción: {i['descripcion']}")
            print("-" * 30)
    
    
        print(f"la suma total de los gastos diarios es de ${suma_total}")
        print("=" * 45)
        print("==========Totales por categoria==========") 
        for i in totales_categoria:
            print(f"{i}:${totales_categoria[i]}")
        print("-" * 30)
    
    
    #SEMANAL==============================================================================================================================================
    elif opcion==2:
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
                    
        else:         
            for i in fechas_semana:
                print(f"Fecha      : {i['fecha']}")
                print(f"Monto      : ${i['monto']}")
                print(f"Categoría  : {i['categoria']}")
                print(f"Descripción: {i['descripcion']}")
                print("-" * 30)
        
        
        
            print(f"la suma total de los gastos semanales es de ${suma_total}")
            print("=" * 45)
            print("==========Totales por categoria==========") 
            for i in totales_categoria:
                print(f"{i}:${totales_categoria[i]}")
            print("-" * 30)
            
            
    #MENSUAL==========================================================================================================================================================
    elif opcion==3:
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
        else:
                
            for i in fechas_mensual:
                print(f"Fecha      : {i['fecha']}")
                print(f"Monto      : ${i['monto']}")
                print(f"Categoría  : {i['categoria']}")
                print(f"Descripción: {i['descripcion']}")
                print("-" * 45)
            
            
            
            print(f"la suma total de los gastos mensuales es de ${suma_total}")
            print("=" * 45)
            print("==========Totales por categoria==========") 
            for i in totales_categoria:
                print(f"{i}:${totales_categoria[i]}")
            print("-" * 30)
        
        
#SALIR#############################################################################################################################################
    elif opcion==4:
        
        print("Regresando al menu principal...")
        return
     
    
    else: 
        print("Opcion no valida")
        return