from tkinter import Tk, Frame, Label
from PIL import Image, ImageTk

# Create the main window
raiz = Tk()
ico = Image.open('test.icns')
photo = ImageTk.PhotoImage(ico)
raiz.wm_iconphoto(False, photo)
# Set the title of the window
raiz.title("Preguntas Geografía")

# Configure the background color of the window
raiz.config(bg="white")



# Create a frame
miFrame = Frame(raiz)
miFrame.pack(fill="y", expand=True)

# Configure the frame
miFrame.config(width=650, height=350, bg="pink", bd=35, relief="groove", cursor="hand2")

# Add a label to the frame
miLabel = Label(miFrame, text="Bienvenidos al juego de Geografía", fg="grey", font=("Comic Sans MS", 18))
miLabel.pack()

# Start the Tkinter event loop
raiz.mainloop()
