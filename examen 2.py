###########################################
###   SEGUNDO EXAMEN DE IS-182
### No    APELLIDOS      NOMBRES          
###
###
###########################################
###########################################
###   PROBLEMA  01
###########################################
'''
Escriba un programa que solicite un nombre de archivo, luego abra ese archivo y lo lea, y cuente las palabras: computador y computadoras. 
Utilice el archivo computador.txt para generar el resultado.

'''
def contar_palabras(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            
            contador_computador = 0
            contador_computadoras = 0
            
            for palabra in palabras:
                if palabra.lower() == 'computador':
                    contador_computador += 1
                elif palabra.lower() == 'computadoras':
                    contador_computadoras += 1
            
            return contador_computador, contador_computadoras
        
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return 0, 0

def main():
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    contador_computador, contador_computadoras = contar_palabras(nombre_archivo)
    
    print(f"La palabra 'computador' aparece {contador_computador} veces.")
    print(f"La palabra 'computadoras' aparece {contador_computadoras} veces.")
    

print(main())





###########################################
###   PROBLEMA  02
###########################################
'''
Escriba un programa que solicite un nombre de archivo, luego abra ese archivo y lo lea, buscando líneas del formulario:

X-DSPAM-Confidence:    0.8475

Cuente estas líneas y extraiga los valores de punto flotante de cada una de las líneas y calcule el promedio de esos valores. 
La salida produce el siguiente resultado del promedio es:

'''






###########################################
###   PROBLEMA  03
###########################################
'''


'''






###########################################
###   PROBLEMA  04
###########################################
'''


'''






###########################################
###   PROBLEMA  05
###########################################
'''


'''
