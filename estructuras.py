import sys
import xml.etree.ElementTree as ET
import pacientes


def mostrar_menu():
    print('-------------------------------')
    print('1. Realizar estudio paciente')
    print('2. Generar Reporte de pacientes')
    print('3. Salir')
    print('-------------------------------')
    print('Porfavor selecione una opcion')

    opcion = str(input())

    if opcion == '1':
        print('Porfavor introduzca la ruta al archivo')
        ruta_archivo = input()

        paciente = obtencion_datos(ruta_archivo)

    elif opcion == '2':
        print('generando reporte de pacientes')
    elif opcion == '3':
        sys.exit()

def obtencion_datos(ruta):
    archivo_xml = ET.parse(ruta)

    raiz = archivo_xml.getroot()

    datos_celdas_cont = ''

    print('porfavor introduzca el nombre del paciente a examinar')
    entrada = input()


    for datos in raiz.findall('paciente'):
        #print(datos)
        periodo = datos.find('periodos').text
        matriz = datos.find('m').text
        #print(periodo,matriz)
        for paciente in datos.findall('datospersonales'):
            #print(paciente)
            nombre_paciente = paciente.find('nombre').text
            edad_paciente = paciente.find('edad').text
            #print(nombre_paciente,edad_paciente)
            for datos_celdas in datos.iter('celda'):
                fila = datos_celdas.get('f')
                columna = datos_celdas.get('c')
                datos_celdas_cont += str(fila) + ',' + str(columna) + ';'
                #print(f"La fila se {fila} y la columna es {columna}")
        if entrada == nombre_paciente:
            print(f"mi nombre es {nombre_paciente} y mi edad es {edad_paciente}")
            print(f"mis periodos son de {periodo} y la matriz a usar es de {matriz}")
            print('mis celulas infectadas se encuentran de la siguiente forma')
            print(f"Mis celdas contagiadas son las siguientes {datos_celdas_cont}")
            mi_paciente = pacientes.persona(nombre_paciente,edad_paciente,periodo,matriz,datos_celdas_cont)
            return mi_paciente

  
        
