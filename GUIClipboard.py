#modules used
import tkinter as tk
from pathlib import Path
import clipboard
from PIL import ImageTk ,Image

#path used (this allows me to keep all the images in one place) 
a=Path("Images")

#functions
"""
These functions solely tend to the Delete buttons(2,4,6).We clear the entry  and then reset the clipboard variable."""

def reset1():
    Entry1.delete(0,'end')
    clipboard.copy("")
def reset2():
    Entry2.delete(0,'end')
    clipboard.copy("")
def reset3():
    Entry3.delete(0,'end')
    clipboard.copy("")
    
#Tkinter body
"""Just configure functions for the various GUI components"""
top=tk.Tk()
top.geometry("600x450+650+150")
top.minsize(148, 1)
top.maxsize(1924, 1055)
top.resizable(1, 1)
top.title("GUI Clipboard")
top.configure(background="#353839")

Label1 = tk.Label(top)
Label1.place(relx=0.033, rely=0.733, height=106, width=562)
Label1.configure(background="#d9d9d9")
Label1.configure(text="Label Picture")
Label1.configure(background="#FFFFFF")

Entry1 = tk.Entry(top)
Entry1.place(relx=0.033, rely=0.178,height=54, relwidth=0.707)
Entry1.configure(background="white")
Entry1.configure(font="TkFixedFont")


Button1 = tk.Button(top)
Button1.place(relx=0.767, rely=0.178, height=53, width=56)
Button1.configure(background="#d9d9d9")
Button1.configure(command=lambda :clipboard.copy(Entry1.get()))
Button1.configure(text="Copy")

Button2 = tk.Button(top)
Button2.place(relx=0.883, rely=0.178, height=53, width=56)
Button2.configure(background="#d9d9d9")
Button2.configure(command=reset1)
Button2.configure(text="Del")

Entry2 = tk.Entry(top)
Entry2.place(relx=0.033, rely=0.356,height=54, relwidth=0.707)
Entry2.configure(background="white")

Button3 = tk.Button(top)
Button3.place(relx=0.767, rely=0.356, height=53, width=56)
Button3.configure(background="#d9d9d9")
Button3.configure(command=lambda :clipboard.copy(Entry2.get()))
Button3.configure(text="Copy")

Button4 = tk.Button(top)
Button4.place(relx=0.883, rely=0.356, height=53, width=56)
Button4.configure(background="#d9d9d9")
Button4.configure(command=reset2)
Button4.configure(text="Del")

Entry3 = tk.Entry(top)
Entry3.place(relx=0.033, rely=0.533,height=54, relwidth=0.707)
Entry3.configure(background="white")

Button5 = tk.Button(top)
Button5.place(relx=0.767, rely=0.533, height=53, width=56)
Button5.configure(background="#d9d9d9")
Button5.configure(command=lambda :clipboard.copy(Entry3.get()))
Button5.configure(text="Copy")

Button6 = tk.Button(top)
Button6.place(relx=0.883, rely=0.533, height=53, width=56)
Button6.configure(background="#d9d9d9")
Button6.configure(command=reset3)
Button6.configure(text="Del")
"""try and except block checks if there is any error in importing the images"""
try:
    img1 = ImageTk.PhotoImage(Image.open(a/"copy.png").resize((53,56)))
    img2 = ImageTk.PhotoImage(Image.open(a/"trashcan.png").resize((53,56)))
    img3 = ImageTk.PhotoImage(Image.open(a/"label_image.png")) 
    Button6.configure(image=img2)
    Button5.configure(image=img1)
    Button4.configure(image=img2)
    Button3.configure(image=img1)
    Label1.configure(image=img3)
    Button1.configure(image=img1)
    Button2.configure(image=img2)
except:
    print("Error in loading images!")
    

top.mainloop()




