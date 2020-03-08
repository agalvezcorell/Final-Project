import flujo.funimagen as funimg
import pandas as pd
import numpy as np
from PIL import Image


def generaLaImagen(array,pol):
    """
    Recibe el array y la polaridad y lo normaliza
    y lo mezcla y genera la imagen.
    """
    if pol < -0.3:
        print("negativo")
        normalizado = funimg.normalizaNegativo(array)
        clave = "negativos"

    elif pol >0.3:
        print("positivo")
        normalizado = funimg.normalizaPositivo(array)
        clave = "positivos"

    else:
        print("neutro")
        normalizado = funimg.normalizaNeutro(array)
        clave = "neutros"
    
    #elegimos forma de mezclar los colores
    if array.max() >= 0.015:
        print("forma1")
        normalizado = funimg.formaUno(normalizado)
    else:
        print("forma2")
        normalizado = funimg.formaDos(normalizado)

    r = "R"
    g = "G"
    b = "B"
    print("Creando capas rgb...")
    capar,capag,capab = funimg.capa(normalizado,r,clave),funimg.capa(normalizado,g,clave),funimg.capa(normalizado,b,clave)
    print("Capas Generadas")
    rf, gf, bf = funimg.arrayReshape(capar), funimg.arrayReshape(capag), funimg.arrayReshape(capab)
    capas = [rf,gf,bf]


    imagen = np.stack(capas, axis=2).astype('uint8')
    imagen = Image.fromarray(imagen)
    imagen.save("creada.jpg")
    print("Imagen creada")