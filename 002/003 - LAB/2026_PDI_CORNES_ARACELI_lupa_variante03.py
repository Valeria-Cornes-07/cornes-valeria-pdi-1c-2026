import py5

img = None

def setup():
    global img
    py5.size(800, 400)
    img = py5.load_image(r"C:\Temp\VALE\ISFT 24 CIENCIA DE DATOS E IA\1C 2026\BARRETO\cornes-valeria-pdi-1c-2026\002\003 - LAB\img\gatito.jpg")
    img.resize(400, 400)

def draw():
    py5.background(255)

    # Mostrar la imagen en la mitad izquierda
    py5.image(img, 0, 0)

    # MODIFICACIÓN PEDIDA EN LA CONSIGNA:
    # se quita la protección que limitaba el mouse al área de la imagen
    # ahora se usan directamente las coordenadas reales del cursor
    mx = py5.mouse_x
    my = py5.mouse_y

    # Si el mouse sale de la imagen, estas coordenadas pueden quedar fuera de rango
    # y provocar un error al intentar leer un píxel inexistente
    color_pixel = py5.get_pixels(int(mx), int(my))

    # Separar el color en sus tres canales
    r = py5.red(color_pixel)
    g = py5.green(color_pixel)
    b = py5.blue(color_pixel)

    py5.fill(color_pixel)
    py5.stroke(0)
    py5.rect(450, 50, 300, 300)

    # Mostrar los valores numéricos
    py5.fill(0)
    py5.text_size(18)
    py5.text(f"Posición: ({mx}, {my})", 450, 30)
    py5.text(f"R: {r:.0f}   G: {g:.0f}   B: {b:.0f}", 450, 380)

py5.run_sketch()