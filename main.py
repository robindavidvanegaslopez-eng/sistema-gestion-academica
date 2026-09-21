from estudiantes import ( 
 agregar_estudiante, 
 mostrar_estudiantes, 
 buscar_estudiante 
) 
from notas import ( 
 agregar_nota, 
 calcular_promedio, 
 estado_estudiante 
) 

 print("\n========================================")
    print("       SISTEMA DE GESTIÓN ACADÉMICA")
    print("========================================")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Registrar nota")
    print("5. Consultar promedio")
    print("6. Salir")
    print("========================================")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_estudiante()

    elif opcion == "2":
        mostrar_estudiantes()

    elif opcion == "3":
        buscar_estudiante()

    elif opcion == "4":
        agregar_nota()

    elif opcion == "5":
        calcular_promedio()

    elif opcion == "6":
        print("Gracias por utilizar el sistema.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")