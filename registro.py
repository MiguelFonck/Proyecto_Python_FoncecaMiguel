from datetime import datetime
from funciones import guardar_gastos

def registrar_gastos(gastos):
    
    categoria_final=""
    fecha_actual=datetime.now().strftime("%Y-%m-%d")
    
    print("="*35)
    print ("REGISTRAR NUEVO GASTO".center(35))
    print("="*35)
    print ("Ingrese la información del gasto:")
    print ("Monto del gasto:")
    print ("Categoria: comida, transporte, entretenimiento, otros")
    print ("Descripcion:")
    
    try:
         monto =int(input(" Ingrese su monto del gasto:")) 
    except ValueError:
     print("Entrada no válida")
     return
  
    if monto >= 0: 
        print ("""Categorias:
               1.Comida
               2.transporte
               3.entretenimiento
               4.otros
            """)
        
        try:
         categoria =int(input(" Seleccione una opción:"))
        except ValueError:
         print("Entrada no válida")
         return
      
        if categoria==1:
                categoria_final= "comida" 
        elif categoria==2: 
                categoria_final="transporte"
        elif categoria==3: 
                categoria_final="entretenimiento"
        elif categoria==4:
                categoria_final="otros"
        else:
            print ("Opcion no valida")
            return
            
          
    descripcion=input ("Añade una pequeña descripcion  de tu gasto")
     
            
    
        
    opcion=input("Ingrese 'S' para guardar o 'C' para cancelar.") 
    opcion = opcion.lower().strip()
    print("="*35) 
    
    if opcion == "c":
        print("Cancelando...")
        return
    
    
    elif opcion =="s":
        gasto={
                "fecha":fecha_actual,
                "monto":monto,
                "categoria":categoria_final,
                "descripcion":descripcion
                
            }
        gastos.append(gasto)
        guardar_gastos(gastos)
        print("Registro de gasto guardado con exito")
    else:
        print ("Opcion no valida")
        return