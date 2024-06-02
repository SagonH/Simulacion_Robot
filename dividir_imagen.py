from PIL import Image  # Importa el módulo Image de la librería PIL (Python Imaging Library)
import os  # Importa el módulo os para interactuar con el sistema operativo

def dividir_guardar_imagen(ruta_imagen, carpeta_destino, divisiones_por_columna):
    # Verificar si la imagen existe
    if not os.path.exists(ruta_imagen):
        print(f"Error: La imagen {ruta_imagen} no existe.")
        return

    # Cargar la imagen
    try:
        img = Image.open(ruta_imagen)
        img.load()  # Asegurarse de que la imagen se ha cargado completamente
        ancho, alto = img.size  # Obtener las dimensiones de la imagen (ancho x alto)
    except Exception as e:
        print(f"Error al abrir la imagen: {e}")
        return

    # Calcular el tamaño de cada cuadrado basado en el número de divisiones por columna
    tamano_cuadrado = ancho // divisiones_por_columna
    # Calcular el número de divisiones por fila basado en el tamaño del cuadrado
    divisiones_por_fila = alto // tamano_cuadrado

    # Crear la carpeta de destino si no existe
    os.makedirs(carpeta_destino, exist_ok=True)

    # Dividir y guardar cada cuadrado
    contador = 0  # Contador para nombrar cada archivo de imagen resultante
    for i in range(divisiones_por_fila):
        for j in range(divisiones_por_columna):
            # Coordenadas del cuadrado en la imagen original
            izquierda = j * tamano_cuadrado
            superior = i * tamano_cuadrado
            derecha = izquierda + tamano_cuadrado
            inferior = superior + tamano_cuadrado

            # Cortar y guardar el cuadrado como un archivo de imagen separado
            try:
                cuadrado = img.crop((izquierda, superior, derecha, inferior))
                nombre_archivo = f"tile ({contador + 1}).png"  # Nombre del archivo de imagen
                cuadrado.save(os.path.join(carpeta_destino, nombre_archivo))  # Guardar el cuadrado
                contador += 1  # Incrementar el contador para el siguiente cuadrado
            except Exception as e:
                print(f"Error al cortar o guardar el cuadrado: {e}")

    img.close()  # Asegurarse de cerrar la imagen al finalizar

# Llama a la función dividir_guardar_imagen con los argumentos específicos
dividir_guardar_imagen(r"tiles/mapa.png", "tiles", 60)  # Ejemplo: Divide en 13 columnas


