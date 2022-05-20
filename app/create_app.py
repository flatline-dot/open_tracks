from tkinter import Tk, Frame, Label, Button
from serial import Serial, PARITY_ODD, EIGHTBITS
from serial.tools.list_ports import comports
from time import sleep


comports_status = {f'COM{num}': {'active': False, 'psi_mode': False, 'dafault_mode': True} for num in range(1, 17)}
ports_frames = {}
commands = {
    'check_request': bytearray([16, 57, 16, 3]),
    'binr_mode': '$PORZA,0,115200,3*7E\r\n'.encode('ascii'),
    'psi_mode': bytearray([10, 221, 1, 10, 3])
}


class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wm_state('zoomed')
        self['background'] = 'white'

        container = Frame(self, background='white')
        container.pack(side='top', fill='both', expand=True)

        self.frames = {}

        for F in (StartPage, ):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
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
            frame = PortFrame(title, master=container_ports)
            ports_frames[title] = frame
            frame.grid(row=0, column=high_row.index(title), padx=(0, 30), pady=(70, 50))

        for title in low_row:
            frame = PortFrame(title, master=container_ports)
            ports_frames[title] = frame
            frame.grid(row=1, column=low_row.index(title), padx=(0, 30), pady=(0, 50))

        button_frame_width = container_buttons['width'] / 1.4
        button_frame_height = container_buttons['height'] / 10
        StartPage.render_check_con()
        
        class ButtonFrame(Frame):
            def __init__(self, rely, text, command, container):
                super().__init__(container)
                self['width'] = button_frame_width
                self['height'] = button_frame_height
                self['borderwidth'] = 0
                self['relief'] = 'solid'
                self['background'] = 'white'
              
                self.place(relx=0.5, rely=rely, anchor='center')
                self.grid_propagate(False)

                button = Button(self, text=text, width=22, height=2, borderwidth=2, font='Times 8 bold', relief='groove', command=command)
                button.place(relx=0.5, rely=0.5, anchor='center')
                button.grid_propagate(False)

        check_button = ButtonFrame(0.1, 'Проверка соединения', StartPage.check_con, container_buttons)
        psi_button = ButtonFrame(0.3, 'Режим ПСИ', None, container_buttons)
        cannals_button = ButtonFrame(0.5, 'Инф. о каналах', None, container_buttons)
        vector_button = ButtonFrame(0.7, 'Вектор состояния', None, container_buttons)
        default_button = ButtonFrame(0.9, 'Настройки по умолчанию', None, container_buttons)

    @staticmethod
    def check_con():
        instance_ports = []
        access_ports = [i.device for i in comports()]
        print(access_ports)
        for port in access_ports:
            try:
                com = Serial(port=port)
                com.parity = PARITY_ODD
                com.baudrate = 115200
                com.bytesize = EIGHTBITS
                com.timeout = 1
                com.write(commands['check_request'])
                instance_ports.append(com)
            except Exception:
                print(f'{com}: Отказано в доступе.')

        sleep(1)
        for com in instance_ports.copy():
            if not com.in_waiting:
                instance_ports.remove(com)
                comports_status[com.port]['active'] = False
            else:
                com.reset_input_buffer()
                comports_status[com.port]['active'] = True

        StartPage.render()
        return instance_ports

    @staticmethod
    def render():
        render_options = {
                True: 'yellow',
                False: 'silver'
        }
        #for com in comports_status:
        #    if comports_status[com]['active']:
        #        port_frame = ports_frames[com]
        #        port_frame.title_frame['background'] = 'yellow'
        #        port_frame.title_label['background'] = 'yellow'
        #    else:
        #        port_frame = ports_frames[com]
        #        port_frame.title_frame['background'] = 'silver'
        #        port_frame.title_label['background'] = 'silver'
        #
        #for com in comports_status:
        #    if comports_status[com]['psi_mode']:
        #        port_frame = ports_frames[com]
        #        port_frame.psi_frame['background'] = 'yellow'
        #        port_frame.psi_label['background'] = 'yellow'
        #    else:
        #        port_frame = ports_frames[com]
        #        port_frame.psi_frame['background'] = 'silver'
        #        port_frame.psi_label['background'] = 'silver'
        #
        for com in comports_status:
            port_frame = ports_frames[com]
            port_frame.title_frame['background'] = render_options[comports_status[com]['active']]
            port_frame.title_label['background'] = render_options[comports_status[com]['active']]

            port_frame.psi_frame['background'] = render_options[comports_status[com]['psi_mode']]
            port_frame.psi_label['background'] = render_options[comports_status[com]['psi_mode']]






    @staticmethod
    def reder_con():
        pass


if __name__ == '__main__':
    app = App()
    app.mainloop()
