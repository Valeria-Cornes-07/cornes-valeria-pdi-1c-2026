# Trabajo Práctico 006 — Fotografía Digital

## De la cámara oscura a la imagen intencional
### Óptica, composición y postproceso en fotografía digital

**Materia:** Procesamiento Digital de Imágenes  
**Institución:** IFTS24  
**Alumna:** Valeria Cornes  
**Fecha:** Mayo 2025  

---

# Descripción

Este trabajo práctico integra conceptos de:

- óptica,
- fotografía digital,
- composición visual,
- espacios de color,
- procesamiento digital de imágenes,
- y análisis visual.

El objetivo fue explorar cómo las decisiones técnicas y compositivas modifican la construcción y la lectura de una imagen.

---

# Contenido del trabajo

## Parte 1 — Cámara oscura y procesamiento digital

- Construcción de una cámara oscura
- Registro de proyección invertida
- Conversión RGB ↔ HSV
- Ecualización del canal V
- Análisis mediante histogramas

## Parte 2 — Composición y lenguaje visual

- Fotografía de simplicidad visual
- Reencuadre y reinterpretación
- Punto de vista y construcción narrativa
- Fotografía basada en la luz

## Parte 3 — Reflexión y selección

- Selección crítica de imágenes
- Reflexión final sobre intención visual y postproceso

---

# Tecnologías utilizadas

- Python
- OpenCV
- NumPy
- Matplotlib
- Google Colab

---

# Estructura del repositorio

```text
006_fotografia_digital/
│
├── README.md
├── presentacion.pdf
│
├── imagenes/
│   ├── originales/
│   ├── procesadas/
│   └── descartes/
│
├── codigo/
│   ├── ecualizacion_hsv.py
│   ├── escala_grises.py
│   └── otros_scripts.py
│
└── recursos/

# Procesamientos realizados

# Ecualización HSV

Se convirtió la imagen al espacio HSV para trabajar únicamente sobre el canal de brillo (V), mejorando el contraste sin alterar directamente la información cromática original.

# Conversión a escala de grises

La transformación a escala de grises permitió reducir ruido visual y enfatizar:

- formas,
- siluetas,
- contraste,
- dirección de la luz.

# Conceptos trabajados
- propagación rectilínea de la luz
- proyección invertida
- composición visual
- separación sujeto/fondo
- reencuadre
- punto de vista
- luz lateral y contraluz- 
arrativa visual
- postprocesamiento consciente

# Reflexión

El trabajo permitió comprender que fotografiar no consiste solamente en registrar una escena, sino también en:

- decidir qué mostrar,
- cómo encuadrarlo,
- desde dónde mirar,
- cómo el procesamiento digital modifica la lectura visual final.

