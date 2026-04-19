import py5

img = None

def setup():
    global img
    py5.size(800, 400)
    img = py5.load_image(r"C:\Temp\VALE\ISFT 24 CIENCIA DE DATOS E IA\1C 2026\BARRETO\cornes-valeria-pdi-1c-2026\002\003 - LAB\img\gatito.jpg")
    img.resize(400, 400)

def draw():
    py5.background(35)

    # Se dibuja la imagen original en la mitad izquierda
    py5.image(img, 0, 0)

    # Se cargan los píxeles de la imagen original y del lienzo
    img.load_pixels()
    py5.load_pixels()

    for x in range(img.width):
        for y in range(img.height):

            indice_img = x + y * img.width
            pixel = img.pixels[indice_img]

            # Se separan los tres canales del píxel original
            r = py5.red(pixel)
            g = py5.green(pixel)
            b = py5.blue(pixel)

            # MODIFICACIÓN PEDIDA EN LA CONSIGNA:
            # se elimina por completo el canal rojo
            # esto hace que la imagen resultante conserve solo verde y azul
            r = 0

            # Se escribe el nuevo píxel en la mitad derecha del lienzo
            indice_canvas = (x + 400) + y * py5.width
            py5.pixels[indice_canvas] = py5.color(r, g, b)

    # Se actualiza el lienzo con los cambios realizados
    py5.update_pixels()

py5.run_sketch()