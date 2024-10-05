import csv

# Datos para la columna 'data'
rows = [
    ['dato 1'],
    ['dato 2'],
    ['dato 3'],
    ['dato 4'],
]

file_name = 'archivo.csv'

# Crear y escribir en el archivo CSV
with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Escribir el encabezado
    writer.writerow(['data'])
    
    # Escribir las filas
    writer.writerows(rows)

print(f"Archivo '{file_name}' creado con éxito.")
