persona = {
 'first_name': 'Michael',
 'last_name': 'Hinostroza',
 'age': 20,
 'country': 'Peru',
 'is_married': True, #
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 'address': {
 'street': 'Space street',
 'zipcode': '05000'
 }
}

#a)Comprueba si el diccionario de la persona tiene la clave de habilidades; si es así, imprime la habilidad del medio en la lista de habilidades. 


if "skills" in persona:
    middle_skill = persona["skills"][len(persona["skills"]) // 2]
    print(f"La habilidad del medio es: {middle_skill}")

#b)Comprueba si el diccionario de la persona tiene la clave de habilidades; si es así, verifica si la persona tiene la habilidad 'Python' e imprime el resultado.
if "skills" in persona:
    has_python = "Python" in persona["skills"]
    print(f"¿Tiene habilidad en Python?: {has_python}")
    
#c)Si las habilidades de una persona tienen solo JavaScript y React, imprime ('Él es un desarrollador frontend'), si las habilidades de la persona tienen Node, Python, MongoDB, imprime ('Él es un desarrollador backend'), si las habilidades de la persona tienen React, Node y MongoDB, imprime ('Él es un desarrollador fullstack'), de lo contrario imprime ('título desconocido') - ¡para obtener resultados más precisos, se pueden anidar más condiciones!
if "skills" in persona:
    skills = set(persona["skills"])
    if skills == {"JavaScript", "React"}:
        print("Él es un desarrollador frontend")
    elif skills == {"Node", "Python", "MongoDB"}:
        print("Él es un desarrollador backend")
    elif skills == {"React", "Node", "MongoDB"}:
        print("Él es un desarrollador fullstack")
    else:
        print("título desconocido")
        