#!/usr/bin/python
from PIL import Image
import sys, time, random
 
def escala_grises(image):
    pic = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
 
            (R, G, B) = pic[i,j]
            # Grayscale
            intensity = int((R+G+B)/3)
            R = G = B = intensity
            pic[i,j] = (R, G, B)
    return pic
 
def escala_grises_mas(image):
    pic = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
 
            (R, G, B) = pic[i,j]
            # Grayscale mas claro
            intensity = int((R+G+B)/3)+10
            if intensity>=255:
                R = G = B = 255
            else:    
                R = G = B = intensity
            pic[i,j] = (R, G, B)
    return pic

def escala_grises_menos(image):
    pic = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
 
            (R, G, B) = pic[i,j]
            # Grayscale menos claro
            intensity = int((R+G+B)/3)-10
            if intensity<=0:
                R = G = B = 0
            else:
                R = G = B = intensity-1
            pic[i,j] = (R, G, B)
    return pic

efecto = {
    "grayscale":escala_grises,
    "grises_mas":escala_grises_mas,
    "grises_menos":escala_grises_menos
    }
 
def aplicar_efecto(nImagen, nOutput, aplicar_efectos=[]):
    image = Image.open(nImagen)
    for i in aplicar_efectos:
        pic = efecto[i](image)
    image.save(nOutput)
 
def main():
    aplicar_efecto(sys.argv[1], "grayscale"+"_"+sys.argv[1], ["grayscale"])
    aplicar_efecto(sys.argv[1], "grises_mas"+"_"+sys.argv[1], ["grises_mas"])
    aplicar_efecto(sys.argv[1], "grises_menos"+"_"+sys.argv[1], ["grises_menos"])
    
main()