import random
from tkinter import *

class GeographyQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Preguntas Geografía")
        self.root.geometry("1000x1500")

        self.texto_bienvenida = (
            "¡Bienvenida a Preguntas y Respuestas de Geografía!\n"
            "Tienes 3 intentos para responder cada pregunta correctamente.\n"
            "Si fallas 3 preguntas habrás perdido ¡Ten cuidado!\n"
            "Si aciertas 5 preguntas habrás ganado.\n"
            "!Mucha suerte! Empezamos"
        )

        self.diccionario_preguntas = {
            "¿Cuál es el río más largo de la Península Ibérica?": "Tajo",
            "¿Cuál es el país más pequeño del mundo?": "Vaticano",
            "¿Qué país del mundo en 2023 tenía más habitantes?": "India",
            "¿Cuál es el río más largo del mundo?": "Nilo",
            "¿Cuántos mares existen en la Tierra?": "60",
            "¿Dónde podemos ver las auroras boreales?": "Polo Norte",
            "¿Dónde podemos ver las auroras australes?": "Polo Sur",
            "¿Qué río pasa por más países?": "Danubio",
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

        self.intentos = 3
        self.aciertos = 0
        self.pregunta_seleccionada = ""
        self.respuesta_correcta = ""

        ## Variables de los componentes de la ventana
        ## Necesitamos 5: 

         ## 1. Label comun que mete el texto de bienvenida
        self.reglas = Label(root, text=self.texto_bienvenida, fg="grey", font=("Comic Sans MS", 18))
        self.reglas.grid(row=0, columnspan=2)
        self.reglas.config(bg="blue", fg="black", bd=20, relief="groove")

        ## 2. Label para mostrar la pregunta 
        self.pregunta_label = Label(root, font=("Comic Sans MS", 18))
        self.pregunta_label.grid(row=1, columnspan=2)
        self.pregunta_label.config(bg="lightgrey", fg="black")

        ## 3. Entry (donde el user va a escribir la respuesta)
        self.caja_respuesta = Entry(root, font=("Comic Sans MS", 18))
        self.caja_respuesta.grid(row=2, column=0)

        ## 4. Boton para que el user valide su respuesta
        self.boton = Button(root, text="Enviar Respuesta", command=self.comprobar_respuesta)
        self.boton.grid(row=2, column=1)

        ## 5. Label para mostrar la respuesta
        self.resultado_label = Label(root, font=("Comic Sans MS", 18))
        self.resultado_label.grid(row=3, columnspan=2)

        ### Inicio del juego
        self.siguiente_pregunta()

    ## Devuelve una pregunta y lo setea en el label de pregunta
    ## Tambieb guardo la respuesta de la pregunta
    def seleccion_pregunta(self):
        self.pregunta_seleccionada = random.choice(list(self.diccionario_preguntas))
        self.respuesta_correcta = self.diccionario_preguntas[self.pregunta_seleccionada]
        self.pregunta_label.config(text=self.pregunta_seleccionada)

    def siguiente_pregunta(self):
        ## Vacio la caja de respuesta
        self.caja_respuesta.delete(0, END)
        ## Vacio el texto de la respuesta
        self.resultado_label.config(text="")
        ## Cojo una pregunta
        self.seleccion_pregunta()

    ## Funcion cuando se clica en el boton
    def comprobar_respuesta(self):
        respuesta = self.caja_respuesta.get().strip().lower()
        ##Si acierta:
        if respuesta == self.respuesta_correcta.strip().lower():
            self.aciertos += 1
            self.resultado_label.config(text="Enhorabuena, acertaste", fg="green")
            ## Miro si con esta respuesta ya ha ganado
            if self.aciertos >= 5:
                self.resultado_label.config(text="¡Ganaste el juego!", fg="blue")
                ##Inhabilto el boton, porque ya ha ganado
                self.boton.config(state=DISABLED)
            else:
                ## Si no ha ganado, genero una nueva pregunta
                self.siguiente_pregunta()
        ##Si ha fallado:
        else:
            self.intentos -= 1
            self.resultado_label.config(text=f"Respuesta incorrecta. Te quedan {self.intentos} intentos", fg="red")
            ## Si el numero de intentos ya es 0, ha perdido
            if self.intentos == 0:
                self.resultado_label.config(text="¡Has perdido el juego!", fg="red")
                self.boton.config(state=DISABLED)
            ## Por el contrario borro la respuesta, y dejo que siga contestando la pregunta
            else:
                self.caja_respuesta.delete(0, END)


ventana = Tk()
app = GeographyQuiz(ventana)
ventana.mainloop()
