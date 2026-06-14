import json
cursosDiccionario = {}
variableCursos = 1
listaCursos = []
variableListaGrupo = 0
listaNRC = []
listacombinaciones = {}

def FormatoHora(x):
    # Conseguimos el string x de la hora y le separamos el string en una lista
    b = x.split("-")
    return b


def invertirFormatoHora(x):
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


def FormatoNombres(x):
    # Conseguimos un string x y le quitamos las mayúsculas
    x = x.lower()

    # Detectamos espacios, separamos el string en una lista/array
    b = x.split(" ")

    # Volvemos a unir las partes del string sin espacios ni mayúsculas
    b = "".join(b)
    return b
    # Regresamos
def RevisarMaterias(cursosDiccionario):
    global variableCursos
    z = False
    for curso in cursosDiccionario:
        if cursosDiccionario[curso]["nombre"] not in listaCursos:
            listaCursos.append(cursosDiccionario[curso]["nombre"])
        numeroCurso = curso.find(f"{variableCursos}")
        if numeroCurso != -1:
            variableCursos += 1
        z = True
    if z == True:
        return True
    else:
        return False

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
            horaFormateada = FormatoHora(hora)
            horaNormal = invertirFormatoHora(horaFormateada)
            if horaNormal != 1:
                listaHoras = [hora, horaFormateada, horaNormal]
                return listaHoras
        else:
            print("Incorrecto. Vuelva a introducir la hora nuevamente en el formato (14-17)")


def pedirProf():
    while True:
        profesor = input("Digite el profesor: ")
        profesorFormateado = FormatoNombres(profesor)
        # Este método revisa si todos los digitos están en el alfabeto, quitando los espacios del profesor
        if profesorFormateado.isalpha():
            return profesor
        print("Incorrecto. Vuelva a introducir un Profesor.")


def pedirNRC():
    while True:
        nrc = input("Digite el NRC del curso: ")
        # Este metodo revisa si todos los dígitos en el NRC son numéricos enteros
        try:
            if nrc.isnumeric():
                nrc = int(nrc)
                if nrc < 10000 and nrc > 1000:
                    if not nrc in listaNRC:
                        listaNRC.append(nrc)
                        return nrc
                    else:
                        raise Exception
                else:
                    raise Exception
            else:
                raise Exception
        except:
            print("NRC incorrecto. Vuelva a introducir un NRC.")

def pedirNombre(nombreIgual):
        nombreIngresado = input("Digite el nombre de la materia: ")
        nombreIngresadoFormateado = FormatoNombres(nombreIngresado)
        if not nombreIngresadoFormateado.isascii():
            print("Incorrecto. Vuelva a introducir un nombre.")
        for curso in cursosDiccionario:
            infoCursoActual = cursosDiccionario.get(curso, {})
            CursoActual = infoCursoActual["nombre"]
            CursoActualFor = FormatoNombres(CursoActual)
            if CursoActualFor == nombreIngresadoFormateado:
                print("Nombre ya ingresado. Ingrese otro")
                nombreIgual == True
                return nombreIgual, nombreIngresado
        nombreIgual = False
        return nombreIgual, nombreIngresado


def agregarMateria(cursosDiccionario): 
    global variableCursos
    nombreIgual = True
    while nombreIgual == True:
            listaNombre = pedirNombre(nombreIgual)
            nombreIgual = listaNombre[0]
            nombreIngresado = listaNombre[1]
    nombrecurso = "curso" + str(variableCursos)
    while nombrecurso in listaCursos:
        variableCursos += 1
        nombrecurso = "curso" + str(variableCursos)
        break
    cursosDiccionario.update({nombrecurso: ({"nombre": nombreIngresado, "grupos": ({}), "variablegrupos" : 1, "gsele": False})})
    print(f"Materia {nombreIngresado} agregada")
    print("Actualmente esta materia no tiene grupos. Ingrese a dicha materia para crear uno")


# Función para imprimir materias
def imprimirMaterias(listaCursos):
    variableMaterias = 0
    for curso in listaCursos:
        variableMaterias += 1
        print(f"[{variableMaterias}] {curso}")

