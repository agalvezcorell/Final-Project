import nltk
import pandas as pd
import numpy as np
from PIL import Image
from nltk.tokenize import sent_tokenize, word_tokenize 
import gensim 
from gensim.models import Word2Vec 
from textblob import TextBlob
import funtexto as funt  
from random import sample


#lee texto
sample = open("../input/prueba.txt") 
s = sample.read() 
print("Leyendo texto")
#traduce al inglés
trad = TextBlob(f"{s}")
en = str(trad.translate(from_lang="es",to="en"))

# Reemplaza los saltos de línea por espacios en blanco
f = en.replace("\n", " ") 
  
data = [] 

# itera sobre el texto
for i in sent_tokenize(f): 
    temp = [] 
      
    # añade palabras tokenizadas a una lista temporal
    for j in word_tokenize(i): 
        temp.append(j.lower()) 
          
    data.append(temp) 
# crea el SkipGram model
model2 = gensim.models.Word2Vec(data, min_count = 1, size = 30, 
                                             window = 5, sg = 1) 

print("Generando Modelo")
#Generamos un array de similaridad de features con sol
palabra = model2["mother"]
print(palabra)

print("Normalizando valores")
#normalizamos valores entre 0 y 991
normalizado = ((palabra-palabra.max())*((0-991)/(palabra.min()-palabra.max())))+991

#convierto a entero
normalizado = normalizado.astype(int)

#elegimos forma de mezclar los colores
if palabra.max() >= 0.015:
    print("forma1")
    normalizado = funt.formaUno(normalizado)
else:
    print("forma2")
    normalizado = funt.formaDos(normalizado)



#creamos 3 capas obteniendo los colores de la columna rgb del dataset
r = "R"
g = "G"
b = "B"
print("Creando capas rgb...")
capar,capag,capab = funt.capa(normalizado,r),funt.capa(normalizado,g),funt.capa(normalizado,b)


print("Dando forma a las capas")
rf, gf, bf = funt.arrayReshape(capar), funt.arrayReshape(capag), funt.arrayReshape(capab)
capas = [rf,gf,bf]

#convertimos array en imagen
imagen = np.stack(capas, axis=2).astype('uint8')
imagen = Image.fromarray(imagen)
imagen.save("../creada.jpg")
print("Imagen creada")