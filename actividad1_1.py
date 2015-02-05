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

def filtro_umbral(image):
    escala_grises(image)
    pic = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
 
            (R, G, B) = pic[i,j]
            intensity = R
            if intensity < 128:
                intensity = 0
            else:
                intensity = 255
            R = G = B = intensity
            pic[i,j] = (R, G, B)
    return pic
 
def filtro_media(image):
    escala_grises(image)
    pic = image.load()
    pic_copy = (image.copy()).load()
 
    for i in range(image.size[0]):
        for j in range(image.size[1]):
 
            temp = []
            for h in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if h >= 0 and l >= 0 and h < image.size[0] and l < image.size[1]:
                        temp.append(pic_copy[i, j][0])
 
            temp.sort()
            R = G = B = int(temp[int(len(temp)/2)])
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