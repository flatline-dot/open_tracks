from tkinter import *

window = Tk()
size = window.winfo_screenwidth()
size1 = window.winfo_screenheight()
s = window.winfo_screen()
print(s)
window.geometry(f"{int(size * 0.3)}x500")

frame = Frame(window, height=5, relief=RAISED, borderwidth=1)
frame.grid(columnspan=1)
label = Label(frame, text='ДЫиапозона', borderwidth=1, font='Times 12', width=5, height=1, background='silver',)
label.grid()

frame1 = Frame(window, height=5, relief=RAISED, borderwidth=1)
frame1.grid(row=0, column=1)
label1 = Label(frame1, text='Кол-во в сценарии', borderwidth=1, font='Times 12', width=5, height=1, background='silver',)
label1.grid()


frame2 = Frame(window, height=5, relief=RAISED, borderwidth=1)
frame2.grid(row=0, column=2)
label2 = Label(frame2, text='Обнаружено', borderwidth=1, font='Times 12', width=5, height=1, background='silver')
label2.grid()



frame3 = Frame(window, height=5, relief=RAISED, borderwidth=1)
frame3.grid(row=0, column=3)
label3 = Label(frame3, text='Решение', borderwidth=1, font='Times 12', width=5, height=1, background='silver')
label3.grid()


for i in range(1, 18):
    for j in range(4):
        frame = Frame(window, height=5, relief=RAISED, borderwidth=1)
        frame.grid(row=i, column=j, sticky='ew')
        label = Label(frame, borderwidth=1)
        label.grid()



frame = Frame(window, height=5, relief=RAISED, borderwidth=1)
frame.grid(column=4, row=0)
label = Label(frame, text='Диапозон', borderwidth=1, font='Times 12', width=5, height=1, background='silver',)
label.grid()

frame1 = Frame(window, height=5, relief=RAISED, borderwidth=1)
frame1.grid(row=0, column=5)
label1 = Label(frame1, text='Кол-во в сценарии', borderwidth=1, font='Times 12', width=5, height=1, background='silver')
label1.grid()


frame2 = Frame(window, height=5, relief=RAISED, borderwidth=1)
frame2.grid(row=0, column=6)
label2 = Label(frame2, text='Обнаружено', borderwidth=1, font='Times 12', width=5, height=1, background='silver')
label2.grid()



frame3 = Frame(window, height=5, relief=RAISED, borderwidth=1)
frame3.grid(row=0, column=7)
label3 = Label(frame3, text='Решение', borderwidth=1, font='Times 12', width=5, height=1, background='silver')
label3.grid()




window.mainloop()