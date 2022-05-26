from tkinter import Tk, Frame, Label, Button, IntVar, Checkbutton
from serial import Serial, PARITY_ODD, EIGHTBITS
from serial.tools.list_ports import comports
from time import time, sleep
from interface import Table


comports_status = {
    f'COM{num}': {'active': False, 'psi_mode': False, 'dafault_mode': True, 'serial_instance': None,
                  'warm_request': False, 'vector_status': False} for num in range(1, 17)
    }

ports_frames = {}
commands = {
    'check_request': bytearray([16, 57, 16, 3]),
    'binr_mode': '$PORZA,0,115200,3*7E\r\n'.encode('ascii'),
    'psi_mode': bytearray([16, 221, 1, 16, 3]),
    'default_set': bytearray([16, 221, 0, 16, 3]),
    'request_info_tracks': bytearray([16, 57, 1, 16, 3]),
    'stop_request': bytearray([16, 14, 16, 3]),
    'warm_restart': bytearray([16, 1, 0, 1, 33, 1, 0, 0, 16, 3]),
    'param_21': bytearray([16, 215, 21, 2, 16, 3]),
    'param_25': bytearray([16, 215, 25, 2, 16, 3]),
    'param_27': bytearray([16, 215, 27, 1, 16, 3]),
    'vector_request': bytearray([16, 39, 1, 16, 3]),
    'response_restart': bytearray([16, 67, 5, 0, 16, 3]),
    'response_restart_2': bytearray([16, 67, 5, 1, 16, 3]),
    'response_21': bytearray([16, 231, 21, 2, 16, 3]),
    'response_25': bytearray([16, 231, 25, 2, 16, 3]),
    'response_27': bytearray([16, 231, 27, 1, 16, 3])
}


sputnik_values = {

                        'gln_l1of': 2,
                        'gln_l1sf': 5,
                        'gln_l2of': 3,
                        'gln_l2sf': 6,
                        'gln_l1oc_p': 101,
                        'gln_l1oc_d': 100,
                        'gln_l1sc_p': 103,
                        'gln_l1sc_d': 102,
                        'gln_l2oc_p': 105,
                        'gln_l2oc_ksi': 104,
                        'gln_l2sc_p': 107,
                        'gln_l2sc_d': 106,
                        'gps_l1': 1,
                        'gps_l2_l': 50,
                        'gps_l2_m': 34,
                        'sdkm': 4,
                        'sdps': 4

}


class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wm_state('zoomed')
        self['background'] = 'white'

        container = Frame(self, background='white')
        container.pack(side='top', fill='both', expand=True)

        self.frames = {}

        for F in (StartPage, InfoTracks):
            frame = F(container, self, comports_status)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller, comports_status):
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
        StartPage.render()
        
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
        psi_button = ButtonFrame(0.3, 'Режим ПСИ', StartPage.psi_mode, container_buttons)
        cannals_button = ButtonFrame(0.5, 'Инф. о каналах', lambda: controller.show_frame(InfoTracks), container_buttons)
        vector_button = ButtonFrame(0.7, 'Вектор состояния', None, container_buttons)
        default_button = ButtonFrame(0.9, 'Настройки по умолчанию', StartPage.default_set, container_buttons)

    @staticmethod
    def check_con():
        instance_ports = []
        access_ports = [i.device for i in comports()]
        for comport in comports_status:
            serial_instance = comports_status[comport]['serial_instance']
            if serial_instance:
                serial_instance.close()
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
                comports_status[com.port]['serial_instance'] = com
                comports_status[com.port]['serial_instance'].warm_request = False
                comports_status[com.port]['serial_instance'].vector_status = False
                comports_status[com.port]['active'] = True

        StartPage.render()
        return instance_ports

    @staticmethod
    def render():
        render_options = {
                True: 'yellow',
                False: 'silver'
        }

        for com in comports_status:
            port_frame = ports_frames[com]
            port_frame.title_frame['background'] = render_options[comports_status[com]['active']]
            port_frame.title_label['background'] = render_options[comports_status[com]['active']]

            port_frame.psi_frame['background'] = render_options[comports_status[com]['psi_mode']]
            port_frame.psi_label['background'] = render_options[comports_status[com]['psi_mode']]

    @staticmethod
    def psi_mode():
        for comport in comports_status:
            port = comports_status[comport]
            if port['active']:
                serial_instance = port['serial_instance']
                serial_instance.write(commands['psi_mode'])
                port['psi_mode'] = True

        StartPage.render()

    @staticmethod
    def default_set():
        for comport in comports_status:
            port = comports_status[comport]
            if port['active']:
                serial_instance = port['serial_instance']
                serial_instance.write(commands['default_set'])
                port['psi_mode'] = False

        StartPage.render()


