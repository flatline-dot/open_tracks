from interface import Table
from tkinter import Frame


class ParsingComports(Frame):
    def __init__(self, parent, controller, comports_status):
        super().__init__(parent)
        self.sputnik_values = {

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

        self.request = bytearray([16, 57, 1, 16, 3])
        self.check_request = bytearray([16, 57, 16, 3])
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

    def info_tracks_read(self, com):
        response = b''
        if not com.warm_request:
            if com.in_waiting >= 1924:
                response += com.read(com.in_waiting)
                if (response[-1] == 3) and (response[-2] == 16) and (response[-3] != 16):
                    if self.response_21 in response or self.response_25 in response or self.response_27 in response or self.response_restart in response or self.response_restart_2 in response:
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
            com.write(self.request)
            com.warm_request = False
            table_port.restart_button['state'] = 'normal'
            return (com, None)
        else:
            return (com, None)

    def info_tracks_parse(self, com_response):
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
            count_results = {sputnik: code_list.count(self.sputnik_values[sputnik]) for sputnik in self.sputnik_values}
            if count_results['gps_l2_l'] > count_results['gps_l2_m']:
                count_results['gps_l2_l_m'] = count_results['gps_l2_l']
            else:
                count_results['gps_l2_l_m'] = count_results['gps_l2_m']

            del count_results['gps_l2_l']
            del count_results['gps_l2_m']
            return (com, count_results)
        return (com, None)

    def info_tracks_rendering(self, com_results):
        com, results = com_results
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
            com.write(self.stop_request)
            com.write(self.warm_restart)
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
            com.write(self.param_21)
            com.write(self.param_25)
            table_port.oc_complite = True

        if table_port.var_sc.get() and not table_port.sc_complite:
            com.write(self.param_27)
            table_port.sc_complite = True

    def warm_restart_general(self):
        oc_general.set(0)
        sc_general.set(0)
        for table_port in Table.table_ports:
            table_port.var_oc.set(0)
            table_port.var_sc.set(0)
            table_port.oc_complite = False
            table_port.sc_complite = False

        for com in self.active_ports:
            com.vector_status = False
            com.write(self.warm_restart)

        sleep(3)

        for com in self.active_ports:
            com.write(self.request)
        for table_port in Table.table_ports:
            table_port.start_time = time()

    def set_oc(self):
        for port in self.active_ports:
            table_port = Table.table_ports_dict[port.port]
            table_port.var_oc.set(1)

    def set_sc(self):
        for port in self.active_ports:
            table_port = Table.table_ports_dict[port.port]
            table_port.var_sc.set(1)


#def info_tracks_ctrl():
#    comport.info_tracks_isrun = True
#    start()
#
#
#def start():
#    info_tracks_button['state'] = 'disabled'
#    ready_ports = comport.init_comports()
#
#    if comport.info_tracks_isrun:
#        [port.write(comport.request) for port in ready_ports]
#        for table_port in Table.table_ports:
#            table_port.start_time = time()
#        
#        def running():
#            if comport.info_tracks_isrun:
#                read_results = [comport.info_tracks_read(port) for port in ready_ports]
#                parse_results = [comport.info_tracks_parse(port) for port in read_results]
#                [comport.info_tracks_rendering(port) for port in parse_results]
#                Tk.after(app, 100, running)
#
#        running()
#
#
#def stop():
#    comport.info_tracks_isrun = False
#    comport.info_vector_isrun = False
#    check_conection['state'] = 'normal'
#    info_tracks_button['state'] = 'normal'
#    vector_button['state'] = 'normal'
#    comport.active_names.clear()
#    for port in comport.active_ports.copy():
#        port.write(comport.stop_request)
#        port.reset_input_buffer()
#        comport.active_ports.remove(port)
#        del port
#    print('Stop')


#if __name__ == '__main__':
#    
#    frame_check = Frame(window, width=120, height=45, background='white')
#    frame_check.grid(columnspan=4, column=10, row=40, pady=HEAD_H, sticky='we')
#    frame_check.grid_propagate(False)
#    check_conection = Button(frame_check, text='Проверка соединения', font='Arial 9 bold', borderwidth=3, background='#98d3ed', width=20, height=1, fg='black', command=comport.check_connections)
#    check_conection.place(relx=0.5, rely=0.5, anchor='center')
#
#    frame_start = Frame(window, width=80, height=45, background='white')
#    frame_start.grid(columnspan=3, column=16, row=40, pady=HEAD_H, sticky='w')
#    frame_start.grid_propagate(False)
#    info_tracks_button = Button(frame_start, text='Старт', font='Arial 9 bold', borderwidth=3, background='#98d3ed', width=10, height=1, fg='black', command=info_tracks_ctrl)
#    info_tracks_button.place(relx=0.5, rely=0.5, anchor='center')
#
#    frame_stop = Frame(window, width=80, height=45, background='white')
#    frame_stop.grid(columnspan=3, column=23, row=40, pady=HEAD_H, sticky='w')
#    frame_stop.grid_propagate(False)
#    stop_button = Button(frame_stop, text='Cтоп', font='Arial 9 bold', borderwidth=3, background='#98d3ed', state='normal', width=10, height=1, fg='black', command=stop)
#    stop_button.place(relx=0.5, rely=0.5, anchor='center')
#
#    frame_restart = Frame(window, width=120, height=45, background='white')
#    frame_restart.grid(columnspan=4, column=6, row=40, pady=HEAD_H, sticky='we')
#    frame_check.grid_propagate(False)
#    warm_restart_button = Button(frame_restart, text='Холодный перезапуск', font='Arial 9 bold', borderwidth=3, background='#98d3ed', width=20, height=1, fg='black', command=comport.warm_restart_general)
#    warm_restart_button.place(relx=0.5, rely=0.5, anchor='center')
#
#    #verctor_frame = Frame(window, width=120, height=45, background='white')
#    #verctor_frame.grid(columnspan=4, column=17, row=40, pady=HEAD_H, sticky='we')
#    #verctor_frame.grid_propagate(False)
#    #vector_button = Button(verctor_frame, text='Вектор состояния', font='Arial 9 bold', borderwidth=3, background='#98d3ed', width=20, height=1, fg='black', command=info_vector_ctrl)
#    #vector_button.place(relx=0.5, rely=0.5, anchor='center')
#
#    oc_general = IntVar()
#    oc_checkbok = Checkbutton(window, text='OC', font='Cambria 14 bold', variable=oc_general,command=comport.set_oc, background='white', borderwidth=1)
#    oc_checkbok.grid(column=4, row=40)
#
#    sc_general = IntVar()
#    sc_checkbok = Checkbutton(window, text='SC', font='Cambria 14 bold', variable=sc_general, command=comport.set_sc, background='white')
#    sc_checkbok.grid(column=3, columnspan=2, row=40, sticky='w')
#
#    timer_frame = Frame(window, width=120, height=45, background='white')
#    timer_frame.grid(columnspan=3, column=25, row=40)
#    timer_frame.grid_propagate(False)
#    timer = Label(timer_frame, text='', font='Arial 14', background='white')
#    timer.place(relx=0.5, rely=0.5, anchor='center')
#
#    error_frame = Frame(window, width=60, height=45, background='white')
#    error_frame.grid(columnspan=3, column=27, row=40, pady=HEAD_H, sticky='we')
#    error_frame.grid_propagate(False)
#    error_label = Label(error_frame, text='', font='Times 12 bold', background='white')
#    error_label.grid(sticky='we')
#
#    #window.mainloop()