def seleccionarMateria(cursosDiccionario, listaCursos):
    while True:
        materiaSeleccionada = input("Seleccione una materia: ")
        # Un try para validación simple
        try:
            materiaSeleccionada = int(materiaSeleccionada)
            materia = listaCursos[materiaSeleccionada - 1]
        except:
            print("Materia inválida. Digite un número válido")
            continue
        break
    for curso in cursosDiccionario:
        if cursosDiccionario[curso]["nombre"] == materia:
            materiaSeleccionada = curso
            return materiaSeleccionada, materia

def revisarGrupos(cursosDiccionario, materia):
    global gruposexistentes
    for curso in cursosDiccionario:
       if cursosDiccionario[curso]["nombre"] == materia:
        cursoActual = cursosDiccionario.get(curso, {})
        gruposActuales = cursoActual["grupos"]
    try:
        gruposActuales["1"]
    except:
        print(f"No hay grupos disponibles para esta materia")
        return False
    for grupo in gruposActuales:
        infogruposActuales = gruposActuales.get(grupo, {})
        dia = infogruposActuales["dia"]
        hora = infogruposActuales["hora"]
  
        nrc = infogruposActuales["nrc"]
        profesor = infogruposActuales["profesor"]
        seleccionado = infogruposActuales["sele"]
        a = (f"Grupo {grupo} con NRC {nrc}, profesor {profesor}:")
        if seleccionado == True:
            a += (f" <---- GRUPO SELECCIONADO")
        if type(dia) != type(profesor):
            for diax in dia:
                length = dia.index(diax)
                horasdiax = hora[length]
                horasFormateadas = invertirFormatoHora(horasdiax)
                a += (f"\n{diax}, de {horasFormateadas}")
        else:
            horaNormal = invertirFormatoHora(hora)
            a += (f"\n{dia}, de {horaNormal}")
        print(a)
    return True


def agregarGrupo(cursosDiccionario, cursoSeleccionado):
    # Accedemos al cursoSeleccionado y a los grupos para actualizarlo
    cursoActual = cursosDiccionario[cursoSeleccionado]
    variableListaGrupo = cursoActual["variablegrupos"]
    gruposActualizar = cursoActual["grupos"]
    dia = pedirDia()
    listaHoras = pedirHora()
    horaFormateada = listaHoras[1]
    horaNormal = listaHoras[2]
    profesor = pedirProf()
    nrc = pedirNRC()
    nombreActual = cursoActual["nombre"]
    # Actualizamos el curso con el grupo nuevo que se nos brindó
    gruposActualizar.update(
        {
            str(variableListaGrupo): {
                "dia": dia,
                "hora": horaFormateada,
                "profesor": profesor,
                "nrc": nrc,
                "sele": False,
            }
        }
    )



    print(
        "\n"
        + f"Grupo {variableListaGrupo} agregado para materia {nombreActual}"
    )
    cursoActual["variablegrupos"] += 1


def imprimirGrupos(cursoActual, gruposexistentes):
    if gruposexistentes == False:
        print("No hay grupos que imprimir")
        return
    variableGrupoActual = 0
    for grupo in cursoActual:
        variableGrupoActual += 1
        # Imprimimos el grupo
        print(f"[{variableGrupoActual}] Grupo {grupo}")
    return variableGrupoActual

#Mejorar variables
def eliminarGrupo(cursosDiccionario, cursoSeleccionado, gruposexistentes):
    global variableListaGrupo
    if gruposexistentes == False:
        print("No hay grupos que eliminar")
        return
    cursoActual = cursosDiccionario[cursoSeleccionado]
    gruposActualizar = cursoActual["grupos"]
    variableGrupoActual = imprimirGrupos(gruposActualizar, gruposexistentes)
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
    listaNRC.remove(gruposActualizar[grupoeliminar]["nrc"])
    del gruposActualizar[grupoeliminar]
    variableListaGrupo -= 1
    print(f"Eliminado grupo {grupoeliminar}\n")


