from tkinter import *
root=Tk()


def send():
    send="You =>"+e.get()
    txt.insert(END,'\n'+send)
    if(e.get()=='hello'):
        txt.insert(END,"\n"+"Bot => hi")
    elif(e.get()=='hi'):
        txt.insert(END,"\n"+"Bot => Hello")
    elif(e.get()=='how are you'):
        txt.insert(END,"\n"+"Bot => fine and you")
    elif(e.get()=='fine'):
        txt.insert(END,"\n"+"Bot => nice to hear")
    else:
        txt.insert(END,"\n"+"Bot => sorry i did't get it")
    e.delete(0,END)
    
txt=Text(root)
txt.grid(row=0, column=0)
e=Entry(root,width=100)
send=Button(root,text="send",bg='lightgreen',fg='black',command=send).grid(row=1, column=1)
e.grid(row=1,column=0)
root.title('Welcome to My Chatbot!')
root.mainloop()
