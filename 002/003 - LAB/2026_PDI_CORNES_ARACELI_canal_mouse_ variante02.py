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

    img.load_pixels()
    py5.load_pixels()

    for x in range(img.width):
        for y in range(img.height):

            indice_img = x + y * img.width
            pixel = img.pixels[indice_img]

            # Se extraen los canales del píxel original
            r = py5.red(pixel)
            g = py5.green(pixel)
            b = py5.blue(pixel)

            indice_canvas = (x + 400) + y * py5.width

            # MODIFICACIÓN PEDIDA EN LA CONSIGNA:
            # se intercambian las posiciones del rojo y del azul
            # donde antes iba (r, g, b), ahora va (b, g, r)
            # la imagen sigue siendo válida matemáticamente, pero los colores se alteran
            py5.pixels[indice_canvas] = py5.color(b, g, r)

    py5.update_pixels()

py5.run_sketch()