from tkinter import Tk, Frame, RAISED, Label, Button


class Interface(Tk):
    all_ports = ('COM' + str(i) for i in range(1, 17))
    frame_ports = []

    def __init__(self):
        super().__init__()
        self.wm_state('zoomed')
        self.title('channal_review')

    @staticmethod
    def get_str(port_name, content):
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
                frame = Frame(height=100, master=self, borderwidth=2, relief=RAISED)
                frame.grid(row=i, column=j)

                label = Label(name=next(self.all_ports).lower(), master=frame, width=50, height=12, background='white', font='Times 11')
                label.content = content
                label['text'] = self.get_str(label._name.upper(), content)
                self.frame_ports.append(label)
                label.pack()

    def create_button(self, check, run):
        self.button = Button(master=self, text='Проверка соединения', height=2, width=20, command=check)
        self.button.grid(pady=12, column=1, padx=10, sticky='E')
        self.button1 = Button(master=self, text='Тест', height=2, width=20, command=run)
        self.button1.grid(pady=12, row=4, column=2, sticky='W')


