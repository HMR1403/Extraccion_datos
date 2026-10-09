#Hector Malaga Rodriguez Grupo 951 11/10/2026
#uso de la libreria pyodbc para consultar bases de datos
import pyodbc


#conectando a mi base de datos
def conectar():
    #print(pyodbc.drivers())
    try:
        conexion = pyodbc.connect(
            "DRIVER={ODBC Driver 18 for SQL Server};"
            "SERVER=.\\SQLEXPRESS;"
            "DATABASE=eventos_universitarios;" 
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
        )

        return conexion
    except pyodbc.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

#mostrando todos los eventos que registre
def mostrar_eventos():
    con = conectar()
    try:
        cursor = con.cursor()

        sql = f"""
        SELECT * FROM eventos"""
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print("TODOS NUESTROS EVENTOS:\n")
        for i in resultado:
            print(i)

        cursor.close()

    except pyodbc.Error as e:
        print(f"Error al consultar la tabla 'eventos' en la base de datos: {e}")

    finally:
        con.close()

#buscar un evento por nombre en especifico
def consultar_especifico(busqueda):
    con = conectar()
    try:
        if not busqueda:
            print("Faltan datos pa buscar")
            return False
        cursor = con.cursor()

        sql = f"""
        SELECT * FROM eventos
        WHERE nombre LIKE ?"""
        nombre = f"%{busqueda}%"
        cursor.execute(sql, [nombre])
        resultado = cursor.fetchall()
        print("RESULTADOS:\n")
        for i in resultado:
            print(i)

        cursor.close()

    except pyodbc.Error as e:
        print(f"Error a la hora de consultar la base de datos {e}")

    finally:
        con.close()

#consultar eventos con espacios disponibles para participar
def consultar_disponibles(registrar):
    conexion = conectar()
    try:
        if registrar <= 0:
            print("No aceptamos negativos")
            return False
        cursor = conexion.cursor()

        sql = f"""
        SELECT * FROM eventos
        WHERE (cupo - registrados) >= ?
        """
        cursor.execute(sql, [registrar])
        resultado = cursor.fetchall()
        print("DISPONIBLES:\n")
        if not resultado:
            print("NO SE ENCONTRARON EVENTOS CON DISPONIBILIDAD")
        for i in resultado:
            print(i)

        cursor.close()
    except pyodbc.Error as e:
        print(f"Error con la base de datos: {e}")

    finally:
        conexion.close()

#registrar participantes nuevos solo si el evento existe, los asistentes son validos y si queda espacio de registro
def registro_asistentes(idd,asis):
    con = conectar()
    try:
        if asis <= 0:
            print("NO INSCRIBA AIRE\n")
            return False
        else:
            cursor = con.cursor()

            sql = """
            SELECT * FROM eventos
            WHERE id_evento = ? and (cupo - registrados) >= ?
            """
            cursor.execute(sql, [idd, asis])
            resultado = cursor.fetchall()

            if not resultado:
                print("No se ha encontrado el evento o ya no hay espacio")
                return None
            else:
                print("VALORES ENCONTRADOS:\n")
                for i in resultado:
                    print(i)
                print("ACTUALIZANDO REGISTROS...\n")
                sql2= """
                UPDATE eventos SET registrados = (registrados + ?) WHERE id_evento = ?
                """
                cursor.execute(sql2, [asis, idd])
                con.commit()
                sql3 = """
                SELECT * FROM eventos
                WHERE id_evento = ?
                """
                cursor.execute(sql3, [idd])
                resultado_actualizado = cursor.fetchall()
                print("ACTUALIZACIÓN COMPLETA:\n")
                for i in resultado_actualizado:
                    print(i)

                cursor.close()

    except pyodbc.Error as e:
        print(f"Error al consultar la base de datos: {e}")

    finally:
                con.close()

#cancelar asistentes, super similar a la anterior
def cancelar_asistentes(idd,asis):
    con = conectar()
    try:
        if asis <= 0:
            print("POR QUE ELIMININARIA NADA?\n")
            return False
        else:
            cursor = con.cursor()

            sql = """
                    SELECT * FROM eventos
                    WHERE id_evento = ? and registrados >= ?
                    """
            cursor.execute(sql, [idd, asis])
            resultado = cursor.fetchall()

            if not resultado:
                print("No se ha encontrado el evento o esta intentado eliminar de más asistentes")
                return None

            else:
                print("VALORES ENCONTRADOS:\n")
                for i in resultado:
                    print(i)
                print("ACTUALIZANDO REGISTROS...\n")
                sql2 = """
                            UPDATE eventos SET registrados = (registrados - ?) WHERE id_evento = ?
                            """
                cursor.execute(sql2, [asis, idd])
                con.commit()
                sql3 = """
                            SELECT * FROM eventos
                            WHERE id_evento = ?
                            """
                cursor.execute(sql3, [idd])
                resultado_actualizado = cursor.fetchall()
                print("ACTUALIZACIÓN COMPLETA:\n")
                for i in resultado_actualizado:
                    print(i)

                    cursor.close()

    except pyodbc.Error as e:
        print(f"Error al consultar la base de datos: {e}")

    finally:
        con.close()

