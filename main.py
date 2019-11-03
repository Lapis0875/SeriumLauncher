from tkinter import *


def btnClicked():
    print('Button is Clicked!')


window = Tk()
window.title('Serium Launcher')
label = Label(window, text='Welcome to Python TK Interface Moudle!', bg='gray')
btn = Button(window, text='Click Me', bg='gray', command=btnClicked)
label.pack()    #윈도우에 라벨 위치시키기
btn.pack()      #윈도우에 버튼 위치시키기


window.mainloop()