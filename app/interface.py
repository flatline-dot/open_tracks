from tkinter import Frame, Label, Button, IntVar, Checkbutton


class Table():
    table_ports = []
    table_ports_dict = {}
    __slots__ = ('gln_l1of_tu', 'gln_l1of_fact', 'gln_l1of_status_frame',
                 'gln_l1sf_tu', 'gln_l1sf_fact', 'gln_l1sf_status_frame',
                 'gln_l2of_tu', 'gln_l2of_fact', 'gln_l2of_status_frame',
                 'gln_l2sf_tu', 'gln_l2sf_fact', 'gln_l2sf_status_frame',
                 'gln_l1oc_p_tu', 'gln_l1oc_p_fact', 'gln_l1oc_p_status_frame',
                 'gln_l1oc_d_tu', 'gln_l1oc_d_fact', 'gln_l1oc_d_status_frame',
                 'gln_l1sc_p_tu', 'gln_l1sc_p_fact', 'gln_l1sc_p_status_frame',
                 'gln_l1sc_d_tu', 'gln_l1sc_d_fact', 'gln_l1sc_d_status_frame',
                 'gln_l2oc_p_tu', 'gln_l2oc_p_fact', 'gln_l2oc_p_status_frame',
                 'gln_l2oc_ksi_tu', 'gln_l2oc_ksi_fact', 'gln_l2oc_ksi_status_frame',
                 'gln_l2sc_p_tu', 'gln_l2sc_p_fact', 'gln_l2sc_p_status_frame',
                 'gln_l2sc_d_tu', 'gln_l2sc_d_fact', 'gln_l2sc_d_status_frame',
                 'gps_l1_tu', 'gps_l1_fact', 'gps_l1_status_frame',
                 'gps_l2_l_m_tu', 'gps_l2_l_m_fact', 'gps_l2_l_m_status_frame',
                 'sdkm_tu', 'sdkm_fact', 'sdkm_status_frame',
                 'sdps_tu', 'sdps_fact', 'sdps_status_frame',
                 'title_label', 'title', 'number', 'restart_status', 'var_oc', 'var_sc',
                 'oc_complite', 'sc_complite', 'title_frame', 'restart_button', 'totaltime_frame',
                 'totaltime_label', 'start_time', 'vector_status_frame', 'vector_status_label'
                 )

    def __init__(self, window, col=0, row=0, port=None, name_w=0, tu_w=0, fact_w=0, status_w=0, head_h=0, pad_x=(0, 0), body_font=0, body_h=0, head_font=0):
        Table.table_ports.append(self)
        Table.table_ports_dict[port] = self
        self.number = port
        self.restart_status = False
        self.var_oc = IntVar()
        self.var_sc = IntVar()
        self.oc_complite = False
        self.sc_complite = False
        """Headers"""
        self.title = Frame(window, borderwidth=1, relief='solid', width=name_w + tu_w + fact_w + status_w, height=30, background='white')
        self.title.grid_propagate(False)
        self.title.grid(row=0 + row, column=col, columnspan=4, padx=pad_x, pady=(3, 0))

        self.title_frame = Frame(self.title, borderwidth=1, relief='raised', width=tu_w + status_w + 5, height=28, background='white')
        self.title_frame.grid_propagate(False)
        self.title_frame.grid()

        self.title_label = Label(self.title_frame, text=port, font='Cambria 11 bold', background='white')
        self.title_label.place(relx=0.5, rely=0.5, anchor='center')

        self.restart_button = Button(self.title, text='Restart', borderwidth=2, font='Cambria 8 bold', width=6, command=self.warm_restart, background='silver')
        self.restart_button.place(rely=0.5, relx=0.5, anchor='center')

        oc_checkbox = Checkbutton(self.title, text='OC', font='Cambria 10 bold',  variable=self.var_oc, background='white')
        oc_checkbox.place(relx=0.9, rely=0.5, anchor='center')

        sc_checkbox = Checkbutton(self.title, text='SC', font='Cambria 10 bold', variable=self.var_sc, background='white')
        sc_checkbox.place(relx=0.7, rely=0.5, anchor='center')

        frame_names = Frame(window, relief='raised', borderwidth=1, width=name_w, height=head_h - 7, background='#bbd0f2')
        frame_names.grid(column=0 + col, row=3 + row, padx=pad_x)
        frame_names.grid_propagate(False)
        label_names = Label(frame_names, text='Диапозон', borderwidth=1, font='Times ' + str(head_font) + ' bold', background='#bbd0f2')
        label_names.place(relx=0.5, rely=0.5, anchor='center')

        frame_const = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=head_h - 7, background='#bbd0f2')
        frame_const.grid(row=3 + row, column=1 + col)
        frame_const.grid_propagate(False)
        label_const = Label(frame_const, text='ТУ', font='Times ' + str(head_font) + ' bold', background='#bbd0f2')
        label_const.place(relx=0.45, rely=0.5, anchor='center')

        frame_count = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=head_h - 7, background='#bbd0f2')
        frame_count.grid(row=3 + row, column=2 + col)
        frame_count.grid_propagate(False)
        frame_count = Label(frame_count, text='Факт.', font='Times ' + str(head_font - 1) + ' bold', background='#bbd0f2')
        frame_count.place(relx=0.445, rely=0.5, anchor='center')

        frame_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=head_h - 7, background='#bbd0f2')
        frame_status.grid(row=3 + row, column=3 + col)
        frame_status.grid_propagate(False)
        label_status = Label(frame_status, text='Реш.', font='Times ' + str(head_font - 1) + ' bold', background='#bbd0f2')
        label_status.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L1OF"""
        frame_l1of = Frame(window, relief='raised', borderwidth=1, width=name_w, height=body_h, background='#f5fcff')
        frame_l1of.grid(row=4 + row, column=0 + col, padx=pad_x)
        frame_l1of.grid_propagate(False)
        label_l1of = Label(frame_l1of, text='ГЛН L1OF', font=body_font, background='#f5fcff')
        label_l1of.grid()

        l1of_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h, background='#f5fcff')
        l1of_tu.grid(row=4 + row, column=1+col)
        l1of_tu.grid_propagate(False)
        self.gln_l1of_tu = Label(l1of_tu, text='8', font=body_font, background='#f5fcff')
        self.gln_l1of_tu.place(relx=0.5, rely=0.5, anchor='center')

        l1of_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h, background='#f5fcff')
        l1of_fact.grid(row=4 + row, column=2 + col)
        l1of_fact.grid_propagate(False)
        self.gln_l1of_fact = Label(l1of_fact, text='0', font=body_font, background='#f5fcff')
        self.gln_l1of_fact.place(relx=0.5, rely=0.5, anchor='center')

        self.gln_l1of_status_frame = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h, background='#f5fcff')
        self.gln_l1of_status_frame.grid(row=4 + row, column=3 + col)
        self.gln_l1of_status_frame.grid_propagate(False)

        """GLONASS L1SF"""
        l1sf_title = Frame(window, relief='raised', borderwidth=1, width=name_w, height=body_h, background='#f5fcff')
        l1sf_title.grid(row=5 + row, column=0 + col, padx=pad_x)
        l1sf_title.grid_propagate(False)
        l1sf_label = Label(l1sf_title, text='ГЛН L1SF', font=body_font, background='#f5fcff')
        l1sf_label.grid()

        l1sf_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h, background='#f5fcff')
        l1sf_tu.grid(row=5 + row, column=1 + col)
        l1sf_tu.grid_propagate(False)
        self.gln_l1sf_tu = Label(l1sf_tu, text='8', font=body_font, background='#f5fcff')
        self.gln_l1sf_tu.place(relx=0.5, rely=0.5, anchor='center')

        l1sf_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h, background='#f5fcff')
        l1sf_fact.grid(row=5 + row, column=2 + col)
        l1sf_fact.grid_propagate(False)
        self.gln_l1sf_fact = Label(l1sf_fact, text='0', font=body_font, background='#f5fcff')
        self.gln_l1sf_fact.place(relx=0.5, rely=0.5, anchor='center')

        self.gln_l1sf_status_frame = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h, background='#f5fcff')
        self.gln_l1sf_status_frame.grid(row=5 + row, column=3 + col)
        self.gln_l1sf_status_frame.grid_propagate(False)

        """GLONASS L2OF"""
        l2of_title = Frame(window, relief='raised', borderwidth=1, width=name_w, height=body_h, background='#f5fcff')
        l2of_title.grid(row=6 + row, column=0 + col, padx=pad_x)
        l2of_title.grid_propagate(False)
        l2of_label = Label(l2of_title, text='ГЛН L2OF', font=body_font, background='#f5fcff')
        l2of_label.grid()

        l2of_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h, background='#f5fcff')
        l2of_tu.grid(row=6 + row, column=1 + col)
        l2of_tu.grid_propagate(False)
        self.gln_l2of_tu = Label(l2of_tu, text='8', font=body_font, background='#f5fcff')
        self.gln_l2of_tu.place(relx=0.5, rely=0.5, anchor='center')

        l2of_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h, background='#f5fcff')
        l2of_fact.grid(row=6 + row, column=2 + col)
        l2of_fact.grid_propagate(False)
        self.gln_l2of_fact = Label(l2of_fact, text='0', font=body_font, background='#f5fcff')
        self.gln_l2of_fact.place(relx=0.5, rely=0.5, anchor='center')

        self.gln_l2of_status_frame = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h, background='#f5fcff')
        self.gln_l2of_status_frame.grid(row=6 + row, column=3 + col)
        self.gln_l2of_status_frame.grid_propagate(False)

        """GLONASS L2SF"""
        l2sf_title = Frame(window, relief='raised', borderwidth=1, width=name_w, height=body_h, background='#f5fcff')
        l2sf_title.grid(row=7 + row, column=0 + col, padx=pad_x)
        l2sf_title.grid_propagate(False)
        l2sf_label = Label(l2sf_title, text='ГЛН L2SF', font=body_font, background='#f5fcff')
        l2sf_label.grid()

        l2sf_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h, background='#f5fcff')
        l2sf_tu.grid(row=7 + row, column=1 + col)
        l2sf_tu.grid_propagate(False)
        self.gln_l2sf_tu = Label(l2sf_tu, text='8', font=body_font, background='#f5fcff')
        self.gln_l2sf_tu.place(relx=0.5, rely=0.5, anchor='center')

        l2sf_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h, background='#f5fcff')
        l2sf_fact.grid(row=7 + row, column=2 + col)
        l2sf_fact.grid_propagate(False)
        self.gln_l2sf_fact = Label(l2sf_fact, text='0', font=body_font, background='#f5fcff')
        self.gln_l2sf_fact.place(relx=0.5, rely=0.5, anchor='center')

        self.gln_l2sf_status_frame = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h, background='#f5fcff')
        self.gln_l2sf_status_frame.grid(row=7 + row, column=3 + col)
        self.gln_l2sf_status_frame.grid_propagate(False)

        """GLONASS L1OC"""
        l1oc_mix = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.7), height=body_h * 2, background='#f5fcff')
        l1oc_mix.grid(row=8 + row, column=0 + col, sticky='w', padx=pad_x)
        l1oc_mix.grid_propagate(False)
        l1oc_mix_label = Label(l1oc_mix, text='ГЛН L1OC', font=body_font, background='#f5fcff')
        l1oc_mix_label.place(relx=0, rely=0.5, anchor='w')

        """GLONASS L1OCp"""
        l1oc_p_title = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.31), height=body_h, background='#f5fcff')
        l1oc_p_title.grid(row=8 + row, column=0 + col, sticky='en')
        l1oc_p_title.grid_propagate(False)
        gln_l1oc_p = Label(l1oc_p_title, text='p', font=body_font, background='#f5fcff')
        gln_l1oc_p.place(relx=0.5, rely=0.5, anchor='center')

        l1oc_p_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h, background='#f5fcff')
        l1oc_p_tu.grid(row=8 + row, column=1 + col, sticky='n')
        l1oc_p_tu.grid_propagate(False)
        self.gln_l1oc_p_tu = Label(l1oc_p_tu, text='8', font=body_font, background='#f5fcff')
        self.gln_l1oc_p_tu.place(relx=0.5, rely=0.5, anchor='center')

        l1oc_p_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h, background='#f5fcff')
        l1oc_p_fact.grid(row=8 + row, column=2 + col, sticky='n')
        l1oc_p_fact.grid_propagate(False)
        self.gln_l1oc_p_fact = Label(l1oc_p_fact, text='0', font=body_font, background='#f5fcff')
        self.gln_l1oc_p_fact.place(relx=0.5, rely=0.5, anchor='center')

        self.gln_l1oc_p_status_frame = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h, background='#f5fcff')
        self.gln_l1oc_p_status_frame.grid(row=8 + row, column=3 + col, sticky='n')
        self.gln_l1oc_p_status_frame.grid_propagate(False)

        """GLONASS L1OCd"""
        l1oc_d_title = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.31), height=body_h, background='#f5fcff')
        l1oc_d_title.grid(row=8 + row, column=0 + col, sticky='es')
        l1oc_d_title.grid_propagate(False)
        gln_l1oc_d = Label(l1oc_d_title, text='d', font=body_font, background='#f5fcff')
        gln_l1oc_d.place(relx=0.5, rely=0.5, anchor='center')

        l1oc_d_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h, background='#f5fcff')
        l1oc_d_tu.grid(row=8 + row, column=1 + col, sticky='s')
        l1oc_d_tu.grid_propagate(False)
        self.gln_l1oc_d_tu = Label(l1oc_d_tu, text='8', font=body_font, background='#f5fcff')
        self.gln_l1oc_d_tu.place(relx=0.5, rely=0.5, anchor='center')

        l1oc_d_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h, background='#f5fcff')
        l1oc_d_fact.grid(row=8 + row, column=2 + col, sticky='s')
        l1oc_d_fact.grid_propagate(False)
        self.gln_l1oc_d_fact = Label(l1oc_d_fact, text='0', font=body_font, background='#f5fcff')
        self.gln_l1oc_d_fact.place(relx=0.5, rely=0.5, anchor='center')

        self.gln_l1oc_d_status_frame = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h, background='#f5fcff')
        self.gln_l1oc_d_status_frame.grid(row=8 + row, column=3 + col, sticky='s')
        self.gln_l1oc_d_status_frame.grid_propagate(False)

        """GLONASS L1SC"""
        l1sc_mix = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.7), height=int(body_h * 2), background='#f5fcff')
        l1sc_mix.grid(row=10 + row, column=0 + col, sticky='w', padx=pad_x)
        l1sc_mix.grid_propagate(False)
        l1sc_mix_label = Label(l1sc_mix, text='ГЛН L1SC', font=body_font, background='#f5fcff')
        l1sc_mix_label.place(rely=0.5, anchor='w')

        """GLONASS L1SC_p"""
        l1sc_p_title = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.3), height=body_h, background='#f5fcff')
        l1sc_p_title.grid(row=10 + row, column=0 + col, sticky='en')
        l1sc_p_title.grid_propagate(False)
        gln_l1sc_p = Label(l1sc_p_title, text='p', font=body_font, background='#f5fcff')
        gln_l1sc_p.place(relx=0.5, rely=0.5, anchor='center')

        l1sc_p_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h, background='#f5fcff')
        l1sc_p_tu.grid(row=10 + row, column=1 + col, sticky='n')
        l1sc_p_tu.grid_propagate(False)
        self.gln_l1sc_p_tu = Label(l1sc_p_tu, text='8', font=body_font, background='#f5fcff')
        self.gln_l1sc_p_tu.place(relx=0.5, rely=0.5, anchor='center')

        l1sc_p_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h, background='#f5fcff')
        l1sc_p_fact.grid(row=10 + row, column=2 + col, sticky='n')
        l1sc_p_fact.grid_propagate(False)
        self.gln_l1sc_p_fact = Label(l1sc_p_fact, text='0', font=body_font, background='#f5fcff')
        self.gln_l1sc_p_fact.place(relx=0.5, rely=0.5, anchor='center')

        self.gln_l1sc_p_status_frame = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h, background='#f5fcff')
        self.gln_l1sc_p_status_frame.grid(row=10 + row, column=3 + col, sticky='n')
        self.gln_l1sc_p_status_frame.grid_propagate(False)

        """GLONASS L1SC_d"""
        l1sc_d_title = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.31), height=body_h, background='#f5fcff')
        l1sc_d_title.grid(row=10 + row, column=0 + col, sticky='es')
        l1sc_d_title.grid_propagate(False)
        gln_l1sc_d = Label(l1sc_d_title, text='d', font=body_font, background='#f5fcff')
        gln_l1sc_d.place(relx=0.5, rely=0.5, anchor='center')

        l1sc_d_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h, background='#f5fcff')
        l1sc_d_tu.grid(row=10 + row, column=1 + col, sticky='s')
        l1sc_d_tu.grid_propagate(False)
        self.gln_l1sc_d_tu = Label(l1sc_d_tu, text='8', font=body_font, background='#f5fcff')
        self.gln_l1sc_d_tu.place(relx=0.5, rely=0.5, anchor='center')

        l1sc_d_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h, background='#f5fcff')
        l1sc_d_fact.grid(row=10 + row, column=2 + col, sticky='s')
        l1sc_d_fact.grid_propagate(False)
        self.gln_l1sc_d_fact = Label(l1sc_d_fact, text='0', font=body_font, background='#f5fcff')
        self.gln_l1sc_d_fact.place(relx=0.5, rely=0.5, anchor='center')

        self.gln_l1sc_d_status_frame = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h, background='#f5fcff')
        self.gln_l1sc_d_status_frame.grid(row=10 + row, column=3 + col, sticky='s')
        self.gln_l1sc_d_status_frame.grid_propagate(False)

        """GLONASS L2OC"""
        l2oc_mix = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.7), height=int(body_h * 2), background='#f5fcff')
        l2oc_mix.grid(row=12 + row, column=0 + col, sticky='w', padx=pad_x)
        l2oc_mix.grid_propagate(False)
        l2oc_mix_label = Label(l2oc_mix, text='ГЛН L2OC', font=body_font, background='#f5fcff')
        l2oc_mix_label.place(rely=0.5, anchor='w')

        """GLONASS L2OC_p"""
        l2oc_p_title = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.31), height=body_h, background='#f5fcff')
        l2oc_p_title.grid(row=12 + row, column=0 + col, sticky='en')
        l2oc_p_title.grid_propagate(False)
        l2oc_p_label = Label(l2oc_p_title, text='p', font=body_font, background='#f5fcff')
        l2oc_p_label.place(relx=0.5, rely=0.5, anchor='center')

        l2oc_p_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h, background='#f5fcff')
        l2oc_p_tu.grid(row=12 + row, column=1 + col, sticky='n')
        l2oc_p_tu.grid_propagate(False)
        self.gln_l2oc_p_tu = Label(l2oc_p_tu, text='8', font=body_font, background='#f5fcff')
        self.gln_l2oc_p_tu.place(relx=0.5, rely=0.5, anchor='center')

        l2oc_p_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h, background='#f5fcff')
        l2oc_p_fact.grid(row=12 + row, column=2 + col, sticky='n')
        l2oc_p_fact.grid_propagate(False)
        self.gln_l2oc_p_fact = Label(l2oc_p_fact, text='0', font=body_font, background='#f5fcff')
        self.gln_l2oc_p_fact.place(relx=0.5, rely=0.5, anchor='center')

        self.gln_l2oc_p_status_frame = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h, background='#f5fcff')
        self.gln_l2oc_p_status_frame.grid(row=12 + row, column=3 + col, sticky='n')
        self.gln_l2oc_p_status_frame.grid_propagate(False)

        """GLONASS L2OC_КСИ"""
        l2oc_ksi_title = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.31), height=body_h, background='#f5fcff')
        l2oc_ksi_title.grid(row=12 + row, column=0 + col, sticky='es')
        l2oc_ksi_title.grid_propagate(False)
        l2oc_ksi_label = Label(l2oc_ksi_title, text='КСИ', font='Times 7', background='#f5fcff')
        l2oc_ksi_label.place(relx=0.403, rely=0.5, anchor='center')

        l2oc_ksi_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h, background='#f5fcff')
        l2oc_ksi_tu.grid(row=12 + row, column=1 + col, sticky='s')
        l2oc_ksi_tu.grid_propagate(False)
        self.gln_l2oc_ksi_tu = Label(l2oc_ksi_tu, text='8', font=body_font, background='#f5fcff')
        self.gln_l2oc_ksi_tu.place(relx=0.5, rely=0.5, anchor='center')

        l2oc_ksi_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h, background='#f5fcff')
        l2oc_ksi_fact.grid(row=12 + row, column=2 + col, sticky='s')
        l2oc_ksi_fact.grid_propagate(False)
        self.gln_l2oc_ksi_fact = Label(l2oc_ksi_fact, text='0', font=body_font, background='#f5fcff')
        self.gln_l2oc_ksi_fact.place(relx=0.5, rely=0.5, anchor='center')

        self.gln_l2oc_ksi_status_frame = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h, background='#f5fcff')
        self.gln_l2oc_ksi_status_frame.grid(row=12 + row, column=3 + col, sticky='s')
        self.gln_l2oc_ksi_status_frame.grid_propagate(False)

        """GLONASS L2SC"""
        l2sc_mix = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.7), height=int(body_h * 2), background='#f5fcff')
        l2sc_mix.grid(row=14 + row, column=0 + col, sticky='w', padx=pad_x)
        l2sc_mix.grid_propagate(False)
        l2sc_mix_label = Label(l2sc_mix, text='ГЛН L2SC', font=body_font, background='#f5fcff')
        l2sc_mix_label.place(rely=0.5, anchor='w')

        """GLONASS L2SC_p"""
        l2sc_p_title = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.31), height=body_h, background='#f5fcff')
        l2sc_p_title.grid(row=14 + row, column=0 + col, sticky='en')
        l2sc_p_title.grid_propagate(False)
        l2sc_p_label = Label(l2sc_p_title, text='p', font=body_font, background='#f5fcff')
        l2sc_p_label.place(relx=0.5, rely=0.5, anchor='center')

        l2sc_p_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h, background='#f5fcff')
        l2sc_p_tu.grid(row=14 + row, column=1 + col, sticky='n')
        l2sc_p_tu.grid_propagate(False)
        self.gln_l2sc_p_tu = Label(l2sc_p_tu, text='8', font=body_font, background='#f5fcff')
        self.gln_l2sc_p_tu.place(relx=0.5, rely=0.5, anchor='center')

        l2sc_p_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h, background='#f5fcff')
        l2sc_p_fact.grid(row=14 + row, column=2 + col, sticky='n')
        l2sc_p_fact.grid_propagate(False)
        self.gln_l2sc_p_fact = Label(l2sc_p_fact, text='0', font=body_font, background='#f5fcff')
        self.gln_l2sc_p_fact.place(relx=0.5, rely=0.5, anchor='center')

        self.gln_l2sc_p_status_frame = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h, background='#f5fcff')
        self.gln_l2sc_p_status_frame.grid(row=14 + row, column=3 + col, sticky='n')
        self.gln_l2sc_p_status_frame.grid_propagate(False)

        """GLONASS L2SC_d"""
        l2sc_d_title = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.31), height=body_h, background='#f5fcff')
        l2sc_d_title.grid(row=14 + row, column=0 + col, sticky='es')
        l2sc_d_title.grid_propagate(False)
        l2sc_d_label = Label(l2sc_d_title, text='d', font=body_font, background='#f5fcff')
        l2sc_d_label.place(relx=0.5, rely=0.5, anchor='center')

        l2sc_d_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h, background='#f5fcff')
        l2sc_d_tu.grid(row=14 + row, column=1 + col, sticky='s')
        l2sc_d_tu.grid_propagate(False)
        self.gln_l2sc_d_tu = Label(l2sc_d_tu, text='8', font=body_font, background='#f5fcff')
        self.gln_l2sc_d_tu.place(relx=0.5, rely=0.5, anchor='center')

        l2sc_d_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h, background='#f5fcff')
        l2sc_d_fact.grid(row=14 + row, column=2 + col, sticky='s')
        l2sc_d_fact.grid_propagate(False)
        self.gln_l2sc_d_fact = Label(l2sc_d_fact, text='0', font=body_font, background='#f5fcff')
        self.gln_l2sc_d_fact.place(relx=0.5, rely=0.5, anchor='center')

        self.gln_l2sc_d_status_frame = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h, background='#f5fcff')
        self.gln_l2sc_d_status_frame.grid(row=14 + row, column=3 + col, sticky='s')
        self.gln_l2sc_d_status_frame.grid_propagate(False)

        """GPS L1"""
        gps_l1_title = Frame(window, relief='raised', borderwidth=1, width=name_w, height=body_h, background='#f5fcff')
        gps_l1_title.grid(row=15 + row, column=0 + col, padx=pad_x)
        gps_l1_title.grid_propagate(False)
        gps_l1_label = Label(gps_l1_title, text='GPS L1', font=body_font, background='#f5fcff')
        gps_l1_label.grid()

        gps_l1_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h, background='#f5fcff')
        gps_l1_tu.grid(row=15 + row, column=1 + col)
        gps_l1_tu.grid_propagate(False)
        self.gps_l1_tu = Label(gps_l1_tu, text='9', font=body_font, background='#f5fcff')
        self.gps_l1_tu.place(relx=0.5, rely=0.5, anchor='center')

        gps_l1_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h, background='#f5fcff')
        gps_l1_fact.grid(row=15 + row, column=2 + col)
        gps_l1_fact.grid_propagate(False)
        self.gps_l1_fact = Label(gps_l1_fact, text='0', font=body_font, background='#f5fcff')
        self.gps_l1_fact.place(relx=0.5, rely=0.5, anchor='center')

        self.gps_l1_status_frame = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h, background='#f5fcff')
        self.gps_l1_status_frame.grid(row=15 + row, column=3 + col)
        self.gps_l1_status_frame.grid_propagate(False)

        """GPS L2L_M"""
        gps_l2_l_m_title = Frame(window, relief='raised', borderwidth=1, width=name_w, height=body_h, background='#f5fcff')
        gps_l2_l_m_title.grid(row=16 + row, column=0 + col, padx=pad_x)
        gps_l2_l_m_title.grid_propagate(False)
        gps_l2_l_label = Label(gps_l2_l_m_title, text='GPS L2 L/M', font=body_font, background='#f5fcff')
        gps_l2_l_label.grid()

        gps_l2_l_m_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h, background='#f5fcff')
        gps_l2_l_m_tu.grid(row=16 + row, column=1 + col, sticky='n')
        gps_l2_l_m_tu.grid_propagate(False)
        self.gps_l2_l_m_tu = Label(gps_l2_l_m_tu, text='8', font=body_font, background='#f5fcff')
        self.gps_l2_l_m_tu.place(relx=0.5, rely=0.5, anchor='center')

        gps_l2_l_m_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h, background='#f5fcff')
        gps_l2_l_m_fact.grid(row=16 + row, column=2 + col, sticky='n')
        gps_l2_l_m_fact.grid_propagate(False)
        self.gps_l2_l_m_fact = Label(gps_l2_l_m_fact, text='0', font=body_font, background='#f5fcff')
        self.gps_l2_l_m_fact.place(relx=0.5, rely=0.5, anchor='center')

        self.gps_l2_l_m_status_frame = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h, background='#f5fcff')
        self.gps_l2_l_m_status_frame.grid(row=16 + row, column=3 + col, sticky='n')
        self.gps_l2_l_m_status_frame.grid_propagate(False)

        """СДКМ"""
        sdkm_title = Frame(window, relief='raised', borderwidth=1, width=name_w, height=body_h, background='#f5fcff')
        sdkm_title.grid(row=17 + row, column=0 + col, padx=pad_x)
        sdkm_title.grid_propagate(False)
        sdkm_label = Label(sdkm_title, text='СДКМ', font=body_font, background='#f5fcff')
        sdkm_label.grid()

        sdkm_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h, background='#f5fcff')
        sdkm_tu.grid(row=17 + row, column=1 + col)
        sdkm_tu.grid_propagate(False)
        self.sdkm_tu = Label(sdkm_tu, text='1', font=body_font, background='#f5fcff')
        self.sdkm_tu.place(relx=0.5, rely=0.5, anchor='center')

        sdkm_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h, background='#f5fcff')
        sdkm_fact.grid(row=17 + row, column=2 + col)
        sdkm_fact.grid_propagate(False)
        self.sdkm_fact = Label(sdkm_fact, text='0', font=body_font, background='#f5fcff')
        self.sdkm_fact.place(relx=0.5, rely=0.5, anchor='center')

        self.sdkm_status_frame = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h, background='#f5fcff')
        self.sdkm_status_frame.grid(row=17 + row, column=3 + col)
        self.sdkm_status_frame.grid_propagate(False)

        """ШДПС"""
        sdps_title = Frame(window, relief='raised', borderwidth=1, width=name_w, height=body_h, background='#f5fcff')
        sdps_title.grid(row=18 + row, column=0 + col, padx=pad_x)
        sdps_title.grid_propagate(False)
        sdps_label = Label(sdps_title, text='ШДПС', font=body_font, background='#f5fcff')
        sdps_label.grid()

        sdps_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h, background='#f5fcff')
        sdps_tu.grid(row=18 + row, column=1 + col)
        sdps_tu.grid_propagate(False)
        self.sdps_tu = Label(sdps_tu, text='1', font=body_font, background='#f5fcff')
        self.sdps_tu.place(relx=0.5, rely=0.5, anchor='center')

        sdps_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h, background='#f5fcff')
        sdps_fact.grid(row=18 + row, column=2 + col)
        sdps_fact.grid_propagate(False)
        self.sdps_fact = Label(sdps_fact, text='0', font=body_font, background='#f5fcff')
        self.sdps_fact.place(relx=0.5, rely=0.5, anchor='center')

        self.sdps_status_frame = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h, background='#f5fcff')
        self.sdps_status_frame.grid(row=18 + row, column=3 + col)
        self.sdps_status_frame.grid_propagate(False)

        pas_frame = Frame(window, height=10)
        pas_frame.grid(row=19)

        self.totaltime_frame = Frame(window, borderwidth=1, relief='raised', width=name_w + tu_w + fact_w + status_w, height=23, background='white')
        self.totaltime_frame.grid_propagate(False)
        self.totaltime_frame.grid(row=1 + row, column=col, columnspan=4, padx=pad_x)

        self.totaltime_label = Label(self.totaltime_frame, text='00:00:00', font=body_font, background='#f5fcff')
        self.totaltime_label.place(relx=0.5, rely=0.5, anchor='center')

    def warm_restart(self):
        self.restart_status = True
