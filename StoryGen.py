
import numpy as np
import tkinter as tk

#tkinter setup screen
Screen = Tk()
Screen.title("Nathaniel James 'Madlibs' project")
Screen.geometry('1000x1000')
Screen.config(bg="#F5B847")
Label(Screen, text='Nathaniel James Madlibs project').place(x=100, y=20)
#creating buttons
Story1Button = Button(Screen, text='A memorable day', font=("Lato", 13),command=lambda: Story1(Screen),bg='White')
Story1Button.place(x=140, y=90)
Story2Button = Button(Screen, text='Ambitions', font=("Lato", 13),command=lambda: Story2(Screen), bg='White')
Story2Button.place(x=150, y=150)
 
Screen.update()
Screen.mainloop()

