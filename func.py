variableListaGrupo = 0
variableCursos = 1
# Una lista para evitar NRC's repetidos
listaNRC = []

#Lista para el generador de horarios
listacombinaciones = {}




def funcHora(x):
    # Conseguimos el string x de la hora y le separamos el string en una lista
    b = x.split("-")
    return b


def invfuncHora(x):
    # Validamos si son cumplen, la hora minima es 6-7 (6+7=13), maxima 19-20 (19+20=39), y que el inicio sea menor que el final
    if (
        int(x[0]) + int(x[1]) < 13
        or int(x[0]) + int(x[1]) > 39
        or int(x[0]) > int(x[1])
    ):
        a = 1
        return a
    # Conseguimos el string x de la hora y le separamos el string en una lista
    a = x[0] + " a " + x[1]
    return a


def formatNombres(x):
    # Conseguimos un string x y le quitamos las mayúsculas
    x = x.lower()

    # Detectamos espacios, separamos el string en una lista/array
    b = x.split(" ")

    # Volvemos a unir las partes del string sin espacios ni mayúsculas
    b = "".join(b)
    return b
    # Regresamos

def agregarMateria(cursosDiccionario): 
         global variableCursos 
         while True: 
            nombre = input("Digite el nombre de la materia: ")
            nombreformateado = formatNombres(nombre)
            if nombreformateado.isalpha():
             break
            print("Incorrecto. Vuelva a introducir un nombre.")
         try:
            while True:
                # Esta variable continue para controlar el while
                continuee = 0

                # Asignamos el diccionario madre a otra variable con el fin de no hacerle ningún cambio
                nombres = ""

                # Entramos al diccionario madre
                for curso in cursosDiccionario:

                    # Reasignamos la variable nombres para conseguir los valores de curso, es decir las propiedades de x curso
                    nombres = cursosDiccionario.get(curso, {})

                    # Conseguimos el nombre del curso
                    currentnombre = nombres["nombre"]

                    # Formateamos el nombre del curso y el ingresado
                    currentnombre = formatNombres(currentnombre)
                    nombreformat = formatNombres(nombre)

                    # Revisamos si son iguales
                    if currentnombre == nombreformat:
                        print("Nombre ya ingresado, digite otro")
                        nombre = input("Digite el nombre de la materia: ")
                        continuee = 1
                print(nombres)
                if continuee == 0:
                    break
         except Exception as e:
            print("Error. Pruebe de nuevo")

        # Asignamos un nombre al curso (curso1, curso2...)
         nombrecurso = "curso" + str(variableCursos)

        # Metemos el curso en el diccionario madre
         cursosDiccionario.update({nombrecurso: ({"nombre": nombre, "grupos": ({})})})

        # Subimos el número de variable para evitar confusiones
         variableCursos += 1

         print(f"Materia {nombre} agregada")


def pedirDia():
    print(
        "\n[1] Lunes \n[2] Martes \n[3] Miercoles \n[4] Jueves \n[5] Viernes \n[6] Sabado"
    )
    while True:
        dia = input("Digite el día: ")
        try:
            match int(dia):
                case 1:
                    dia = "Lunes"
                case 2:
                    dia = "Martes"
                case 3:
                    dia = "Miercoles"
                case 4:
                    dia = "Jueves"
                case 5:
                    dia = "Viernes"
                case 6:
                    dia = "Sabado"
                case _:
                    raise (Exception)
            return dia
        except Exception:
            print("Día inválido. Digite un número válido:")
            continue


def pedirHora():
    while True:
        # Pedimos la hora del curso en hora militar y un separador fácil para convertirlo en lista
        hora = input("Digite la hora(14-15, 12-13): ")
        if hora.isascii():
            try:
                horan = funcHora(hora)
                horainv = invfuncHora(horan)
                if horainv != 1:
                    horas = [hora, horan, horainv]
                    return horas
            except:
                sinsentido = 1
        print(
            "Incorrecto. Vuelva a introducir la hora nuevamente en el formato (14-17)"
        )


def pedirProf():
    while True:
        profesor = input("Digite el profesor: ")
        nuevoprofesor = formatNombres(profesor)
        # Este método revisa si todos los digitos están en el alfabeto
        if nuevoprofesor.isalpha():
            return profesor
            break
        print("Incorrecto. Vuelva a introducir un Profesor.")


def pedirNRC():
    while True:
        nrc = input("Digite el NRC del curso: ")
        # Este metodo revisa si todos los dígitos en el NRC son numéricos enteros
        if nrc.isnumeric():
            nrc = int(nrc)
            if nrc < 10000 and nrc > 1000:
                if not nrc in listaNRC:
                    listaNRC.append(nrc)
                    return nrc
                    break
        print("NRC incorrecto. Vuelva a introducir un NRC.")


