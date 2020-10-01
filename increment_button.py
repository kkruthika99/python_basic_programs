from tkinter import *
root =Tk()
count=StringVar()
num=0
count.set(str(num))
def up():
global num
global count
num=num+1
count.set(str(num))
def down():
global num
global count
num=num-1
count.set(str(num))
Ubutton=Button(root,text="UP",command= lambda :up())
Ubutton.pack()
Dbutton=Button(root,text="DOWN",command=lambda :down())
Dbutton.pack()
HOD, Dept. of CSE
Disp=Label(root,textvariable= count)
Disp.pack()
root.mainloop()
