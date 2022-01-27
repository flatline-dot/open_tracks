from tkinter import Tk, Frame, RAISED, Label, Button


class Interface(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x800')
        self.resizable(False, False)
        self.all_ports = ['COM' + str(i) for i in range(1, 17)]
        self.frame_ports = []


    def create_frame(self):
        num = 0
        for i in range(4):
            for j in range(4):
                self.frame = Frame(height=100, master=self, borderwidth=2, relief=RAISED)
                self.frame.grid(row=i, column=j)

                self.label = Label(master=self.frame, text=self.all_ports[num], width=35, height=4)
                num += 1
                self.frame_ports.append(self.label)
                self.label.pack()

    def create_button(self, text, command):
        self.button = Button(master=self, text=text, height=2, width=10, command=command)
        self.button.grid(column=1, row=4)