def modificarGrupo(cursosDiccionario, cursoSeleccionado, gruposexistentes):
    if gruposexistentes == False:
        print("No hay grupos que modificar")
        return
    print("\n")
    cursoActual = cursosDiccionario[cursoSeleccionado]
    gruposActualizar = cursoActual["grupos"]
    variableGrupoActual = imprimirGrupos(gruposActualizar, gruposexistentes)
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
    profesormodificar = grupoaModificar["profesor"]
    nrcmodificar = grupoaModificar["nrc"]
    nombremodificar = cursoActual["nombre"]
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
            if type(diamodificar) != type(profesormodificar):
                    diaEsString = True
                    dia = diamodificar
            else:
                dia = pedirDia()
                cursoActual["grupos"][grupomodificar]["dia"] = dia
                print(f"Día modificado a {dia}")
            while dia == diamodificar:
                listadiavalue = 1
                if diaEsString:
                    print("\n")
                for diax in diamodificar:
                    length = diamodificar.index(diax)
                    horasdiax = horamodificar[length]
                    horasFormateadas = invertirFormatoHora(horasdiax)
                    print(f"[{listadiavalue}]{diax}, de {horasFormateadas}")
                    listadiavalue += 1
                dia = input("Qué día desea modificar?\n")
                try:
                    dia = int(dia) - 1
                    nuevodia = pedirDia()
                    if cursoActual["grupos"][grupomodificar]["dia"][dia] == nuevodia:
                        raise Exception
                    cursoActual["grupos"][grupomodificar]["dia"][dia] = nuevodia
                    print(f"Día modificado a {nuevodia}")
                except:
                    print("Error. Intente de nuevo\n")
                    dia = diamodificar
           
        case 2:
            if type(diamodificar) != type(profesormodificar):
                    diaEsString = True
                    hora = horamodificar
            else:
                horas = pedirHora()
                horan = horas[1]
                horainv = horas[2]
                cursoActual["grupos"][grupomodificar]["hora"] = horan
                print(f"Hora modificada, de {horainv}")
            while hora == horamodificar:
                listadiavalue = 1
                if diaEsString:
                    print("\n")
                for diax in diamodificar:
                    length = diamodificar.index(diax)
                    horasdiax = horamodificar[length]
                    horasFormateadas = invertirFormatoHora(horasdiax)
                    print(f"[{listadiavalue}]{diax}, de {horasFormateadas}")
                    listadiavalue += 1
                hora = input("Qué hora desea modificar?\n")
                try:
                    hora = int(hora) - 1
                    nuevalistaHora = pedirHora()
                    nuevahora = nuevalistaHora[1]
                    if cursoActual["grupos"][grupomodificar]["hora"][hora] == nuevahora:
                        raise Exception
                    cursoActual["grupos"][grupomodificar]["hora"][hora] = nuevahora
                    nuevahora = nuevalistaHora[2]
                    print(f"Hora modificada a {nuevahora}")
                except:
                    print("Error. Intente de nuevo\n")
                    hora = horamodificar
        case 3:
            profesor = pedirProf()
            cursoActual["grupos"][grupomodificar]["profesor"] = profesor
            print(f"Profesor modificado a {profesor}")
        case 4:
            nrc = pedirNRC()
            listaNRC.remove(cursoActual["grupos"][grupomodificar]["nrc"])
            listaNRC.append(nrc)
            cursoActual["grupos"][grupomodificar]["nrc"] = nrc
            print(f"NRC modificado a {nrc}")


