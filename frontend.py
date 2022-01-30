from tkinter import Tk, Frame, RAISED, Label, Button


class Interface(Tk):
    def __init__(self):
        super().__init__()
        self.wm_state('zoomed')
        self.all_ports = ('COM' + str(i) for i in range(1, 17))
        self.frame_ports = []

    def get_str(self, port_name, content):
        start_info = port_name + '\n\n'
        for i in content:
            start_info += i + ': ' + str(content[i]) + '\n'
        return start_info

    def create_frame(self):
        content = {
            'GPS': 0,
            'ГЛН': 0,
            'ГЛН L2': 0,
            'ГЛН L1SCd': 0,
            'ГЛН L2OCp': 0,
            'ГЛН L2КСИ': 0,
            'ГЛН L2SCd': 0,
            'GPS L2C-L': 0,
            'GPS L2C-M': 0
        }
        for i in range(4):
            for j in range(4):
                self.frame = Frame(height=100, master=self, borderwidth=2, relief=RAISED)
                self.frame.grid(row=i, column=j)

                self.label = Label(name=next(self.all_ports).lower(), master=self.frame, width=50, height=12, background='white', font='Times 11')
                self.label.content = content
                self.label['text'] = self.get_str(self.label._name.upper(), content)
                self.frame_ports.append(self.label)
                self.label.pack()

    def create_button(self, text, command):
        self.button = Button(master=self, text=text, height=2, width=20, command=command)
        self.button.grid(column=1, row=4)


