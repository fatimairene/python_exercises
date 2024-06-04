import random
from tkinter import *

diccionario_preguntas = {
    "¿Cuál es el río más largo de la Península Ibérica?": "Tajo",                     
    "¿Cuál es el país más pequeño del mundo?": "Vaticano",
    "¿Qué país del mundo en 2023 tenía más habitantes?": "India",
    "¿Cuál es el río más largo del mundo?": "Nilo",
    "¿Cuántos mares existen en la Tierra?": "60",
    "¿Dónde podemos ver las auroras boreales?": "Polo Norte",
    "¿Dónde podemos ver las auroras australes?": "Polo Sur",
    "¿Qué río pasa por más paises?": "Danubio",  
    "¿Cuál es la capital de España?": "Madrid",
    "¿Cuántos países hay en el mundo? Por favor, introduce un número": "195",
    "¿Cuál es la montaña más alta de la Tierra?": "Everest",
    "¿Cuántos océanos hay en el mundo? Por favor, introduce un número": "5",
    "¿Qué país tiene la población más grande del mundo?": "China",
    "¿Cuál es el desierto más grande del mundo?": "Sahara",
    "¿Cuántos estados tiene Estados Unidos? Por favor, introduce un número": "50",
    "¿Cuál es la capital de Australia?": "Canberra",
    "¿Qué país es el más grande en términos de superficie terrestre?": "Rusia",
    "¿Cuál es el lago más grande del mundo?": "Mar Caspio",
    "¿En qué continente se encuentra Egipto?": "África",
    "¿Cuál es la capital de Brasil?": "Brasilia",
    "¿Qué país tiene la mayor cantidad de islas?": "Suecia",
    "¿Cuántos habitantes tiene aproximadamente la Tierra? Por favor, introduce un número": "7800 millones",
    "¿Cuál es la lengua oficial de Canadá?": "Inglés y francés",
    "¿Cuál es la ciudad más poblada del mundo?": "Tokio",
    "¿Cuál es la moneda oficial de la Unión Europea?": "Euro",
    "¿Cuál es el país más pequeño del mundo?": "Vaticano",
    "¿Cuál es el volcán más activo del mundo?": "Kilauea"
    }

textoBienvenida = "¡Bienvenida a Preguntas y Respuestas de Geografía!\nTienes 3 intentos para responder cada pregunta correctamente.\nSi fallas 3 preguntas habrás perdido ¡Ten cuidado!\nSi aciertas 5 preguntas habrás ganado.\n!Mucha suerte! Empezamos"


## FUNCTIONES

def seleccion_pregunta():
    preguntaText = random.choice(list(diccionario_preguntas))
    return preguntaText


## JUEGOOO 
ventana=Tk()
ventana.title("Preguntas Geografía")
ventana.geometry("1000x1500")

reglas= Label(ventana,text = textoBienvenida,fg="grey",font=("Comic Sans MS",18))
reglas.pack(anchor="nw")
reglas.config(bg="blue", fg="black", bd=20, relief="groove")
reglas.grid(row=0)

preguntaText = seleccion_pregunta()
pregunta = Label(ventana,text = preguntaText,font=("Comic Sans MS",18))
pregunta.grid(row=1)
pregunta.config (bg="lightgrey", fg="black")
caja_respuesta = Entry(ventana, font=("Comic Sans MS",18))
caja_respuesta.grid(row=2)


def comprobar_respuesta():
    respuesta = caja_respuesta.get().strip().lower()
    respuesta_correcta = diccionario_preguntas[preguntaText].strip().lower()
    print(respuesta)
    if respuesta == respuesta_correcta.strip().lower():
        texto2 = "Enhorabuena, acertaste"

        acierto = Label(ventana,text=texto2,font=("Helvetica",40))
        acierto.grid(row=3)
        nuevaPregunta =  seleccion_pregunta()
        pregunta.config(text=nuevaPregunta)
    else:
        texto2 = "Fallaste, vuelve a intentarlo"
        fallo = Label(ventana,text=texto2,font=("Helvetica",40))
        fallo.grid(row=3)

boton=Button(ventana, text="Click aquí", command=comprobar_respuesta())
boton.grid(row=2, column=1)

   






    
    




ventana.mainloop() 
