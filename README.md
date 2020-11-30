# PlaceHolder-for-Tkinter
PlaceHolder для ткинтера. Адаптирован для 3 Entrys 2, 4 и больше неработают. Если хотите чтоб работал нужно дописать проверки.
Показ работы PlaceHolder-ра здесь https://www.youtube.com/watch?v=b70ydACVMUE&feature=youtu.be

ВЫЗОВ САМОГО PLACEHOLDER-ра
```py
from tkinter import *

root = Tk()
main = PlaceHolder('Login', 'password', 'number')
ent = Entry(root) # login
ent2 = Entry(root) # password
ent3 = Entry(root) # number

def first(event):
  main.DeletePlaceHolder(1, 3, ent, ent2, ent3)
 
def second(event):
  main.DeletePlaceHolder(2, 3, ent, ent2, ent3)

def three(event):
  main.DeletePlaceHolder(3, 3, ent, ent2, ent3)

ent.bind('<Button-1>', first)
ent2.bind('<Button-1>', second)
ent3.bind('<Button-1>', three)

insertNumb()
packEntrys()

def insertNumb():
  ent.insert(0, 'login')
  ent2.insert(0, 'password')
  ent3.insert(0, 'number')
  
def packEntrys():
  ent.pack()
  ent2.pack()
  ent3.pack()

root.mainloop()
```
  