# Función para imprimir materias
def imprimirMaterias(cursosDiccionario, listaCursos):
    # Declaramos la variable de los grupos
    variableGrupos = 0
    for curso in cursosDiccionario:
        # Pedimos el valor de cada curso
        nombres = cursosDiccionario.get(curso, {})
        # Conseguimos el nombre actual del curso
        currentnombre = nombres["nombre"]

        # Hacemos una lista para los nombres, mayor facilidad al acceder después
        listaCursos.append(currentnombre)

        # Imprimimos el curso
        print(f"[{variableGrupos + 1}] {currentnombre}")
        variableGrupos += 1

    while True:
        materiaSeleccionada = input("Seleccione una materia: ")
        # Un try para validación simple
        try:
            materiaSeleccionada = int(materiaSeleccionada)
            # Devolvemos el nombre de la materia para acceder a ella
            materia = listaCursos[materiaSeleccionada - 1]
        except:
            print("Materia inválida. Digite un número válido")
            continue
        break
    return materia


def seleccionarMateria(cursosDiccionario, materia):
    for curso in cursosDiccionario:
        # Aquí entramos al valor del curso actual, si coincide con la materia almacenamos para actualizarlo
        nombres = cursosDiccionario.get(curso, {})
        currentnombre = nombres["nombre"]
        if currentnombre == materia:
            cursoSeleccionado = curso
            break
    return cursoSeleccionado

def revisarMateria(cursosDiccionario):
    try:
        cursosDiccionario["curso1"]
        return True
    except:
        print("\nNo hay materias disponibles. Agregue uno")
        return False


def revisarGrupos(cursosDiccionario, materia):
    for curso in cursosDiccionario:
       if cursosDiccionario[curso]["nombre"] == materia:
        grupoActual = cursosDiccionario.get(curso, {})
        grupos = grupoActual["grupos"]
        try:
            grupos["1"]
        except:
            print(f"No hay grupos disponibles para esta materia")
            return False
        for grupo in grupos:
            grupoActual = grupos.get(grupo, {})
            dia = grupoActual["dia"]
            hora = grupoActual["hora"]
            nrc = grupoActual["nrc"]
            horan = invfuncHora(hora)
            profesor = grupoActual["profesor"]
            seleccionado = grupoActual["sele"]
            a = (
                f"Grupo {grupo} con NRC {nrc}, {dia}, de {horan}, profesor {profesor}"
            )
            if seleccionado == True:
                a += (f" <---- GRUPO SELECCIONADO")
            print(a)
    
    return True


def agregarGrupo(cursosDiccionario, cursoSeleccionado):
    # Accedemos a la variableListaGrupo y la lista de NRC
    global variableListaGrupo, listaNRC
    dia = pedirDia()
    horas = pedirHora()
    hora = horas[0]
    horan = horas[1]
    horainv = horas[2]
    profesor = pedirProf()
    nrc = pedirNRC()

    # Accedemos al cursoSeleccionado y a los grupos para actualizarlo
    cursoActual = cursosDiccionario[cursoSeleccionado]
    gruposActualizar = cursoActual["grupos"]
    nombreActual = cursoActual["nombre"]
    variableListaGrupo += 1
    # Actualizamos el curso con el grupo nuevo que se nos brindó
    gruposActualizar.update(
        {
            str(variableListaGrupo): {
                "dia": dia,
                "hora": horan,
                "profesor": profesor,
                "nrc": nrc,
                "sele": False,
            }
        }
    )

    # Subimos la variable del grupo

    print(
        "\n"
        + f"Agregado para {nombreActual}, grupo {variableListaGrupo} con NRC {nrc}, {dia}, de {horainv}, profesor {profesor}"
    )


def imprimirGrupos(cursoActual, gruposexistentes, listaGrupos):
    if gruposexistentes == False:
        print("No hay grupos que imprimir")
        return
    variableGrupoActual = 0
    for grupo in cursoActual:
        variableGrupoActual += 1
        grupos = cursoActual.get(grupo, {})
        currentnombre = grupo

        listaGrupos.append(currentnombre)

        # Imprimimos el grupo
        print(f"[{variableGrupoActual}] Grupo {currentnombre}")
    return variableGrupoActual


def eliminarGrupo(cursosDiccionario, cursoSeleccionado, gruposexistentes, listaGrupos):
    if gruposexistentes == False:
        print("No hay grupos que eliminar")
        return
    global variableListaGrupo
    cursoActual = cursosDiccionario[cursoSeleccionado]
    gruposActualizar = cursoActual["grupos"]
    variableGrupoActual = imprimirGrupos(
        gruposActualizar, gruposexistentes, listaGrupos
    )
    while True:
        try:
            grupoeliminar = input("Qué grupo desea eliminar?\n")
            if int(grupoeliminar) not in range(0, variableGrupoActual + 1):
                raise Exception
            break
        except:
            print("Grupo inválido. Seleccione de nuevo")
    for grupo in gruposActualizar:
        if grupo == grupoeliminar:
            grupoeliminar = grupo
    del gruposActualizar[grupoeliminar]
    variableListaGrupo -= 1
    print(f"Eliminado grupo {grupoeliminar}\n")


