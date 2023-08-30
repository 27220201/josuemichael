# 1) Aquí tenemos un diccionario de una persona. ¡Siéntete libre de modificarlo!
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
# a) Comprueba si el diccionario de la persona tiene la clave de habilidades ('skills'); si es así, imprime la habilidad 
# del medio en la lista de habilidades. 2.5ptos
if "skills"  in persona:
    middle_skill = persona["skills"][len(persona["skills"]) // 2]
    print(f"La habilidad del medio es: {middle_skill}")
      
# b) Comprueba si el diccionario de la persona tiene la clave de habilidades; si es así, verifica si la persona 
# tiene la habilidad 'Python' e imprime el resultado. 2.5ptos
if "skills" in persona:
    has_python = "Python" in persona["skills"]
    print(f"¿La persona tiene habilidad en 'Python'?: {has_python}")

# c) Si las habilidades de una persona tienen solo JavaScript y React, imprime ('Él es un desarrollador 
# frontend'), si las habilidades de la persona tienen Node, Python, MongoDB, imprime ('Él es un 
# desarrollador backend'), si las habilidades de la persona tienen React, Node y MongoDB, imprime ('Él es 
# un desarrollador fullstack'), de lo contrario imprime ('título desconocido') - ¡para obtener resultados más 
# precisos, se pueden anidar más condiciones! 3ptos
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



# 2) A partir del archivo de datos proporcionado countries_data.py. Desarrollar lo siguiente:

# a) ¿Cuál es el número total de idiomas en los datos?4ptos
all_languages = set()
for country in countries:
    for language in country["languages"]:
        all_languages.add(language)

print(f"El Total de idiomas en los datos son: {len(all_languages)}")

# b) Encuentra los diez idiomas más hablados a partir de los datos.4ptos
language_count = {}
for country in countries:
    for language in country["languages"]:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
top_languages = sorted_languages[:10]

print("Los diez idiomas más hablados a partir de los datos son:")
for lang, count in top_languages:
    print(f"{lang}: {count} países")

# c) Encuentra los 10 países más poblados del mundo.4pto
sorted_countries = sorted(countries, key=lambda x: x["population"], reverse=True)
top_populated_countries = sorted_countries[:10]

print("Los diez paises más poblados del mundo:")
for country in top_populated_countries:
    print(f"{country['name']}: {country['population']