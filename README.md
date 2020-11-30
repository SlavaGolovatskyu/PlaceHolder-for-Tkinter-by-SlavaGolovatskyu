# PlaceHolder-for-Tkinter
PlaceHolder для ткинтера. Адаптирован для 2-3 Entrys 4 и больше неработают. Если хотите чтоб работал нужно дописать проверки.
Показ работы PlaceHolder-ра здесь https://www.youtube.com/watch?v=b70ydACVMUE&feature=youtu.be

ВЫЗОВ САМОГО PLACEHOLDER-ра
```py
main = PlaceHolder('Login', 'password', 'number')
ent = Entry() # login
ent2 = Entry() # password
ent3 = Entry() # number

def first(event):
  DeletePlaceHolder(1, 3, ent, ent2, ent3)
 
def second(event):
  DeletePlaceHolder(2, 3, ent, ent2, ent3)

def three(event):
  DeletePlaceHolder(3, 3, ent, ent2, ent3)

ent.bind('<Button-1>', first)
ent2.bind('<Button-1>', second)
ent3.bind('<Button-1>', three)
```
  
