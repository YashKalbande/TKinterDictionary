from tkinter import *
import json
from difflib import get_close_matches
from PIL import Image, ImageTk

data = json.load(open("data.json"))

def search(word):
    if word in data:
        t1.delete(1.0,END)
        t1.config(fg='blue')
        listboxA.delete(0,END)
        listboxA.insert(0,'Meaning found')
        listboxA.config(fg='green')
        t1.insert(END,data[word])
    elif len(get_close_matches(word,data.keys()))>0:
        t1.config(fg='red')
        t1.delete(1.0,END)
        t1.insert(END,"Did you mean {} to mean : {} ".format (get_close_matches(word,data.keys())[0],data[get_close_matches(word,data.keys())[0]]))
        listboxA.delete(0,END)
        output = get_close_matches(word,data.keys())
        for item in output:
            listboxA.insert(0,item)


#main window
window = Tk()
window.title (" DevNgecu Dictionary")
window.geometry("500x500+350+100")


def close():
    window.destroy()

def dark():
    window.config(bg='#343434')
    l1.config(bg='#343434',fg='white')
    l2.config(bg='#343434',fg='white')
    e1.config(bg="#444444",fg="white")
    e1.config(bg="#444444",fg="white")
    

def light():
    window.config(bg='#bebebe')
    l1.config(bg='white',fg='black')
    l2.config(bg='white',fg='black')
    e1.config(bg="white",fg="black")
    t1.config(bg="white",fg="black")



image = Image.open('WebDevelopemnt.png')
photo_image = ImageTk.PhotoImage(image)
l2 = Label(window,image = photo_image)
l2.pack()
  
#label for the word to search
l1 = Label(window,text="Search")
l1.config(bg='#343434',fg='white')
l1.place(relx=0.2,rely=0.005,relwidth=0.05)




#input of the word to search
e1_value=StringVar()
e1 = Entry(window,textvariable=e1_value,bg="#444444",fg="white")
e1.place(relx=.1,rely=0.5,relwidth=.8,relheight=.1)



#seach button to execute command

b1 = Button(window,text="Search",command= lambda : search(e1_value.get()),relief=RIDGE )
b1.place(relx=.3,rely=.95,relwidth=.3,height=45)



#Close Button
b2 =Button(window,text="Close",command=close,relief=RIDGE )
b2.config(bg='#FA0032',fg='white')
b2.place(relx=.65,rely=.95,relwidth=.3,height=45)

#ouput the definition of the word
t1 = Text(window,fg="white",relief=FLAT,bg="#444444")
t1.place(relx=.3,rely=02.1,relwidth=.65,relheight=.80)


#menu item
menubar = Menu(window)
window.config(menu = menubar)
menubar.config(bg="white")

submenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Themes",menu=submenu)
menubar.add_cascade(label="Exit!",command = close)
submenu.add_command(label="Dark Theme",command=dark)
submenu.add_command(label="Leight Theme",command=light)

background_image=PhotoImage('WebDevelopemnt.png')
background_label =Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

window.mainloop()