import json

class Person:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f"[nombre: {self.nombre}, apellido: {self.apellido}, edad: {self.edad}]"


def generate_dictionary(list):
    if len(list) != 3:
        print("La lista no contien 3 elementos")
        return None

    return {
        'nombre': list[0],
        'apellido': list[1],
        'edad': list[2]
    }

persons_list = []
persons_list.append(generate_dictionary(["Oscar", "Hernandez", 44]))
persons_list.append(generate_dictionary(["Ivan", "Ventura", 44]))
persons_list.append(generate_dictionary(["Dave", "Mustain", 64]))

with open("nombres.json", "w") as json_file:
    json.dump(persons_list, json_file, indent=1)

for persona in persons_list:
    persona = Person(persona["nombre"], persona["apellido"], persona["edad"]);
    print(str(persona))