from funciones import cargar_gastos
from registro import registrar_gastos
from listar import listar_gastos
from calcular import calculador
from reportes import generar_reporte


        

def menu():
    
    while True: 
        
        gastos = cargar_gastos()
        
        print("="*45)
        print ("         SIMULADOR DE GASTOS DIARIOS          ")
        print("="*45)        
        
        print ("""
        1.Registrar nuevo gasto
        2. Listar gastos
        3. Calcular total de gastos
        4. Generar reporte de gastos
        5. Salir""")
        print("="*45)
        
        
        try:
            opcion =int(input(" Seleccione una opción:"))
        except ValueError:
            print("Entrada no válida")
            continue
        
        
        if opcion == 1:
            registrar_gastos(gastos)
            
            
            
        
        elif opcion == 2:
            
            listar_gastos(gastos)
            
            
            

        elif opcion ==3:

            calculador(gastos)
    
            
        elif opcion == 4:
        
            generar_reporte(gastos)
        
        
        elif opcion == 5:
            print ("¿Desea salir del programa? ")
            print ("Seleccione S para salir o N para continuar")
        
            opcion2 = (input("").lower().strip())
        
            if opcion2=="s": 
                print("Saliendo...")
                break
            elif opcion2=="n":
                print("Regresando al menu principal...")
                continue
            else:
                print("Entrada no válida")
                continue
            
            
            
            
        else:
            print ("Opcion no valida")
            continue
    
if __name__ =="__main__":
     menu()