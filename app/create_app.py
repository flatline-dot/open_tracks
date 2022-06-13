from tkinter import Tk, Frame, Label, Button, IntVar, Checkbutton
from serial import Serial, PARITY_ODD, EIGHTBITS
from serial.tools.list_ports import comports
from time import time, sleep
from interface import Table


comports_status = {
    'COM' + str(num): {'active': False, 'psi_mode': False, 'dafault_mode': True, 'serial_instance': None,
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
    'response_27': bytearray([16, 231, 27, 1, 16, 3]),
    'vision_sputnik': bytearray([16, 36, 1, 16, 3])
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
        self.info_tracks_isrun = False
        self.vector_status_isrun = False
        self.vision_sputnik_isrun = False

        container = Frame(self, background='white')
        container.pack(side='top', fill='both', expand=True)

        self.frames = {}

        for F in (StartPage, InfoTracks, VectorPage, VisionSputnik):
            frame = F(container, self, comports_status)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]

        if isinstance(frame, VectorPage):
            for table in [value for key, value in frame.vectortables.items()]:
                table.vector_label['background'] = 'white'
                table.vector_frame['background'] = 'white'

        if isinstance(frame, VisionSputnik):
            for table in [value for key, value in frame.visiontables.items()]:
                table.vision_label['background'] = 'white'
                table.vision_label['text'] = '0 GPS + 0 GLN + 0 SBAS'
                table.vision_frame['background'] = 'white'

        frame.tkraise()


class StartPage(Frame):
    perm_buttons = []

    def __init__(self, parent, controller, comports_status):
        super().__init__(parent)
        self['background'] = 'white'

        window_width = self.winfo_screenwidth()
        window_height = self.winfo_screenheight()

        container_buttons = Frame(self, width=window_width / 8, height=window_height / 2,
                                  borderwidth=6, relief='groove', background='white')

        container_buttons.grid()
        container_buttons.grid_propagate(False)

        container_ports = Frame(self, width=window_width, height=window_height / 2,
                                borderwidth=0, relief='solid', background='white')

        container_ports.grid(row=0, column=2, padx=(window_width / 24))
        container_ports.grid_propagate(False)

        class PortFrame(Frame):
            def __init__(self, title, container, *args, **kwargs):
                super().__init__(container)
                self['width'] = window_width / 12
                self['height'] = window_height / 16
                self['borderwidth'] = 0
                self['background'] = 'white'
                self.grid_propagate(False)

                self.title_frame = Frame(self, width=self['width'], height=self['height'] / 2, borderwidth=1, relief='solid')
                self.title_frame.grid(row=0, column=0)
                self.title_frame.grid_propagate(False)
                self.title_label = Label(self.title_frame, text=title, font='Times 14', background='white')
                self.title_label.place(relx=0.5, rely=0.5, anchor='center')

                self.psi_frame = Frame(self, width=self['width'], height=self['height'] / 2, borderwidth=1, relief='solid')
                self.psi_frame.grid(row=1, column=0)
                self.psi_frame.grid_propagate(False)
                self.psi_label = Label(self.psi_frame, text='Режим ПСИ', font='Times 11')
                self.psi_label.place(relx=0.5, rely=0.5, anchor='center')

        high_row = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8']
        low_row = ['COM9', 'COM10', 'COM11', 'COM12', 'COM13', 'COM14', 'COM15', 'COM16']

        for title in high_row:
            frame = PortFrame(title, container_ports)
            ports_frames[title] = frame
            frame.grid(row=0, column=high_row.index(title), padx=(0, 30), pady=(70, 50))

        for title in low_row:
            frame = PortFrame(title, container_ports)
            ports_frames[title] = frame
            frame.grid(row=1, column=low_row.index(title), padx=(0, 30), pady=(0, 50))

        button_frame_width = container_buttons['width'] / 1.4
        button_frame_height = container_buttons['height'] / 10
        StartPage.render()

        class ButtonFrame(Frame):
            def __init__(self, rely, text, command, container, state='disabled'):
                super().__init__(container)
                self['width'] = button_frame_width
                self['height'] = button_frame_height
                self['borderwidth'] = 0
                self['relief'] = 'solid'
                self['background'] = 'white'

                self.place(relx=0.5, rely=rely, anchor='center')
                self.grid_propagate(False)

                self.button = Button(self, text=text, width=22, height=2, borderwidth=3, font='Times 8 bold', relief='raised', command=command, state=state)
                self.button.place(relx=0.5, rely=0.5, anchor='center')
                self.button.grid_propagate(False)

        check_button = ButtonFrame(0.1, 'Установить соединение', StartPage.check_con, container_buttons, state='normal')
        psi_button = ButtonFrame(0.25, 'Режим ПСИ', StartPage.psi_mode, container_buttons)
        cannals_button = ButtonFrame(0.40, 'Инф. о каналах', lambda: controller.show_frame(InfoTracks), container_buttons)
        vector_button = ButtonFrame(0.55, 'Вектор состояния', lambda: controller.show_frame(VectorPage), container_buttons)
        vision_button = ButtonFrame(0.70, 'Видимые спутники', lambda: controller.show_frame(VisionSputnik), container_buttons)
        default_button = ButtonFrame(0.85, 'Настройки по умолчанию', StartPage.default_set, container_buttons)

        self.perm_buttons.append(psi_button)
        self.perm_buttons.append(cannals_button)
        self.perm_buttons.append(vector_button)
        self.perm_buttons.append(vision_button)
        self.perm_buttons.append(default_button)

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
                print(str(com) + ' : Отказано в доступе.')

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
                comports_status[com.port]['serial_instance'].vision_sputnik_is = False
                comports_status[com.port]['active'] = True

        StartPage.render()
        #if [comports_status[com]['serial_instance'] for com in comports_status if comports_status[com]['active']]:
        for frame in StartPage.perm_buttons:
            frame.button['state'] = 'normal'
        return instance_ports

    @staticmethod
    def render():
        render_options = {
                True: 'yellow',
                False: 'white'
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
        buttonframe_height = self.winfo_screenheight() / 12
        buttonframe = Frame(self, width=buttonframe_width, height=buttonframe_height, background='white')
        buttonframe.grid(columnspan=20, column=6)
        buttonframe.grid_propagate(False)

        frame_start = Frame(buttonframe, width=buttonframe_width / 7, height=buttonframe_height / 2, background='white')
        frame_start.place(relx=0.1, rely=0.7, anchor='center')
        frame_start.grid_propagate(False)
        self.start_button = Button(frame_start, text='Старт', font='Arial 8 bold', borderwidth=3, background='silver', width=10, height=2, fg='black', command=self.start, relief='raised')
        self.start_button.place(relx=0.5, rely=0.5, anchor='center')

        frame_stop = Frame(buttonframe, width=buttonframe_width / 8, height=buttonframe_height / 2, background='white')
        frame_stop.place(relx=0.3, rely=0.7, anchor='center')
        frame_stop.grid_propagate(False)
        self.stop_button = Button(frame_stop, text='Стоп', font='Arial 8 bold', borderwidth=3, background='silver', width=10, height=2, fg='black', command=self.stop, state='disabled', relief='raised')
        self.stop_button.place(relx=0.5, rely=0.5, anchor='center')

        frame_restart = Frame(buttonframe, width=buttonframe_width / 6, height=buttonframe_height / 2, background='white')
        frame_restart.place(relx=0.5, rely=0.7, anchor='center')
        frame_stop.grid_propagate(False)
        self.restart_button = Button(frame_restart, text='Холодный перезапуск', font='Arial 8 bold', borderwidth=3, background='silver', width=20, height=2, fg='black', command=self.restart, state='disabled', relief='raised')
        self.restart_button.place(relx=0.5, rely=0.5, anchor='center')

        self.oc_general = IntVar()
        self.oc_checkbok = Checkbutton(buttonframe, text='OC', font='Cambria 14 bold', variable=self.oc_general, command=self.set_oc, background='white', borderwidth=2, state='disabled')
        self.oc_checkbok.place(relx=0.7, rely=0.7, anchor='center')

        self.sc_general = IntVar()
        self.sc_checkbok = Checkbutton(buttonframe, text='SC', font='Cambria 14 bold', variable=self.sc_general, command=self.set_sc, background='white', state='disabled')
        self.sc_checkbok.place(relx=0.8, rely=0.7, anchor='center')

        backframe_width = self.winfo_screenwidth() / 15
        backframe_height = self.winfo_screenheight() / 14
        backframe = Frame(self, width=backframe_width, height=backframe_height, background='white')
        backframe.grid(columnspan=3, column=0, row=39)
        backframe.grid_propagate(False)
        self.back_button = Button(backframe, text='Назад', font='Arial 8 bold', borderwidth=3, background='silver', width=15, height=2, fg='black', command=lambda: controller.show_frame(StartPage), relief='raised')
        self.back_button.place(relx=0.5, rely=0.7, anchor='center')

    @staticmethod
    def info_tracks_read(com):
        response = b''
        if not com.warm_request:
            if com.in_waiting >= 1924:
                response += com.read(com.in_waiting)
                if (response[-1] == 3) and (response[-2] == 16) and (response[-3] != 16):
                    if commands['response_21'] in response or commands['response_25'] in response or commands['response_27'] in response or commands['response_restart'] in response or commands['response_restart_2'] in response:
                        print('OK')
                        return (com, False)
                    com.reset_input_buffer()
                    return (com, response)
                else:
                    return (com, response)
            else:
                return (com, None)
        elif com.warm_request and ((time() - com.warm_restart_start) > 3):
            # sleep(3)
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
        table_port = Table.table_ports_dict[com.port]
        if table_port.start_time == 'Restart':
            table_port.totaltime_label['text'] = 'Restart'
        else:
            current_time = int(time() - table_port.start_time)
            if current_time <= 36:
                table_port.totaltime_label['text'] = '00:00:' + str(current_time )

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
            com.write(commands['warm_restart'])

        sleep(3)

        for com in [comports_status[com]['serial_instance'] for com in comports_status if comports_status[com]['active']]:
            com.write(commands['request_info_tracks'])
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
        App.info_tracks_isrun = True
        self.back_button['state'] = 'disabled'
        self.start_button['state'] = 'disabled'
        self.restart_button['state'] = 'normal'
        self.stop_button['state'] = 'normal'
        self.oc_checkbok['state'] = 'normal'
        self.sc_checkbok['state'] = 'normal'
        ready_ports = [comports_status[com]['serial_instance'] for com in comports_status if comports_status[com]['active']]

        [port.write(commands['request_info_tracks']) for port in ready_ports]
        for table in Table.table_ports_dict:
            table_port = Table.table_ports_dict[table]
            table_port.start_time = time()

        def running():
            if App.info_tracks_isrun:
                read_results = [InfoTracks.info_tracks_read(port) for port in ready_ports]
                parse_results = [InfoTracks.info_tracks_parse(port) for port in read_results]
                [InfoTracks.info_tracks_rendering(port) for port in parse_results]
                Tk.after(app, 100, running)

        running()

    def stop(self):
        self.back_button['state'] = 'normal'
        self.start_button['state'] = 'normal'
        self.restart_button['state'] = 'disabled'
        self.stop_button['state'] = 'disabled'
        self.oc_checkbok['state'] = 'disabled'
        self.sc_checkbok['state'] = 'disabled'
        App.info_tracks_isrun = False
        ready_ports = [comports_status[com]['serial_instance'] for com in comports_status if comports_status[com]['active']]
        [port.write(commands['stop_request']) for port in ready_ports]
        sleep(0.5)
        [port.reset_input_buffer() for port in ready_ports]


class VectorPage(Frame):
    vectortables = {}

    def __init__(self, parent, controller, comports_status):
        super().__init__(parent)
        self['background'] = 'white'

        window_width = self.winfo_screenwidth()
        window_height = self.winfo_screenheight()

        container_ports = Frame(self, width=window_width, height=window_height / 2,
                                borderwidth=0, relief='solid', background='white')

        container_ports.grid(row=0, column=2, padx=(window_width / 10, 0))
        container_ports.grid_propagate(False)

        class VectorTable(Frame):
            def __init__(self, title, container, *args, **kwargs):
                super().__init__(container)
                self['width'] = window_width / 12
                self['height'] = window_height / 8
                self['borderwidth'] = 0
                self['background'] = 'white'
                self.grid_propagate(False)
                self.restart_status = False

                self.title_frame = Frame(self, width=self['width'], height=self['height'] / 4, borderwidth=1, relief='solid', background='white')
                self.title_frame.grid(row=0, column=0)
                self.title_frame.grid_propagate(False)
                self.title_label = Label(self.title_frame, text=title, font='Times 14', background='white')
                self.title_label.place(relx=0.5, rely=0.5, anchor='center')

                self.vector_frame = Frame(self, width=self['width'], height=self['height'] / 4, borderwidth=1, relief='solid', background='white')
                self.vector_frame.grid(row=1, column=0)
                self.vector_frame.grid_propagate(False)
                self.vector_label = Label(self.vector_frame, text='Вектор состояния', font='Times 11', background='white')
                self.vector_label.place(relx=0.5, rely=0.5, anchor='center')

                self.time_frame = Frame(self, width=self['width'], height=self['height'] / 4, borderwidth=1, relief='solid', background='white')
                self.time_frame.grid(row=2, column=0)
                self.time_frame.grid_propagate(False)
                self.totaltime_label = Label(self.time_frame, text='00:00:00', font='Times 12', background='white')
                self.totaltime_label.place(relx=0.5, rely=0.5, anchor='center')

                self.restart_frame = Frame(self, width=self['width'], height=self['height'] / 5, borderwidth=1, relief='solid', background='white')
                self.restart_frame.grid(row=3, column=0)
                self.restart_frame.grid_propagate(False)

                self.restart_button = Button(self.restart_frame, text='Restart', borderwidth=2, font='Cambria 8 bold', width=6, command=self.reverse_restart_flag, background='silver')
                self.restart_button.place(rely=0.5, relx=0.5, anchor='center')
                self.restart_button.grid_propagate(False)

                VectorPage.vectortables[title] = self

            def reverse_restart_flag(self):
                self.restart_status = True

        high_row = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8']
        low_row = ['COM9', 'COM10', 'COM11', 'COM12', 'COM13', 'COM14', 'COM15', 'COM16']

        for title in high_row:
            frame = VectorTable(title, container_ports)
            frame.grid(row=0, column=high_row.index(title), padx=(0, 30), pady=(70, 50))

        for title in low_row:
            frame = VectorTable(title, container_ports)
            frame.grid(row=1, column=low_row.index(title), padx=(0, 30), pady=(0, 50))

        buttonframe_width = window_width / 1.5
        buttonframe_height = window_height / 12
        buttonframe = Frame(self, width=buttonframe_width, height=buttonframe_height, background='white', borderwidth=1)
        buttonframe.grid(columnspan=20)
        buttonframe.grid_propagate(False)

        frame_start = Frame(buttonframe, width=buttonframe_width / 8, height=buttonframe_height / 2, background='white')
        frame_start.place(relx=0.3, rely=0.7, anchor='center')
        frame_start.grid_propagate(False)
        self.start_button = Button(frame_start, text='Старт', font='Arial 8 bold', borderwidth=3, background='silver', width=10, height=2, fg='black', command=self.start, relief='raised')
        self.start_button.place(relx=0.5, rely=0.5, anchor='center')

        frame_stop = Frame(buttonframe, width=buttonframe_width / 8, height=buttonframe_height / 2, background='white')
        frame_stop.place(relx=0.4, rely=0.7, anchor='center')
        frame_stop.grid_propagate(False)
        self.stop_button = Button(frame_stop, text='Стоп', font='Arial 8 bold', borderwidth=3, background='silver', width=10, height=2, fg='black', command=self.stop, state='disabled', relief='raised')
        self.stop_button.place(relx=0.5, rely=0.5, anchor='center')

        frame_restart = Frame(buttonframe, width=buttonframe_width / 8, height=buttonframe_height / 2, background='white')
        frame_restart.place(relx=0.53, rely=0.7, anchor='center')
        frame_restart.grid_propagate(False)
        self.restart_button = Button(frame_restart, text='Холодный перезапуск', font='Arial 8 bold', borderwidth=2, background='silver', width=20, height=2, fg='black', command=VectorPage.restart, state='disabled', relief='raised')
        self.restart_button.place(relx=0.5, rely=0.5, anchor='center')

        backframe = Frame(buttonframe, width=buttonframe_width / 8, height=buttonframe_height / 2, background='white')
        backframe.place(relx=0.1, rely=0.7, anchor='center')
        backframe.grid_propagate(False)
        self.back_button = Button(backframe, text='Назад', font='Arial 8 bold', borderwidth=3, background='silver', width=15, height=2, fg='black', command=lambda: controller.show_frame(StartPage), relief='raised')
        self.back_button.place(relx=0.5, rely=0.5, anchor='center')

    @staticmethod
    def vector_read(com):
        response = b''
        if not com.warm_request:
            if com.in_waiting >= 74:
                response += com.read(com.in_waiting)
                if (response[-1] == 3) and (response[-2] == 16) and (response[-3] != 16):
                    com.reset_input_buffer()
                    return (com, response)
                else:
                    return (com, None)
            else:
                return (com, None)
        elif com.warm_request and ((time() - com.warm_restart_start) > 3):
            #sleep(3)
            com.warm_restart_start = True
            table_port = VectorPage.vectortables[com.port]
            table_port.start_time = time()
            com.write(commands['vector_request'])
            com.warm_request = False
            table_port.restart_button['state'] = 'normal'
            return (com, None)
        else:
            return (com, None)

    @staticmethod
    def vector_parse(com_response):
        com, response = com_response
        vector_status = False
        if response:
            response_clear = response.replace(bytes.fromhex('10') + bytes.fromhex('10'), bytes.fromhex('10'))
            vector_status = int(response_clear[70:71].hex(), 16)
        else:
            return(com, False)
        if vector_status == 17 or vector_status == 25:
            return (com, True)
        else:
            return(com, False)

    def vector_rendering(self, com_results):
        com, result = com_results
        table_port = VectorPage.vectortables[com.port]
        if table_port.start_time == 'Restart':
            table_port.totaltime_label['text'] = 'Restart'
        else:
            current_time = int(time() - table_port.start_time)
            if current_time <= 36:
                table_port.totaltime_label['text'] = '00:00:' + str(current_time)

        if com.vector_status:
            return None
        else:
            if result:
                table_port.vector_frame['background'] = 'green'
                table_port.vector_label['background'] = 'green'
                com.vector_status = True
            else:
                table_port.vector_frame['background'] = 'red'
                table_port.vector_label['background'] = 'red'

        if table_port.restart_status:
            com.write(commands['stop_request'])
            com.write(commands['warm_restart'])
            com.warm_restart_start = time()
            table_port.start_time = 'Restart'
            table_port.restart_status = False
            table_port.restart_button['state'] = 'disabled'
            com.warm_request = True
            com.vector_status = False

    @staticmethod
    def restart():
        worker_ports = [comports_status[com]['serial_instance'] for com in comports_status if comports_status[com]['active']]
        for com in worker_ports:
            com.vector_status = False
            com.write(commands['warm_restart'])
        sleep(3)
        for com in worker_ports:
            com.write(commands['vector_request'])
        for table_port in VectorPage.vectortables:
            table_port = VectorPage.vectortables[table_port]
            table_port.start_time = time()

    def start(self):
        App.vector_status_isrun = True
        self.back_button['state'] = 'disabled'
        self.start_button['state'] = 'disabled'
        self.restart_button['state'] = 'normal'
        self.stop_button['state'] = 'normal'
        ready_ports = [comports_status[com]['serial_instance'] for com in comports_status if comports_status[com]['active']]

        [port.write(commands['vector_request']) for port in ready_ports]
        for table in VectorPage.vectortables:
            table_port = VectorPage.vectortables[table]
            table_port.start_time = time()

        def running():
            if App.vector_status_isrun:
                read_results = [VectorPage.vector_read(port) for port in ready_ports]
                parse_results = [VectorPage.vector_parse(port) for port in read_results]
                [self.vector_rendering(port) for port in parse_results]
                Tk.after(app, 100, running)

        running()

    def stop(self):
        self.back_button['state'] = 'normal'
        self.start_button['state'] = 'normal'
        self.restart_button['state'] = 'disabled'
        self.stop_button['state'] = 'disabled'
        App.vector_status_isrun = False
        ready_ports = [comports_status[com]['serial_instance'] for com in comports_status if comports_status[com]['active']]
        [port.write(commands['stop_request']) for port in ready_ports]
        sleep(0.5)
        [port.reset_input_buffer() for port in ready_ports]


class VisionSputnik(Frame):
    visiontables = {}

    def __init__(self, parent, controller, comports_status):
        super().__init__(parent)
        self['background'] = 'white'

        window_width = self.winfo_screenwidth()
        window_height = self.winfo_screenheight()

        container_ports = Frame(self, width=window_width, height=window_height / 2,
                                borderwidth=0, relief='solid', background='white')

        container_ports.grid(row=0, column=2, padx=(window_width / 10, 0))
        container_ports.grid_propagate(False)

        class VisionTable(Frame):
            def __init__(self, title, container, *args, **kwargs):
                super().__init__(container)
                self['width'] = window_width / 12
                self['height'] = window_height / 8
                self['borderwidth'] = 0
                self['background'] = 'white'
                self.grid_propagate(False)
                self.restart_status = False

                self.title_frame = Frame(self, width=self['width'], height=self['height'] / 4, borderwidth=1, relief='solid', background='white')
                self.title_frame.grid(row=0, column=0)
                self.title_frame.grid_propagate(False)
                self.title_label = Label(self.title_frame, text=title, font='Times 14', background='white')
                self.title_label.place(relx=0.5, rely=0.5, anchor='center')

                self.vision_frame = Frame(self, width=self['width'], height=self['height'] / 4, borderwidth=1, relief='solid', background='white')
                self.vision_frame.grid(row=1, column=0)
                self.vision_frame.grid_propagate(False)
                self.vision_label = Label(self.vision_frame, text='0 GPS + 0 GLN + 0 SBAS', font='Times 10', background='white')
                self.vision_label.place(relx=0.5, rely=0.5, anchor='center')

                self.restart_frame = Frame(self, width=self['width'], height=self['height'] / 5, borderwidth=1, relief='solid', background='white')
                self.restart_frame.grid(row=3, column=0)
                self.restart_frame.grid_propagate(False)

                self.restart_button = Button(self.restart_frame, text='Restart', borderwidth=2, font='Cambria 8 bold', width=6, command=self.reverse_restart_flag, background='silver')
                self.restart_button.place(rely=0.5, relx=0.5, anchor='center')
                self.restart_button.grid_propagate(False)

                VisionSputnik.visiontables[title] = self

            def reverse_restart_flag(self):
                self.restart_status = True

        high_row = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8']
        low_row = ['COM9', 'COM10', 'COM11', 'COM12', 'COM13', 'COM14', 'COM15', 'COM16']

        for title in high_row:
            frame = VisionTable(title, container_ports)
            frame.grid(row=0, column=high_row.index(title), padx=(0, 30), pady=(70, 50))

        for title in low_row:
            frame = VisionTable(title, container_ports)
            frame.grid(row=1, column=low_row.index(title), padx=(0, 30), pady=(0, 50))

        buttonframe_width = window_width / 1.5
        buttonframe_height = window_height / 12

        buttonframe = Frame(self, width=buttonframe_width, height=buttonframe_height, background='white', borderwidth=1)
        buttonframe.grid(columnspan=20)
        buttonframe.grid_propagate(False)

        frame_start = Frame(buttonframe, width=buttonframe_width / 8, height=buttonframe_height / 2, background='white')
        frame_start.place(relx=0.3, rely=0.7, anchor='center')
        frame_start.grid_propagate(False)
        self.start_button = Button(frame_start, text='Старт', font='Arial 8 bold', borderwidth=3, background='silver', width=10, height=2, fg='black', command=self.start, relief='raised')
        self.start_button.place(relx=0.5, rely=0.5, anchor='center')

        frame_stop = Frame(buttonframe, width=buttonframe_width / 8, height=buttonframe_height / 2, background='white')
        frame_stop.place(relx=0.4, rely=0.7, anchor='center')
        frame_stop.grid_propagate(False)
        self.stop_button = Button(frame_stop, text='Стоп', font='Arial 8 bold', borderwidth=3, background='silver', width=10, height=2, fg='black', command=self.stop, state='disabled', relief='raised')
        self.stop_button.place(relx=0.5, rely=0.5, anchor='center')

        frame_restart = Frame(buttonframe, width=buttonframe_width / 8, height=buttonframe_height / 2, background='white')
        frame_restart.place(relx=0.53, rely=0.7, anchor='center')
        frame_restart.grid_propagate(False)
        self.restart_button = Button(frame_restart, text='Холодный перезапуск', font='Arial 8 bold', borderwidth=3, background='silver', width=20, height=2, fg='black', command=VisionSputnik.restart, state='disabled', relief='raised')
        self.restart_button.place(relx=0.5, rely=0.5, anchor='center')

        backframe = Frame(buttonframe, width=buttonframe_width / 8, height=buttonframe_height / 2, background='white')
        backframe.place(relx=0.1, rely=0.7, anchor='center')
        backframe.grid_propagate(False)
        self.back_button = Button(backframe, text='Назад', font='Arial 8 bold', borderwidth=3, background='silver', width=15, height=2, fg='black', command=lambda: controller.show_frame(StartPage), relief='raised')
        self.back_button.place(relx=0.5, rely=0.5, anchor='center')

    @staticmethod
    def vision_read(com):
        response = b''
        if not com.warm_request:
            if com.in_waiting >= 4:
                response += com.read(com.in_waiting)
                if (response[0] == 16 and response[1] == 82) and (response[-1] == 3) and (response[-2] == 16) and (response[-3] != 16):
                    com.reset_input_buffer()
                    return (com, response)
                else:
                    com.reset_input_buffer()
                    return (com, None)
            else:
                return (com, None)
        elif com.warm_request and ((time() - com.warm_restart_start) > 3):
            #sleep(3)
            com.warm_restart_start = True
            table_port = VisionSputnik.visiontables[com.port]
            table_port.start_time = time()
            com.write(commands['vision_sputnik'])
            com.warm_request = False
            table_port.restart_button['state'] = 'normal'
            return (com, None)
        else:
            return (com, None)

    @staticmethod
    def vision_parse(com_response):
        com, response = com_response
        sputnik_code = {
            1: 'GPS',
            2: 'GLN',
            4: 'SBAS'
        }

        result = {
            'GPS': 0,
            'GLN': 0,
            'SBAS': 0
        }
        sputnik_count = 0
        if response:
            response_clear = response.replace(bytes.fromhex('10') + bytes.fromhex('10'), bytes.fromhex('10'))
            sputnik_count = int(len(response_clear[2:-2]) / 7)
            system_index = 2
            signal_index = 8

            for _ in range(sputnik_count):
                #if int(response_clear[signal_index:signal_index + 1].hex(), 16) > 0:
                system = int(response_clear[system_index:system_index + 1].hex(), 16)
                result[sputnik_code[system]] += 1
                system_index += 7
                signal_index += 7

            return (com, result)
        else:
            return(com, False)

    def vision_rendering(self, com_results):
        com, result = com_results
        table_port = VisionSputnik.visiontables[com.port]
        table_port.title_frame['background'] = 'yellow'
        table_port.title_label['background'] = 'yellow'

        table_port.vision_label['text'] = str(result['GPS']) + ' GPS' + '+' + str(result['GLN']) + ' GLN' + str(result['SBAS']) + ' SBAS'

        if table_port.restart_status:
            com.write(commands['stop_request'])
            com.write(commands['warm_restart'])
            com.warm_restart_start = time()
            table_port.restart_status = False
            table_port.restart_button['state'] = 'disabled'
            com.warm_request = True
            com.vision_sputnil_is = False

    @staticmethod
    def restart():
        worker_ports = [comports_status[com]['serial_instance'] for com in comports_status if comports_status[com]['active']]
        for com in worker_ports:
            com.vector_status = False
            com.write(commands['warm_restart'])
        sleep(3)
        for com in worker_ports:
            com.write(commands['vision_sputnik'])

    def start(self):
        App.vision_sputnik_isrun = True
        self.back_button['state'] = 'disabled'
        self.start_button['state'] = 'disabled'
        self.restart_button['state'] = 'normal'
        self.stop_button['state'] = 'normal'
        ready_ports = [comports_status[com]['serial_instance'] for com in comports_status if comports_status[com]['active']]
        [port.reset_input_buffer() for port in ready_ports]
        [port.write(commands['vision_sputnik']) for port in ready_ports]

        def running():
            if App.vision_sputnik_isrun:
                read_results = [VisionSputnik.vision_read(port) for port in ready_ports]
                parse_results = [VisionSputnik.vision_parse(port) for port in read_results]
                [self.vision_rendering(port) for port in parse_results]
                Tk.after(app, 100, running)

        running()

    def stop(self):
        self.back_button['state'] = 'normal'
        self.start_button['state'] = 'normal'
        self.restart_button['state'] = 'disabled'
        self.stop_button['state'] = 'disabled'
        App.vision_sputnik_isrun = False
        ready_ports = [comports_status[com]['serial_instance'] for com in comports_status if comports_status[com]['active']]
        [port.write(commands['stop_request']) for port in ready_ports]
        sleep(0.5)
        [port.reset_input_buffer() for port in ready_ports]


if __name__ == '__main__':
    app = App()
    app.mainloop()
