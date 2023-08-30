"""
1) Aquí tenemos un diccionario de una persona. ¡Siéntete libre de modificarlo!
persona = {
 'first_name': 'Edem',
 'last_name': 'Terraza',
 'age': 31,
 'country': 'Peru',
 'is_married': True, # 
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 'address': {
 'street': 'Space street',
 'zipcode': '02210'
 }
}
a) Comprueba si el diccionario de la persona tiene la clave de habilidades; si es así, imprime la habilidad 
del medio en la lista de habilidades. 2.5ptos
b) Comprueba si el diccionario de la persona tiene la clave de habilidades; si es así, verifica si la persona 
tiene la habilidad 'Python' e imprime el resultado. 2.5ptos
c) Si las habilidades de una persona tienen solo JavaScript y React, imprime ('Él es un desarrollador 
frontend'), si las habilidades de la persona tienen Node, Python, MongoDB, imprime ('Él es un 
desarrollador backend'), si las habilidades de la persona tienen React, Node y MongoDB, imprime ('Él es 
un desarrollador fullstack'), de lo contrario imprime ('título desconocido') - ¡para obtener resultados más 
precisos, se pueden anidar más condiciones! 3ptos
"""
persona = {
    'first_name': 'Edem',
    'last_name': 'Terraza',
    'age': 31,
    'country': 'Peru',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
#ejercicio 1
if 'skills' in persona:
    habilidades = persona['skills']
    if len(habilidades) > 2:
        middle_skill = habilidades[len(habilidades) // 2]
        print("Habilidad del medio:", middle_skill)
else:
     print("La clave 'skills' no está presente en el diccionario de la persona.")

#ejercico 2

if 'skills' in persona:
    skills_list = persona['skills']
    if 'Python' in skills_list:
        print("La persona tiene la habilidad 'Python'.")
    else:
        print("La persona no tiene la habilidad 'Python'.")
else:
    print("La clave 'skills' no está presente en el diccionario de la persona.")

#ejercicio 3

if 'skills' in persona:
    skills_list = persona['skills']
    
    if 'JavaScript' in skills_list and 'React' in skills_list:
        print("Él es un desarrollador frontend.")
    elif 'Node' in skills_list and 'Python' in skills_list and 'MongoDB' in skills_list:
        print("Él es un desarrollador backend.")
    elif 'React' in skills_list and 'Node' in skills_list and 'MongoDB' in skills_list:
        print("Él es un desarrollador fullstack.")
   
else:
    print("La clave 'skills' no está presente en el diccionario de la persona.")
 
