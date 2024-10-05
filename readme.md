# Coupling and Cohesion

El programa 
1. crea un archivo `.csv` a partir de un `dataframe`
2. Lee el archivo `.csv`
3. Busca en las filas del archivo un término de búsqueda específico
4. Guarda los resultados filtrados en otro archivo `.csv`

## Crea un ambiente virtual
Usa venv o conda para crear un ambiente aislado en tu equipo.
 
```cmd
python -m venv my_env
```

```
#En windows
.\my_env\Scripts\activate

#En linux
source my_env/bin/activate
```

## Instala las dependencias con pip

```
pip install -r requirements.txt
```

## Ejecuta el código
 
Ejecuta el programa en el siguiente orden.

1. `python create_file.py`
2. `python main.py`

## Ejercicio

Mejorar el nivel de cohesión y acople en la función `main.py`.
¿Es necesario crear otros archivos para manejar las lógicas de negocio, o es suficiente con crear otras funciones o clases?