class InfoTracks(Frame):
    def __init__(self, parent, controller, comports_status):
        super().__init__(parent)
        

        self.request = bytearray([16, 57, 1, 16, 3])
        #self.check_request = bytearray([16, 57, 16, 3])
        self.stop_request = bytearray([16, 14, 16, 3])
        self.warm_restart = bytearray([16, 1, 0, 1, 33, 1, 0, 0, 16, 3])
        self.param_21 = bytearray([16, 215, 21, 2, 16, 3])
        self.param_25 = bytearray([16, 215, 25, 2, 16, 3])
        self.param_27 = bytearray([16, 215, 27, 1, 16, 3])
        self.vector_request = bytearray([16, 39, 1, 16, 3])
        self.response_restart = bytearray([16, 67, 5, 0, 16, 3])
        self.response_restart_2 = bytearray([16, 67, 5, 1, 16, 3]) 
        self.response_21 = bytearray([16, 231, 21, 2, 16, 3])
        self.response_25 = bytearray([16, 231, 25, 2, 16, 3])
        self.response_27 = bytearray([16, 231, 27, 1, 16, 3])
        #self.active_names = []
        #self.active_ports = []
        self.info_tracks_isrun = False
        self.info_vector_isrun = False


        self['background'] = 'white'

        NAME_W = int(self.winfo_screenwidth() / 17)
        TU_W = int(self.winfo_screenwidth() / 63.5)
        FACT_W = int(self.winfo_screenwidth() / 42.5)
        STATUS_W = int(self.winfo_screenwidth() / 44.5)
        HEAD_H = int(self.winfo_screenheight() / 33.3)
        BODY_H = int(self.winfo_screenheight() / 47)
        PAD_X = (int(self.winfo_screenwidth() / 150), 0)

        if TU_W <= 25:
            BODY_FONT = 'Times 7'
            HEAD_FONT = 8

        else:
            BODY_FONT = 'Times 8'
            HEAD_FONT = 10

        Table(self, col=0, row=0, port='COM1', pad_x=0, body_font=BODY_FONT, body_h=BODY_H, head_font=HEAD_FONT, name_w=NAME_W, tu_w=TU_W, fact_w=FACT_W, status_w=STATUS_W, head_h=HEAD_H)
        Table(self, col=4, row=0, port='COM2', pad_x=PAD_X, body_font=BODY_FONT, body_h=BODY_H, head_font=HEAD_FONT, name_w=NAME_W, tu_w=TU_W, fact_w=FACT_W, status_w=STATUS_W, head_h=HEAD_H)
        Table(self, col=8, row=0, port='COM3', pad_x=PAD_X, body_font=BODY_FONT, body_h=BODY_H, head_font=HEAD_FONT, name_w=NAME_W, tu_w=TU_W, fact_w=FACT_W, status_w=STATUS_W, head_h=HEAD_H)
        Table(self, col=12, row=0, port='COM4', pad_x=PAD_X, body_font=BODY_FONT, body_h=BODY_H, head_font=HEAD_FONT, name_w=NAME_W, tu_w=TU_W, fact_w=FACT_W, status_w=STATUS_W, head_h=HEAD_H)
        Table(self, col=16, row=0, port='COM5', pad_x=PAD_X, body_font=BODY_FONT, body_h=BODY_H, head_font=HEAD_FONT, name_w=NAME_W, tu_w=TU_W, fact_w=FACT_W, status_w=STATUS_W, head_h=HEAD_H)
        Table(self, col=20, row=0, port='COM6', pad_x=PAD_X, body_font=BODY_FONT, body_h=BODY_H, head_font=HEAD_FONT, name_w=NAME_W, tu_w=TU_W, fact_w=FACT_W, status_w=STATUS_W, head_h=HEAD_H)
        Table(self, col=24, row=0, port='COM7', pad_x=PAD_X, body_font=BODY_FONT, body_h=BODY_H, head_font=HEAD_FONT, name_w=NAME_W, tu_w=TU_W, fact_w=FACT_W, status_w=STATUS_W, head_h=HEAD_H)
        Table(self, col=28, row=0, port='COM8', pad_x=PAD_X, body_font=BODY_FONT, body_h=BODY_H, head_font=HEAD_FONT, name_w=NAME_W, tu_w=TU_W, fact_w=FACT_W, status_w=STATUS_W, head_h=HEAD_H)
        Table(self, col=0, row=20, port='COM9', body_font=BODY_FONT, body_h=BODY_H, head_font=HEAD_FONT, name_w=NAME_W, tu_w=TU_W, fact_w=FACT_W, status_w=STATUS_W, head_h=HEAD_H)
        Table(self, col=4, row=20, port='COM10', pad_x=PAD_X, body_font=BODY_FONT, body_h=BODY_H, head_font=HEAD_FONT, name_w=NAME_W, tu_w=TU_W, fact_w=FACT_W, status_w=STATUS_W, head_h=HEAD_H)
        Table(self, col=8, row=20, port='COM11', pad_x=PAD_X, body_font=BODY_FONT, body_h=BODY_H, head_font=HEAD_FONT, name_w=NAME_W, tu_w=TU_W, fact_w=FACT_W, status_w=STATUS_W, head_h=HEAD_H)
        Table(self, col=12, row=20, port='COM12', pad_x=PAD_X, body_font=BODY_FONT, body_h=BODY_H, head_font=HEAD_FONT, name_w=NAME_W, tu_w=TU_W, fact_w=FACT_W, status_w=STATUS_W, head_h=HEAD_H)
        Table(self, col=16, row=20, port='COM13', pad_x=PAD_X, body_font=BODY_FONT, body_h=BODY_H, head_font=HEAD_FONT, name_w=NAME_W, tu_w=TU_W, fact_w=FACT_W, status_w=STATUS_W, head_h=HEAD_H)
        Table(self, col=20, row=20, port='COM14', pad_x=PAD_X, body_font=BODY_FONT, body_h=BODY_H, head_font=HEAD_FONT, name_w=NAME_W, tu_w=TU_W, fact_w=FACT_W, status_w=STATUS_W, head_h=HEAD_H)
        Table(self, col=24, row=20, port='COM15', pad_x=PAD_X, body_font=BODY_FONT, body_h=BODY_H, head_font=HEAD_FONT, name_w=NAME_W, tu_w=TU_W, fact_w=FACT_W, status_w=STATUS_W, head_h=HEAD_H)
        Table(self, col=28, row=20, port='COM16', pad_x=PAD_X, body_font=BODY_FONT, body_h=BODY_H, head_font=HEAD_FONT, name_w=NAME_W, tu_w=TU_W, fact_w=FACT_W, status_w=STATUS_W, head_h=HEAD_H)

        buttonframe_width = self.winfo_screenwidth() / 2
        buttonframe_height = self.winfo_screenheight() / 14
        buttonframe = Frame(self, width=buttonframe_width, height=buttonframe_height, borderwidth=1, relief='solid')
        buttonframe.grid(columnspan=20, column=5)
        buttonframe.grid_propagate(False)

        frame_start = Frame(buttonframe, width=buttonframe_width / 7, height=buttonframe_height / 2, background='white')
        frame_start.place(relx=0.1, rely=0.5, anchor='center')
        frame_start.grid_propagate(False)
        self.start_button = Button(frame_start, text='Старт', font='Arial 8 bold', borderwidth=3, background='silver', width=10, height=1, fg='black', command=self.start)
        self.start_button.place(relx=0.5, rely=0.5, anchor='center')

        frame_stop = Frame(buttonframe, width=buttonframe_width / 8, height=buttonframe_height / 2, background='white', borderwidth=1, relief='solid')
        frame_stop.place(relx=0.3, rely=0.5, anchor='center')
        frame_stop.grid_propagate(False)
        self.stop_button = Button(frame_stop, text='Стоп', font='Arial 8 bold', borderwidth=3, background='silver', width=10, height=1, fg='black', command=self.stop)
        self.stop_button.place(relx=0.5, rely=0.5, anchor='center')

        frame_restart = Frame(buttonframe, width=buttonframe_width / 6, height=buttonframe_height / 2, background='white')
        frame_restart.place(relx=0.5, rely=0.5, anchor='center')
        frame_stop.grid_propagate(False)
        self.restart_button = Button(frame_restart, text='Холодный перезапуск', font='Arial 8 bold', borderwidth=3, background='silver', width=20, height=1, fg='black', command=self.restart)
        self.restart_button.place(relx=0.5, rely=0.5, anchor='center')

        self.oc_general = IntVar()
        self.oc_checkbok = Checkbutton(buttonframe, text='OC', font='Cambria 14 bold', variable=self.oc_general, command=self.set_oc, background='white', borderwidth=1)
        self.oc_checkbok.place(relx=0.7, rely=0.5, anchor='center')

        self.sc_general = IntVar()
        self.sc_checkbok = Checkbutton(buttonframe, text='SC', font='Cambria 14 bold', variable=self.sc_general, command=self.set_sc, background='white')
        self.sc_checkbok.place(relx=0.8, rely=0.5, anchor='center')

    @staticmethod
    def info_tracks_read(com):
        response = b''
        if not com.warm_request:
            if com.in_waiting >= 1924:
                response += com.read(com.in_waiting)
                if (response[-1] == 3) and (response[-2] == 16) and (response[-3] != 16):
                    if commands['response_21'] in response or commands['response_25'] in response or commands['response_27'] in response or commands['response_restart'] in response or commands['response_restart_2'] in response:
                        return (com, False)
                    com.reset_input_buffer()
                    return (com, response)
                else:
                    return (com, response)
            else:
                return (com, None)
        elif com.warm_request and ((time() - com.warm_restart_start) > 3):
            #sleep(3)
            com.warm_restart_start = True
            table_port = Table.table_ports_dict[com.port]
            table_port.start_time = time()
            com.write(commands['request_info_tracks'])
            com.warm_request = False
            table_port.restart_button['state'] = 'normal'
            return (com, None)
        else:
            return (com, None)

    @staticmethod
    def info_tracks_parse(com_response):
        print(com_response)
        com, response = com_response
        if response:
            code_list = []
            response_clear = response.replace(bytes.fromhex('10') + bytes.fromhex('10'), bytes.fromhex('10'))
            system_index = 2
            signal_index = 4
            for _ in range(96):
                if int(response_clear[signal_index:signal_index + 1].hex(), 16) > 0:
                    code_list.append(int(response_clear[system_index:system_index + 1].hex(), 16))
                system_index += 20
                signal_index += 20
            count_results = {sputnik: code_list.count(sputnik_values[sputnik]) for sputnik in sputnik_values}
            if count_results['gps_l2_l'] > count_results['gps_l2_m']:
                count_results['gps_l2_l_m'] = count_results['gps_l2_l']
            else:
                count_results['gps_l2_l_m'] = count_results['gps_l2_m']

            del count_results['gps_l2_l']
            del count_results['gps_l2_m']
            return (com, count_results)
        return (com, None)

    @staticmethod
    def info_tracks_rendering(com_results):
        com, results = com_results
        print(com.port)
        table_port = Table.table_ports_dict[com.port]
        if table_port.start_time == 'Restart':
            table_port.totaltime_label['text'] = 'Restart'
        else:
            current_time = int(time() - table_port.start_time)
            if current_time <= 36:
                table_port.totaltime_label['text'] = f'00:00:{ current_time }'

        if results:
            table_port.title_frame['background'] = 'yellow'
            table_port.title_label['background'] = 'yellow'
            for result in results:
                fact = getattr(table_port, result + '_fact')
                fact['text'] = results[result]
                frame = getattr(table_port, result + '_status_frame')
                if int(getattr(table_port, result + '_tu')['text']) - int(fact['text']) <= 2 and int(fact['text']) != 0:
                    frame['background'] = '#4fdb37'
                else:
                    frame['background'] = '#fc4838'

        if table_port.restart_status:
            com.write(commands['stop_request'])
            com.write(commands['warm_restart'])
            com.warm_restart_start = time()
            table_port.start_time = 'Restart'
            table_port.restart_status = False
            table_port.restart_button['state'] = 'disabled'
            com.warm_request = True
            table_port.var_oc.set(0)
            table_port.var_sc.set(0)
            table_port.oc_complite = False
            table_port.sc_complite = False
        #else:
        #    table_port.restart_button['state'] = 'normal'

        if table_port.var_oc.get() and not table_port.oc_complite:
            com.write(commands['param_21'])
            com.write(commands['param_25'])
            table_port.oc_complite = True

        if table_port.var_sc.get() and not table_port.sc_complite:
            com.write(commands['param_27'])
            table_port.sc_complite = True

    def restart(self):
        self.oc_general.set(0)
        self.sc_general.set(0)
        for table in Table.table_ports_dict:
            table_port = Table.table_ports_dict[table]
            table_port.var_oc.set(0)
            table_port.var_sc.set(0)
            table_port.oc_complite = False
            table_port.sc_complite = False

        for com in [comports_status[com]['serial_instance'] for com in comports_status if comports_status[com]['active']]:
            com.vector_status = False
            com.write(commands['warm_request'])

        sleep(3)

        for com in [comports_status[com]['serial_instance'] for com in comports_status if comports_status[com]['active']]:
            com.write(self.request)
        for table in Table.table_ports_dict:
            table_port = Table.table_ports_dict[table]
            table_port.start_time = time()

    def set_oc(self):
        for port in [comports_status[com]['serial_instance'] for com in comports_status if comports_status[com]['active']]:
            table_port = Table.table_ports_dict[port.port]
            table_port.var_oc.set(1)

    def set_sc(self):
        for port in [comports_status[com]['serial_instance'] for com in comports_status if comports_status[com]['active']]:
            table_port = Table.table_ports_dict[port.port]
            table_port.var_sc.set(1)

    def start(self):
        self.start_button['state'] = 'disabled'
        ready_ports = [comports_status[com]['serial_instance'] for com in comports_status if comports_status[com]['active']]

        [port.write(commands['request_info_tracks']) for port in ready_ports]
        print(Table.table_ports_dict)
        for table in Table.table_ports_dict:
            table_port = Table.table_ports_dict[table]
            table_port.start_time = time()

        def running():
            read_results = [InfoTracks.info_tracks_read(port) for port in ready_ports]
            parse_results = [InfoTracks.info_tracks_parse(port) for port in read_results]
            [InfoTracks.info_tracks_rendering(port) for port in parse_results]
            Tk.after(app, 100, running)

        running()

    def stop(self):
        pass


























if __name__ == '__main__':
    app = App()
    app.mainloop()