def seleccionarGrupo(cursosDiccionario,cursoSeleccionado,gruposexistentes):
    if gruposexistentes == False:
        print("No hay grupos que seleccionar")
        return
    print("\n")
    cursoActual = cursosDiccionario[cursoSeleccionado]
    gruposActualizar = cursoActual["grupos"]
    variableGrupoActual = imprimirGrupos(gruposActualizar, gruposexistentes)
    while True:
        try:
            gruposeleccionar = input("Qué grupo desea seleccionar/deseleccionar?\n")
            if int(gruposeleccionar) not in range(0, variableGrupoActual + 1):
                raise Exception
            break
        except:
            print("Grupo inválido. Seleccione de nuevo")
    for grupo in gruposActualizar:
        if grupo == gruposeleccionar:
            gruposeleccionar = grupo
        elif grupo != gruposeleccionar and cursoActual["grupos"][grupo]["sele"] == True:
            print(f"Grupo {grupo} ya seleccionado. Deseleccionelo para seleccionar otros grupos")
            return
    if cursoActual["grupos"][gruposeleccionar]["sele"] == True:
        cursoActual["grupos"][gruposeleccionar]["sele"] = False
        cursoActual["gsele"] = False
        print(f"Grupo {gruposeleccionar} deseleccionado")
    else:
        cursoActual["grupos"][gruposeleccionar]["sele"] = True
        cursoActual["gsele"] = True
        print(f"Grupo {gruposeleccionar} seleccionado")

def modificarNombre(cursosDiccionario,cursoSeleccionado):
    global listaCursos
    print("\n")
    cursoActual = cursosDiccionario[cursoSeleccionado]
    nombreIgual = True
    while nombreIgual == True:
        listaNombre = pedirNombre(nombreIgual)
        nombreIgual = listaNombre[0]
        nombre = listaNombre[1]
    listaCursos.remove(cursoActual["nombre"])
    cursoActual["nombre"] = nombre
    print(f"Nombre modificado a {nombre}")
    
    

