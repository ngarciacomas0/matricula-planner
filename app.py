import json
import func as f
# Creamos el diccionario madre de los cursos
cursosDiccionario = {}
# Creamos la lista del nombre de los cursos
listaCursos = []
# Creamos la lista del nombre de los grupos
listaGrupos = []
# Creamos una variable de cursos, esto para asignarle un numero al curso

# Lo mismo con los grupos
variableListaGrupo = 0

while True:
    materiasexistentes = f.revisarMateria(cursosDiccionario)
    menu = 11
    try:
        int(menu)
        while menu not in range(1,5):
            menu = input(
         "Bienvenido a el Planner de Matrícula! Digite un número para continuar: \n"
            + "1. Ingresar una materia \n"
            + "2. Ver materias y grupos \n"
         + "3. Generar horarios \n"
         + "4. Revisar diccionario madre\n"
            )
            if int(menu) not in range(1,5):
                print("\n\nOpción inválida, intente de nuevo")
            else: 
                 break
    except KeyboardInterrupt:
        print("\n\nCerrando...")
        break
    except:
        print("\n\nOpción inválida, intente de nuevo")
    # Input de menu
    
    if menu == "1":
        f.agregarMateria(cursosDiccionario)

    if menu == "2":

        if materiasexistentes == False:
            continue
        materia = f.imprimirMaterias(cursosDiccionario, listaCursos)

        cursoSeleccionado = f.seleccionarMateria(cursosDiccionario, materia)

        print(f"{materia}:")
        gruposexistentes = f.revisarGrupos(cursosDiccionario, materia)
        decision = input("Qué desea hacer?\n[1] Agregar grupo\n[2] Eliminar grupo\n[3] Modificar grupo\n[4] (De)Seleccionar grupo\n")
        while decision != "1" and decision != "2" and decision != "3" and decision != "4":
            print("Opción inválida, vuelvalo a intentar")
            decision = input(
                "Qué desea hacer?\n[1] Agregar grupo\n[2] Eliminar grupo\n[3] Modificar grupo\n[4] (De)Seleccionar grupo\n"
            )
        if decision == "1":
            f.agregarGrupo(cursosDiccionario, cursoSeleccionado)
        elif decision == "2":
            f.eliminarGrupo(cursosDiccionario,cursoSeleccionado,gruposexistentes, listaGrupos)
        elif decision == "3":
            f.modificarGrupo(cursosDiccionario,cursoSeleccionado,gruposexistentes, listaGrupos)
        elif decision == "4":
            f.seleccionarGrupo(cursosDiccionario,cursoSeleccionado,gruposexistentes, listaGrupos)
    if menu == "3":
        f.generarHorarios(cursosDiccionario)
    if menu == "4":
        print(json.dumps(cursosDiccionario, indent=4))
