import py5

img = None

def setup():
    global img
    py5.size(800, 400)
    img = py5.load_image(r"C:\Temp\VALE\ISFT 24 CIENCIA DE DATOS E IA\1C 2026\BARRETO\cornes-valeria-pdi-1c-2026\002\003 - LAB\img\gatito.jpg")
    img.resize(400, 400)

def draw():
    py5.background(35)

    # Se dibuja la imagen original a la izquierda
    py5.image(img, 0, 0)

    # MODIFICACIÓN PEDIDA EN LA CONSIGNA:
    # en lugar de controlar el rojo, se controla el verde con la posición X del mouse
    factor_verde = py5.remap(py5.mouse_x, 0, py5.width, 0, 2.5)

    # Agregado sugerido por la consigna:
    # se usa la posición Y del mouse para crear un segundo factor y controlar el azul
    factor_azul = py5.remap(py5.mouse_y, 0, py5.height, 0, 2.5)

    img.load_pixels()
    py5.load_pixels()

    for x in range(img.width):
        for y in range(img.height):

            indice_img = x + y * img.width
            pixel = img.pixels[indice_img]

            r = py5.red(pixel)
            g = py5.green(pixel)
            b = py5.blue(pixel)

            # MODIFICACIÓN PEDIDA:
            # se aplica el factor al canal verde en vez de al rojo
            g = g * factor_verde

            # MODIFICACIÓN ADICIONAL SUGERIDA:
            # se aplica un segundo factor al canal azul según la posición Y del mouse
            b = b * factor_azul

            # Se limitan los valores para no superar el máximo permitido en RGB
            if g > 255:
                g = 255
            if b > 255:
                b = 255

            indice_canvas = (x + 400) + y * py5.width
            py5.pixels[indice_canvas] = py5.color(r, g, b)

    py5.update_pixels()

py5.run_sketch()