def generarHorarios(cursosDiccionario):
    global variableCursos
    listacursos = []
    combinacionesValidas = []
    variablecombinacionesValidas = 0
    cursosActuales = variableCursos - 1
    settings = 4
    while settings not in range(1,4):
        settings = input("Desea algún ajuste?\n[1] Mostrar combinaciones con días libres\n[2] Mostrar combinaciones solo con los cursos seleccionados\n")
        match int(settings):
            case 1: 
                settings = 1
            case 2: 
                settings = 2 
            case 3: 
                print("Imprimiendo combinaciones sin ajustes...")
                settings = 3

    for i in cursosDiccionario:
        listacursos.append(i)
    diccionario = {}
    for i in listacursos:
        variableGrupos = len(cursosDiccionario[i]["grupos"])
        diccionario.update({f"{i}": variableGrupos})
    combinaciones = [1] * cursosActuales
    Cursos = list(diccionario.values())
    varcomp = 1
    n = 1
    while True:
        invalido = False
        dias = []
        horas = []
        variableFor = 0
        if settings == 2:
            cursosSeleccion = []
            gruposSeleccion = []
            for i in cursosDiccionario:
                curso = cursosDiccionario[i]
                if curso["gsele"] == True:
                    cursosSeleccion.append(i)
                    curso = cursosDiccionario.get(i, {})
                    grupos = curso["grupos"]
                    for z in grupos:
                        if grupos[z]["sele"] == True:
                            gruposSeleccion.append(z)
                            break
        if settings == 2:
            variableFor2 = 0
            for index, value in enumerate(combinaciones):
                variableFor2 += 1
                if f"curso{variableFor2}" in cursosSeleccion:
                    indexcurso = cursosSeleccion.index(f"curso{variableFor2}")
                else:
                    continue
                for curso in cursosSeleccion:
                    if variableFor2 - 1 == index:
                        if value != int(gruposSeleccion[indexcurso]):
                            invalido = True
                
    
        for i in combinaciones:
            variableFor += 1
            if invalido == True:
                break
            grupoActual = cursosDiccionario[f"curso{variableFor}"]["grupos"][f"{i}"]
            dia = grupoActual["dia"]
            horass = grupoActual["hora"]
            if type(dia) != type (grupoActual["profesor"]):
                for i in dia:
                    dias.append(i)
            else:
                dias.append(dia)
            if type(horass[1]) != type([1]):
                horas.append(horass)
            else:
                for i in horass:
                    horas.append(i)
        if len(dias) == len(set(dias)) and invalido == False:
            diasRepetidos = False
            combinacionesValidas.append(combinaciones.copy())
            variablecombinacionesValidas += 1
        else:
            diasRepetidos = True
            diccionarioDiasRepetidos = {}
            semana = ["Lunes", "Martes", "Miercoles","Jueves", "Viernes"]
            dias2 = dias.copy()
            for i in dias:
                if i in diccionarioDiasRepetidos:
                    continue
                diccionarioDiasRepetidos.update({i : [dias.index(i)]}) 
                dias2.remove(i)
                semana.remove(i)
                indexReal = 1
                while i in dias2:
                    rep = dias2.index(i)
                    diccionarioDiasRepetidos[i].append(rep + indexReal)
                    dias2.pop(rep)
                    indexReal += 1
            if settings == 1 and semana != []:
                invalido == True
            for i in diccionarioDiasRepetidos:
                if invalido == True:
                    break
                horasdd = list(range(0,25))
                indexes = diccionarioDiasRepetidos[i]
                for i in indexes:
                    if invalido == True:
                        break
                    horaActual = horas[i]
                    rangohoraActual = list(range(int(horaActual[0]), int(horaActual[1]) + 1))
                    for i in rangohoraActual:
                        if invalido == True:
                            break
                        if i in horasdd:
                            horasdd.remove(i)
                        else:
                            invalido = True
                
        
        if invalido == False and diasRepetidos == True:
            combinacionesValidas.append(combinaciones.copy())
            variablecombinacionesValidas += 1
        if combinaciones != Cursos:
                while n != len(combinaciones):
                    while combinaciones[-n] == Cursos[-n]:
                       combinaciones[-n] = 1
                       n += 1
                    if combinaciones[-n] != Cursos[-n]:
                        combinaciones[-n] += 1
                    n = 1
                    break
                
                
                
        else:
            print(f"Hay {variablecombinacionesValidas} combinaciones válidas:")
            listaComb = combinacionesValidas.copy()
            variableCurso = 0
            variableComb = 0
            for i in listaComb:
                variableComb += 1
                print(f"====COMBINACION {variableComb}====")
                for z in i:
                    variableCurso += 1
                    grupoActual = cursosDiccionario[f"curso{variableCurso}"]["grupos"][f"{z}"]
                    print(f"Curso {variableCurso}:")
                    
                    a = f"=>Grupo {z}: "
                    diaActual = grupoActual["dia"]
                    horass = grupoActual["hora"]
                    if type(diaActual) == type([1,2]):
                        for i in diaActual:
                            index = diaActual.index(i)
                            horaActual = horass[index]
                            horaActualInvertida = invertirFormatoHora(horaActual)
                            a += (f"{i}, de {horaActualInvertida} | ")
                    else:
                        horaActual = invertirFormatoHora(horass)
                        a += (f"{diaActual}, de {horaActual}")
                    print(a)
                variableCurso = 0
            return combinacionesValidas
        
        


def pedirMenu():
    try:
        materiasDisponibles = RevisarMaterias(cursosDiccionario) 
        menu = input("---------MENU--------------: \n[1] Ingresar una materia \n[2] Ver materias y grupos \n[3] Generar horarios \n[4] Revisar diccionario madre\n[5] Salir\n")
        while int(menu) not in range(1,6):
            raise Exception
        return menu, materiasDisponibles
    except KeyboardInterrupt:
        print("\n\nCerrando...")
        return False
    except:
        print("\n\nOpción inválida, intente de nuevo")
        menu = 1
        return menu
    
