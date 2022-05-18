from tkinter import Tk, Frame, Label, Button


class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wm_state('zoomed')
        self['background'] = 'white'

        window_width = self.winfo_screenwidth()
        window_height = self.winfo_screenheight()

        container_buttons = Frame(self, width=window_width / 8, height=window_height / 2,
                                  borderwidth=2, relief='raised', background='white')

        container_buttons.grid()
        container_buttons.grid_propagate(False)

        container_ports = Frame(self, width=window_width, height=window_height / 2,
                                borderwidth=0, relief='solid', background='white')

        container_ports.grid(row=0, column=2, padx=(window_width / 24))
        container_ports.grid_propagate(False)

        class PortFrame(Frame):
            def __init__(self, title, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self['width'] = window_width / 12
                self['height'] = window_height / 16
                self.grid_propagate(False)

                self.title_frame = Frame(self, width=self['width'], height=self['height'] / 2, borderwidth=1, relief='solid')
                self.title_frame.grid(row=0, column=0)
                self.title_frame.grid_propagate(False)
                self.title_label = Label(self.title_frame, text=title, font='Times 11')
                self.title_label.place(relx=0.5, rely=0.5, anchor='center')

                self.psi_frame = Frame(self, width=self['width'], height=self['height'] / 2, borderwidth=1, relief='solid')
                self.psi_frame.grid(row=1, column=0)
                self.psi_frame.grid_propagate(False)
                self.psi_label = Label(self.psi_frame, text='Режим ПСИ', font='Times 11')
                self.psi_label.place(relx=0.5, rely=0.5, anchor='center')

        high_row = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8']
        low_row = ['COM9', 'COM10', 'COM11', 'COM12', 'COM13', 'COM14', 'COM15', 'COM16']

        for title in high_row:
            PortFrame(title, master=container_ports).grid(row=0, column=high_row.index(title), padx=(0, 30), pady=(70, 50))

        for title in low_row:
            PortFrame(title, master=container_ports).grid(row=1, column=low_row.index(title), padx=(0, 30), pady=(0, 50))

        button_frame_width = container_buttons['width'] / 1.4
        button_frame_height = container_buttons['height'] / 10

        class ButtonFrame(Frame):
            def __init__(self, rely, text, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self['width'] = button_frame_width
                self['height'] = button_frame_height
                self['borderwidth'] = 0
                self['relief'] = 'solid'
                self['background'] = 'white'
                
                self.place(relx=0.5, rely=rely, anchor='center')
                self.grid_propagate(False)

                button = Button(self, text=text, width=22, height=2, borderwidth=2, font='Times 8 bold', relief='groove')
                button.place(relx=0.5, rely=0.5, anchor='center')
                button.grid_propagate(False)

        check_buuton = ButtonFrame(0.1, 'Проверка соединения', container_buttons)
        psi_buuton = ButtonFrame(0.3, 'Режим ПСИ', container_buttons)
        cannals_buuton = ButtonFrame(0.5, 'Инф. о каналах', container_buttons)
        vector_buuton = ButtonFrame(0.7, 'Вектор состояния', container_buttons)
        default_buuton = ButtonFrame(0.9, 'Настройки по умолчанию', container_buttons)


app = App()
app.mainloop()
