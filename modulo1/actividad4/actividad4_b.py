segundos_por_hora = 3600
segundos_por_dia =  segundos_por_hora * 24

horas_por_dia_float = segundos_por_dia / segundos_por_hora
horas_por_dia_int = segundos_por_dia // segundos_por_hora

print(horas_por_dia_float)
print(horas_por_dia_int)

if horas_por_dia_float == horas_por_dia_int:
    print("Datos validos.")
else:
    print("Datos inconsistentes.")