def agregarTurnoGrupo(cursosDiccionario,materiaSeleccionada,gruposexistentes):
    if gruposexistentes == False:
        print("No hay grupos que modificar")
        return
    print("\n")
    cursoActual = cursosDiccionario[materiaSeleccionada]
    gruposActualizar = cursoActual["grupos"]
    variableGrupoActual = imprimirGrupos(gruposActualizar, gruposexistentes)
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
            break
    diacursoActual = cursoActual["grupos"][grupomodificar]["dia"] 
    horaCursoActual = cursoActual["grupos"][grupomodificar]["hora"] 
    profesor = cursoActual["grupos"][grupomodificar]["profesor"]
    if type(diacursoActual) == type(profesor):
        diaEsString = True
    if diaEsString:
        dia = diacursoActual
        while dia == diacursoActual:
            dia = pedirDia()
            if dia == diacursoActual:
                print("Incorrecto. No puede ser igual a otro día")
    else:
        while True:
            dia = pedirDia()
            if dia in diacursoActual:
                print("Incorrecto. No puede ser igual a otro día")
            else:
                break
    horas = pedirHora()
    horaFormateada = horas[1]
    horaString = horas[2]
    
    profesor = cursoActual["grupos"][grupomodificar]["profesor"] 


    if diaEsString:
        cursoActual["grupos"][grupomodificar]["dia"] = []
        cursoActual["grupos"][grupomodificar]["dia"].append(diacursoActual)

    cursoActual["grupos"][grupomodificar]["dia"].append(dia)

    if type(cursoActual["grupos"][grupomodificar]["hora"][0]) == type(profesor):
        cursoActual["grupos"][grupomodificar]["hora"] = []
        cursoActual["grupos"][grupomodificar]["hora"].append(horaCursoActual)

    cursoActual["grupos"][grupomodificar]["hora"].append(horaFormateada)   
    print(f"Nuevo horario agregado: {dia}, de {horaString}")


try:
    with open("info.json", "r") as f:
        cursosDiccionario = json.load(f)
except:
    print("No se logró cargar información pasada. Creando nueva lista...")



while True:
    listaMenu = pedirMenu()
    if listaMenu == 1:
        continue
    elif listaMenu == False:
        break
    menu = listaMenu[0]
    materiasDisponibles = listaMenu[1]

    match menu:
        case "1":
            try:
                agregarMateria(cursosDiccionario)
            except KeyboardInterrupt:
                print("\nCerrando...")
                break
        case "2":
            if materiasDisponibles == False:
                print("No hay materias disponibles. Agregue una")
                continue
            imprimirMaterias(listaCursos)
            try:
                listaSeleccion = seleccionarMateria(cursosDiccionario, listaCursos)
            except KeyboardInterrupt:
                print("\nCerrando...")
                break
            nombreMateria = listaSeleccion[1]
            materiaSeleccionada = listaSeleccion[0]
            print(f"{nombreMateria}:")
            gruposexistentes = revisarGrupos(cursosDiccionario, nombreMateria)
            while True:
                try:
                    decision = input("Qué desea hacer?\n[1] Agregar grupo\n[2] Eliminar grupo\n[3] Modificar grupo\n[4] (De)Seleccionar grupo\n[5] Modificar nombre\n[6] Agregar otro turno a un grupo")
                    match decision:
                        case "1": agregarGrupo(cursosDiccionario, materiaSeleccionada)
                        case "2": eliminarGrupo(cursosDiccionario,materiaSeleccionada,gruposexistentes)
                        case "3": modificarGrupo(cursosDiccionario,materiaSeleccionada,gruposexistentes)
                        case "4": seleccionarGrupo(cursosDiccionario,materiaSeleccionada,gruposexistentes)
                        case "5":  modificarNombre(cursosDiccionario,materiaSeleccionada)
                        case "6": agregarTurnoGrupo(cursosDiccionario,materiaSeleccionada,gruposexistentes)
                        case _: raise ValueError
                    break
                except KeyboardInterrupt:
                    print("\nSaliendo...")
                    break
                except ValueError:
                    print("Opción inválida, vuelvalo a intentar")
                except Exception as e:
                    print(f"Algo salió mal: {e}")
        case "3":
            combinacionesValidas = generarHorarios(cursosDiccionario)
        case "4":
            print(json.dumps(cursosDiccionario, indent=4))
        case "5":
            guardar = input("Desea guardar la información? 1. Si, 2. No")
            if int(guardar) == 1:
                print("")
                with open("info.json", "w") as f:
                    json.dump(cursosDiccionario, f, indent=4)
            print("\nCerrando...")
            break