def modificarGrupo(cursosDiccionario, cursoSeleccionado, gruposexistentes, listaGrupos):
    if gruposexistentes == False:
        print("No hay grupos que modificar")
        return
    print("\n")
    cursoActual = cursosDiccionario[cursoSeleccionado]
    gruposActualizar = cursoActual["grupos"]
    variableGrupoActual = imprimirGrupos(
        gruposActualizar, gruposexistentes, listaGrupos
    )
    while True:
        try:
            grupomodificar = input("Qué grupo desea modificar?\n")
            if int(grupomodificar) not in range(0, variableGrupoActual + 1):
                raise Exception
            break
        except:
            print("Grupo inválido. Seleccione de nuevo")
    for grupo in gruposActualizar:
        if grupo == grupomodificar:
            grupomodificar = grupo
    grupoaModificar = gruposActualizar.get(grupomodificar, {})
    diamodificar = grupoaModificar["dia"]
    horamodificar = grupoaModificar["hora"]
    horamodificar = invfuncHora(horamodificar)
    profesormodificar = grupoaModificar["profesor"]
    nrcmodificar = grupoaModificar["nrc"]
    opcionModificar = input(
        f"Qué desea modificar?\n[1]Día: {diamodificar}\n[2]Hora: {horamodificar}\n[3]Profesor: {profesormodificar}\n"
        + f"[4]NRC: {nrcmodificar}\n"
    )
    while int(opcionModificar) not in range(0, 5):
        print("Opción inválida. Intente de nuevo")
        opcionModificar = input(
            f"Qué desea modificar?\n[1]Día: {diamodificar}\n[2]Hora: {horamodificar}\n[3]Profesor: {profesormodificar}\n"
            + f"[4]NRC: {nrcmodificar}\n"
        )
    match int(opcionModificar):
        case 1:
            dia = pedirDia()
            cursoActual["grupos"][grupomodificar]["dia"] = dia
            print(f"Día modificado a {dia}")
        case 2:
            horas = pedirHora()
            horan = horas[1]
            horainv = horas[2]
            cursoActual["grupos"][grupomodificar]["hora"] = horan
            print(f"Hora modificada, de {horainv}")
        case 3:
            profesor = pedirProf()
            cursoActual["grupos"][grupomodificar]["profesor"] = profesor
            print(f"Profesor modificado a {profesor}")
        case 4:
            nrc = pedirNRC()
            cursoActual["grupos"][grupomodificar]["nrc"] = nrc
            print(f"NRC modificado a {nrc}")


def seleccionarGrupo(cursosDiccionario,cursoSeleccionado,gruposexistentes, listaGrupos):
    if gruposexistentes == False:
        print("No hay grupos que modificar")
        return
    print("\n")
    cursoActual = cursosDiccionario[cursoSeleccionado]
    gruposActualizar = cursoActual["grupos"]
    variableGrupoActual = imprimirGrupos(
        gruposActualizar, gruposexistentes, listaGrupos
    )
    while True:
        try:
            gruposeleccionar = input("Qué grupo desea seleccionar?\n")
            if int(gruposeleccionar) not in range(0, variableGrupoActual + 1):
                raise Exception
            break
        except:
            print("Grupo inválido. Seleccione de nuevo")
    for grupo in gruposActualizar:
        if grupo == gruposeleccionar:
            gruposeleccionar = grupo
    if cursoActual["grupos"][gruposeleccionar]["sele"] == True:
        cursoActual["grupos"][gruposeleccionar]["sele"] = False
        print(f"Grupo {gruposActualizar} deseleccionado")
    else:
        cursoActual["grupos"][gruposeleccionar]["sele"] = True
        print(f"Grupo {gruposActualizar} seleccionado")
    

def generarHorarios(cursosDiccionario):
    variableCombinaciones = 1
    while True:
     for curso in cursosDiccionario:
        listacombinaciones.update({f"{variableCombinaciones}": []})
        combinacionActual = listacombinaciones[f"{variableCombinaciones}"]
        cursoActual = cursosDiccionario[curso]["grupos"]
        for grupo in cursoActual:
            dia = cursoActual[grupo]["dia"]
            hora = cursoActual[grupo]["hora"]
            combinacionActual.append(dia)
            combinacionActual.append(hora)
        for otrocurso in cursosDiccionario:
            if otrocurso == curso:
                print("")
            else:
                cursoActual = cursosDiccionario[otrocurso]["grupos"]
                for grupo in cursoActual:
                    dia = cursoActual[grupo]["dia"]
                    hora = cursoActual[grupo]["hora"]
                    combinacionActual.append(dia)
                    combinacionActual.append(hora)
     variableCombinaciones += 1
     print(listacombinaciones)
     break

