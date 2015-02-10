from tkinter import *
    from random import choice
ventana=tk()
ventana.geometry("700x700+0+0")
ventana.config(bg="blue")
ventana.title("imagenes")
     
    imagen = choice(imageName)
    f = open(imagen)

ventana.mainloop()