#insertar un nuevo evento con los registrados en 0
def agregar_evento(nombre, fecha, hora, lugar, cupo):
    con = conectar()
    try:
        cursor = con.cursor()

        print("REGISTRANDO NUEVO EVENTO...")
        sql = """
        INSERT INTO eventos(nombre,fecha,hora,lugar,cupo,registrados)
        VALUES(?,?,?,?,?,0)
        """
        cursor.execute(sql, [nombre, fecha, hora, lugar, cupo])
        con.commit()
        print("EVENTO REGISTRADO")

        cursor.close()
    except pyodbc.Error as e:
        print(f"Error al consultar la base de datos: {e}")

    finally:
        con.close()

#modificando un evento mediante fecha, hora, lugar o cupo
def modificar_evento(eve):
    con = conectar()
    try:
        cursor = con.cursor()

        opc = int(input("Que desea modificar?:"
                  "\n1)fecha"
                  "\n2)hora"
                  "\n3)lugar"
                  "\n4)cupo"))
        if opc == 1:
            n_fecha = input("Ingrese la fecha nueva del evento (en formato YYYY-MM-DD):")
            print("ACTUALIZANDO EVENTO...")
            sql = """
            UPDATE eventos SET fecha = ? where id_evento = ?
            """
            cursor.execute(sql, [n_fecha, eve])
            con.commit()
            print("EVENTO ACTUALIZADO")
        elif opc == 2:
            n_hora = input("Ingrese la hora nueva del evento(en formato 24 horas HH:MM:SS):")
            print("ACTUALIZANDO EVENTO...")
            sql = """
            UPDATE eventos SET hora = ? WHERE id_evento = ?
            """
            cursor.execute(sql, [n_hora, eve])
            con.commit()
            print("EVENTO ACTUALIZADO")
        elif opc == 3:
            n_lugar = input("Ingrese el lugar nuevo del evento(solo texto):")
            print("ACTUALIZANDO EVENTO...")
            sql = """
            UPDATE eventos SET lugar = ? WHERE id_evento = ?
            """
            cursor.execute(sql, [n_lugar, eve])
            con.commit()
            print("EVENTO ACTUALIZADO")
        elif opc == 4:
            n_cupo = int(input("Ingrese el cupo nuevo del evento(numero entero):"))
            print("ACTUALIZANDO EVENTO...")
            sql = """
            UPDATE eventos SET cupo = ? WHERE id_evento = ?
            """
            cursor.execute(sql, [n_cupo, eve])
            con.commit()
            print("EVENTO ACTUALIZADO")
        else:
            print("OPCION NO ENCONTRADA")

        cursor.close()

    except pyodbc.Error as e:
        print(f"Error al consultar la base de datos: {e}")

    finally:
        con.close()

#buscar los proximos eventos con cupo y cuanto caben
def proximos_eventos():
    con = conectar()
    try:
        cursor = con.cursor()

        sql =  """
        SELECT *,(cupo - registrados) AS lugares_disponibles FROM eventos WHERE fecha >= CAST(GETDATE() AS DATE) AND (cupo - registrados) > 0
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print("EVENTOS PROXIMOS DISPONIBLES:\n")
        for i in resultados:
            print(i)

    except pyodbc.Error as e:
        print(f"Error al consultar la base de datos: {e}")

    finally:
        con.close()

#el menu
if __name__ == '__main__':
    while True:
        print("BIENVENIDO AL SISTEMA DE EVENTOS UNIVERSITARIOS")
        opcion = int(input("¿Qué quiere hacer hoy?:\n\n"
                           "1) Mostrar todos los eventos\n"
                           "2) Buscar evento por nombre\n"
                           "3) Consultar eventos con disponibilidad\n"
                           "4) Registrar asistentes\n"
                           "5) Cancelar registros\n"
                           "6) Agregar un evento nuevo\n"
                           "7) Modificar algun evento\n"
                           "8) Mostrar eventos proximos y con disponibilidad\n"
                           "9) SALIR"))
        if opcion == 1:
            mostrar_eventos()
        elif opcion == 2:
            si = input("Ingrese el nombre del evento que busca:")
            consultar_especifico(si)
        elif opcion == 3:
            inscri = int(input("Ingresa el numero de personas que registrara en el evento: "))
            consultar_disponibles(inscri)
        elif opcion == 4:
            identificador = int(input("Ingrese el identificador del evento que busca"))
            n_asistentes = int(input("Ingrese la cantidad de asistentes al evento"))
            registro_asistentes(identificador,n_asistentes)
        elif opcion == 5:
            identificador = int(input("Ingrese el identificador del evento que busca"))
            n_desertores = int(input("Ingrese la cantidad de asistentes que eliminara del evento"))
            cancelar_asistentes(identificador,n_desertores)
        elif opcion == 6:
            nombre = input("Ingrese un nombre para su evento")
            fecha = input("Ingrese la fecha del evento (en el formato YYYY-MM-DD)")
            hora = input("Ingrese la hora del evento (en el formato HH:MM:SS)")
            lugar = input("Ingrese el lugar del evento")
            cupo = int(input("Ingrese el cupo del evento"))
            agregar_evento(nombre,fecha,hora,lugar,cupo)
        elif opcion == 7:
            evento = int(input("Ingrese el id del evento a modificar"))
            modificar_evento(evento)
        elif opcion == 8:
            proximos_eventos()
        elif opcion == 9:
            print("SALIENDO DEL SISTEMA...")
            break