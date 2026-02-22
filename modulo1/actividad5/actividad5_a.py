v_list = ["guitarra", "bajo", "bateria", "piano", "violin"]
print("Lista inicial:", v_list)

v_list.insert(2, "amplificador")
print("Lista después de insertar en índice 2:", v_list)

v_list.append("gabinete")
print("Lista después de agregar al final:", v_list)

v_string = "Esta es la tarea del master"
print("Cadena:", v_string)

v_chars = len(v_string)
print("Número de caracteres:", v_string)

v_mayusc = v_string.upper()
print("Cadena en mayúsculas:", v_mayusc)

v_dict = {
    "a": "amarillo",
    "b": "azul",
    "d": "blanco",
    "e": "negro"
}
print("Diccionario inicial:", v_dict)

# 8. Agrega un nuevo elemento al diccionario
v_dict["c"] = "rojo"
print("Diccionario después de agregar elemento:", v_dict)

# 9. Elimina el elemento del índice “c”
del v_dict["c"]
print("Diccionario después de eliminar índice 'c':", v_dict)

v_dict_elements = len(v_dict)
print("Número de elementos en el diccionario final:", v_dict_elements)