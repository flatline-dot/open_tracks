from tkinter import *

all_ports = ['COM' + str(i) for i in range(1, 17)]
valid_ports = ['com1', 'com2', 'com3']
lst =[]


def listen_ports():
    a = {'GLN': 1, 'GPS': 1, 'SPAS': 1}
    res = ''
    for i in a:
        test = i + ': ' + str(a[i]) + '\n'
        res += test
    for i in lst:
        i['text'] = res


a = {'GLN': 2, 'GPS': 3, 'SPAS': 1}
res = ''
for i in a:
    test = i + ': ' + str(a[i]) + '\n'
    res += test


window = Tk()
window.geometry('1000x800')
window.resizable(False, False)
c = 0

for i in range(4):
    for j in range(4):
        frame = Frame(
            height='100',
            master=window,
            borderwidth=2,
            relief=RAISED
        )
        frame.grid(row=i, column=j)
        label = Label(name=str(all_ports[c].lower()), master=frame, text=res, width=35, height=4)
        c += 1
        lst.append(label)
        label.pack()


btn = Button(master=window, text='Проверка соединения', command=listen_ports, height=3)
btn.grid(column=1, row=4)
btn.grid()
window.mainloop()