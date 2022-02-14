import time
from tkinter import Tk, Frame, Label, Button

window = Tk()
window.wm_state('zoomed')
window.title('review')
window['background'] = 'white'

NAME_W = int(window.winfo_screenwidth() / 18.8)
TU_W = int(window.winfo_screenwidth() / 64)
FACT_W = int(window.winfo_screenwidth() / 53.3)
STATUS_W = int(window.winfo_screenwidth() / 40)
HEAD_H = int(window.winfo_screenheight() / 33.3)
BODY_H = int(window.winfo_screenheight() / 49)
PAD_X = (int(window.winfo_screenwidth() / 70), 0)


class Table():
    table_ports = []
    __slots__ = ('gln_l1of_tu', 'gln_l1of_fact', 'gln_l1of_status',
                 'gln_l1sf_tu', 'gln_l1sf_fact', 'gln_l1sf_status',
                 'gln_l2of_tu', 'gln_l2of_fact', 'gln_l2of_status',
                 'gln_l2sf_tu', 'gln_l2sf_fact', 'gln_l2sf_status',
                 'gln_l1oc_p_tu', 'gln_l1oc_p_fact', 'gln_l1oc_p_status',
                 'gln_l1oc_d_tu', 'gln_l1oc_d_fact', 'gln_l1oc_d_status',
                 'gln_l1sc_p_tu', 'gln_l1sc_p_fact', 'gln_l1sc_p_status',
                 'gln_l1sc_d_tu', 'gln_l1sc_d_fact', 'gln_l1sc_d_status',
                 'gln_l2oc_p_tu', 'gln_l2oc_p_fact', 'gln_l2oc_p_status',
                 'gln_l2oc_ksi_tu', 'gln_l2oc_ksi_fact', 'gln_l2oc_ksi_status',
                 'gln_l2sc_p_tu', 'gln_l2sc_p_fact', 'gln_l2sc_p_status',
                 'gln_l2sc_d_tu', 'gln_l2sc_d_fact', 'gln_l2sc_d_status',
                 'gps_l1_tu', 'gps_l1_fact', 'gps_l1_status',
                 'gps_l2_l_tu', 'gps_l2_l_fact', 'gps_l2_l_status',
                 'gps_l2_m_tu', 'gps_l2_m_fact', 'gps_l2_m_status',
                 'sdkm_tu', 'sdkm_fact', 'sdkm_status',
                 'sdps_tu', 'sdps_fact', 'sdps_status',
                 'title_label', 'title', 'number'
                 )

    def __init__(self, window, col=0, row=0, port=None, name_w=NAME_W, tu_w=TU_W, fact_w=FACT_W, status_w=STATUS_W, head_h=HEAD_H, pad_x=(0, 0), body_font='Times 8', body_h=BODY_H):
        self.number = port
        Table.table_ports.append(self)
        """Headers"""
        self.title = Frame(window, borderwidth=1, relief='solid', width=name_w + tu_w + fact_w + status_w, height=30, background='white')
        self.title.grid_propagate(False)
        self.title.grid(row=0 + row, column=col, columnspan=4, padx=pad_x)
        self.title_label = Label(self.title, text=port, font='Cambria 12 bold', background='white')
        self.title_label.place(relx=0.5, rely=0.5, anchor='center')

        frame_names = Frame(window, relief='raised', borderwidth=1, width=name_w, height=head_h, background='#bbd0f2')
        frame_names.grid(column=0 + col, row=1 + row, padx=pad_x)
        frame_names.grid_propagate(False)
        label_names = Label(frame_names, text='Диапозон', borderwidth=1, font='Times 10 bold', background='#bbd0f2')
        label_names.place(relx=0.5, rely=0.5, anchor='center')

        frame_const = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=head_h, background='#bbd0f2')
        frame_const.grid(row=1 + row, column=1 + col)
        frame_const.grid_propagate(False)
        label_const = Label(frame_const, text='ТУ', font='Times 10 bold', background='#bbd0f2')
        label_const.place(relx=0.5, rely=0.5, anchor='center')

        frame_count = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=head_h, background='#bbd0f2')
        frame_count.grid(row=1 + row, column=2 + col)
        frame_count.grid_propagate(False)
        frame_count = Label(frame_count, text='Факт.', font='Times 9 bold', background='#bbd0f2')
        frame_count.place(relx=0.5, rely=0.5, anchor='center')

        frame_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=head_h, background='#bbd0f2')
        frame_status.grid(row=1 + row, column=3 + col)
        frame_status.grid_propagate(False)
        label_status = Label(frame_status, text='Cтатус', font='Times 9 bold', background='#bbd0f2')
        label_status.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L1OF"""
        frame_l1of = Frame(window, relief='raised', borderwidth=1, width=name_w, height=body_h)
        frame_l1of.grid(row=2 + row, column=0 + col, padx=pad_x)
        frame_l1of.grid_propagate(False)
        label_l1of = Label(frame_l1of, text='ГЛН L1OF', font=body_font)
        label_l1of.grid()

        l1of_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h)
        l1of_tu.grid(row=2 + row, column=1+col)
        l1of_tu.grid_propagate(False)
        self.gln_l1of_tu = Label(l1of_tu, text='8', font=body_font)
        self.gln_l1of_tu.place(relx=0.5, rely=0.5, anchor='center')

        l1of_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h)
        l1of_fact.grid(row=2 + row, column=2 + col)
        l1of_fact.grid_propagate(False)
        self.gln_l1of_fact = Label(l1of_fact, text='0', font=body_font)
        self.gln_l1of_fact.place(relx=0.5, rely=0.5, anchor='center')

        l1of_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h)
        l1of_status.grid(row=2 + row, column=3 + col)
        l1of_status.grid_propagate(False)
        self.gln_l1of_status = Label(l1of_status, text='', font=body_font, width=8, height=5)
        self.gln_l1of_status.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L1SF"""
        l1sf_title = Frame(window, relief='raised', borderwidth=1, width=name_w, height=body_h)
        l1sf_title.grid(row=3 + row, column=0 + col, padx=pad_x)
        l1sf_title.grid_propagate(False)
        l1sf_label = Label(l1sf_title, text='ГЛН L1SF', font=body_font)
        l1sf_label.grid()

        l1sf_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h)
        l1sf_tu.grid(row=3 + row, column=1 + col)
        l1sf_tu.grid_propagate(False)
        self.gln_l1sf_tu = Label(l1sf_tu, text='8', font=body_font)
        self.gln_l1sf_tu.place(relx=0.5, rely=0.5, anchor='center')

        l1sf_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h)
        l1sf_fact.grid(row=3 + row, column=2 + col)
        l1sf_fact.grid_propagate(False)
        self.gln_l1sf_fact = Label(l1sf_fact, text='0', font=body_font)
        self.gln_l1sf_fact.place(relx=0.5, rely=0.5, anchor='center')

        l1sf_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h)
        l1sf_status.grid(row=3 + row, column=3 + col)
        l1sf_status.grid_propagate(False)
        self.gln_l1sf_status = Label(l1sf_status, text='', font=body_font, width=8, background='#1db546')
        self.gln_l1sf_status.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L2OF"""
        l2of_title = Frame(window, relief='raised', borderwidth=1, width=name_w, height=body_h)
        l2of_title.grid(row=4 + row, column=0 + col, padx=pad_x)
        l2of_title.grid_propagate(False)
        l2of_label = Label(l2of_title, text='ГЛН L2OF', font=body_font)
        l2of_label.grid()

        l2of_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h)
        l2of_tu.grid(row=4 + row, column=1 + col)
        l2of_tu.grid_propagate(False)
        self.gln_l2of_tu = Label(l2of_tu, text='8', font=body_font)
        self.gln_l2of_tu.place(relx=0.5, rely=0.5, anchor='center')

        l2of_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h)
        l2of_fact.grid(row=4 + row, column=2 + col)
        l2of_fact.grid_propagate(False)
        self.gln_l2of_fact = Label(l2of_fact, text='0', font=body_font)
        self.gln_l2of_fact.place(relx=0.5, rely=0.5, anchor='center')

        l2of_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h)
        l2of_status.grid(row=4 + row, column=3 + col)
        l2of_status.grid_propagate(False)
        self.gln_l2of_status = Label(l2of_status, text='', font=body_font, width=8)
        self.gln_l2of_status.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L2SF"""
        l2sf_title = Frame(window, relief='raised', borderwidth=1, width=name_w, height=body_h)
        l2sf_title.grid(row=5 + row, column=0 + col, padx=pad_x)
        l2sf_title.grid_propagate(False)
        l2sf_label = Label(l2sf_title, text='ГЛН L2SF', font=body_font)
        l2sf_label.grid()

        l2sf_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h)
        l2sf_tu.grid(row=5 + row, column=1 + col)
        l2sf_tu.grid_propagate(False)
        self.gln_l2sf_tu = Label(l2sf_tu, text='8', font=body_font)
        self.gln_l2sf_tu.place(relx=0.5, rely=0.5, anchor='center')

        l2sf_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h)
        l2sf_fact.grid(row=5 + row, column=2 + col)
        l2sf_fact.grid_propagate(False)
        self.gln_l2sf_fact = Label(l2sf_fact, text='0', font=body_font)
        self.gln_l2sf_fact.place(relx=0.5, rely=0.5, anchor='center')

        l2sf_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h)
        l2sf_status.grid(row=5 + row, column=3 + col)
        l2sf_status.grid_propagate(False)
        self.gln_l2sf_status = Label(l2sf_status, text='', font=body_font, width=8)
        self.gln_l2sf_status.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L1OC"""
        l1oc_mix = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.7), height=body_h * 2)
        l1oc_mix.grid(row=6 + row, column=0 + col, sticky='w', padx=pad_x)
        l1oc_mix.grid_propagate(False)
        l1oc_mix_label = Label(l1oc_mix, text='ГЛН L1OC', font=body_font)
        l1oc_mix_label.place(rely=0.5, anchor='w')

        """GLONASS L1OCp"""
        l1oc_p_title = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.3), height=body_h)
        l1oc_p_title.grid(row=6 + row, column=0 + col, sticky='en')
        l1oc_p_title.grid_propagate(False)
        gln_l1oc_p = Label(l1oc_p_title, text='p', font=body_font)
        gln_l1oc_p.place(relx=0.5, rely=0.5, anchor='center')

        l1oc_p_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h)
        l1oc_p_tu.grid(row=6 + row, column=1 + col, sticky='n')
        l1oc_p_tu.grid_propagate(False)
        self.gln_l1oc_p_tu = Label(l1oc_p_tu, text='8', font=body_font)
        self.gln_l1oc_p_tu.place(relx=0.5, rely=0.5, anchor='center')

        l1oc_p_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h)
        l1oc_p_fact.grid(row=6 + row, column=2 + col, sticky='n')
        l1oc_p_fact.grid_propagate(False)
        self.gln_l1oc_p_fact = Label(l1oc_p_fact, text='0', font=body_font)
        self.gln_l1oc_p_fact.place(relx=0.5, rely=0.5, anchor='center')

        l1oc_p_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h)
        l1oc_p_status.grid(row=6 + row, column=3 + col, sticky='n')
        l1oc_p_status.grid_propagate(False)
        self.gln_l1oc_p_status = Label(l1oc_p_status, text='', font=body_font, width=8)
        self.gln_l1oc_p_status.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L1OCd"""
        l1oc_d_title = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.3), height=body_h)
        l1oc_d_title.grid(row=6 + row, column=0 + col, sticky='es')
        l1oc_d_title.grid_propagate(False)
        gln_l1oc_d = Label(l1oc_d_title, text='d', font=body_font)
        gln_l1oc_d.place(relx=0.5, rely=0.5, anchor='center')

        l1oc_d_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h)
        l1oc_d_tu.grid(row=6 + row, column=1 + col, sticky='s')
        l1oc_d_tu.grid_propagate(False)
        self.gln_l1oc_d_tu = Label(l1oc_d_tu, text='8', font=body_font)
        self.gln_l1oc_d_tu.place(relx=0.5, rely=0.5, anchor='center')

        l1oc_d_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h)
        l1oc_d_fact.grid(row=6 + row, column=2 + col, sticky='s')
        l1oc_d_fact.grid_propagate(False)
        self.gln_l1oc_d_fact = Label(l1oc_d_fact, text='0', font=body_font)
        self.gln_l1oc_d_fact.place(relx=0.5, rely=0.5, anchor='center')

        l1oc_d_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h)
        l1oc_d_status.grid(row=6 + row, column=3 + col, sticky='s')
        l1oc_d_status.grid_propagate(False)
        self.gln_l1oc_d_status = Label(l1oc_d_status, text='', font=body_font, width=8)
        self.gln_l1oc_d_status.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L1SC"""
        l1sc_mix = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.7), height=int(body_h *2))
        l1sc_mix.grid(row=8 + row, column=0 + col, sticky='w', padx=pad_x)
        l1sc_mix.grid_propagate(False)
        l1sc_mix_label = Label(l1sc_mix, text='ГЛН L1SC', font=body_font)
        l1sc_mix_label.place(rely=0.5, anchor='w')

        """GLONASS L1SC_p"""
        l1sc_p_title = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.3), height=body_h)
        l1sc_p_title.grid(row=8 + row, column=0 + col, sticky='en')
        l1sc_p_title.grid_propagate(False)
        gln_l1sc_p = Label(l1sc_p_title, text='p', font=body_font)
        gln_l1sc_p.place(relx=0.5, rely=0.5, anchor='center')

        l1sc_p_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h)
        l1sc_p_tu.grid(row=8 + row, column=1 + col, sticky='n')
        l1sc_p_tu.grid_propagate(False)
        self.gln_l1sc_p_tu = Label(l1sc_p_tu, text='8', font=body_font)
        self.gln_l1sc_p_tu.place(relx=0.5, rely=0.5, anchor='center')

        l1sc_p_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h)
        l1sc_p_fact.grid(row=8 + row, column=2 + col, sticky='n')
        l1sc_p_fact.grid_propagate(False)
        self.gln_l1sc_p_fact = Label(l1sc_p_fact, text='0', font=body_font)
        self.gln_l1sc_p_fact.place(relx=0.5, rely=0.5, anchor='center')

        l1sc_p_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h)
        l1sc_p_status.grid(row=8 + row, column=3 + col, sticky='n')
        l1sc_p_status.grid_propagate(False)
        self.gln_l1sc_p_status = Label(l1sc_p_status, text='', font=body_font, width=8)
        self.gln_l1sc_p_status.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L1SC_d"""
        l1sc_d_title = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.3), height=body_h)
        l1sc_d_title.grid(row=8 + row, column=0 + col, sticky='es')
        l1sc_d_title.grid_propagate(False)
        gln_l1sc_d = Label(l1sc_d_title, text='d', font=body_font)
        gln_l1sc_d.place(relx=0.5, rely=0.5, anchor='center')

        l1sc_d_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h)
        l1sc_d_tu.grid(row=8 + row, column=1 + col, sticky='s')
        l1sc_d_tu.grid_propagate(False)
        self.gln_l1sc_d_tu = Label(l1sc_d_tu, text='8', font=body_font)
        self.gln_l1sc_d_tu.place(relx=0.5, rely=0.5, anchor='center')

        l1sc_d_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h)
        l1sc_d_fact.grid(row=8 + row, column=2 + col, sticky='s')
        l1sc_d_fact.grid_propagate(False)
        self.gln_l1sc_d_fact= Label(l1sc_d_fact, text='0', font=body_font)
        self.gln_l1sc_d_fact.place(relx=0.5, rely=0.5, anchor='center')

        l1sc_d_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h)
        l1sc_d_status.grid(row=8 + row, column=3 + col, sticky='s')
        l1sc_d_status.grid_propagate(False)
        self.gln_l1sc_d_status = Label(l1sc_d_status, text='', font=body_font, width=8)
        self.gln_l1sc_d_status.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L2OC"""
        l2oc_mix = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.7), height=int(body_h * 2))
        l2oc_mix.grid(row=10 + row, column=0 + col, sticky='w', padx=pad_x)
        l2oc_mix.grid_propagate(False)
        l2oc_mix_label = Label(l2oc_mix, text='ГЛН L2OC', font=body_font)
        l2oc_mix_label.place(rely=0.5, anchor='w')

        """GLONASS L2OC_p"""
        l2oc_p_title = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.3), height=body_h)
        l2oc_p_title.grid(row=10 + row, column=0 + col, sticky='en')
        l2oc_p_title.grid_propagate(False)
        l2oc_p_label = Label(l2oc_p_title, text='p', font=body_font)
        l2oc_p_label.place(relx=0.5, rely=0.5, anchor='center')

        l2oc_p_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h)
        l2oc_p_tu.grid(row=10 + row, column=1 + col, sticky='n')
        l2oc_p_tu.grid_propagate(False)
        self.gln_l2oc_p_tu = Label(l2oc_p_tu, text='8', font=body_font)
        self.gln_l2oc_p_tu.place(relx=0.5, rely=0.5, anchor='center')

        l2oc_p_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h)
        l2oc_p_fact.grid(row=10 + row, column=2 + col, sticky='n')
        l2oc_p_fact.grid_propagate(False)
        self.gln_l2oc_p_fact = Label(l2oc_p_fact, text='0', font=body_font)
        self.gln_l2oc_p_fact.place(relx=0.5, rely=0.5, anchor='center')

        l2oc_p_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h)
        l2oc_p_status.grid(row=10 + row, column=3 + col, sticky='n')
        l2oc_p_status.grid_propagate(False)
        self.gln_l2oc_p_status = Label(l2oc_p_status, text='', font=body_font, width=8)
        self.gln_l2oc_p_status.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L2OC_КСИ"""
        l2oc_ksi_title = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.3), height=body_h)
        l2oc_ksi_title.grid(row=10 + row, column=0 + col, sticky='es')
        l2oc_ksi_title.grid_propagate(False)
        l2oc_ksi_label = Label(l2oc_ksi_title, text='КСИ', font=body_font)
        l2oc_ksi_label.place(relx=0.5, rely=0.5, anchor='center')

        l2oc_ksi_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h)
        l2oc_ksi_tu.grid(row=10 + row, column=1 + col, sticky='s')
        l2oc_ksi_tu.grid_propagate(False)
        self.gln_l2oc_ksi_tu = Label(l2oc_ksi_tu, text='8', font=body_font)
        self.gln_l2oc_ksi_tu.place(relx=0.5, rely=0.5, anchor='center')

        l2oc_ksi_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h)
        l2oc_ksi_fact.grid(row=10 + row, column=2 + col, sticky='s')
        l2oc_ksi_fact.grid_propagate(False)
        self.gln_l2oc_ksi_fact = Label(l2oc_ksi_fact, text='0', font=body_font)
        self.gln_l2oc_ksi_fact.place(relx=0.5, rely=0.5, anchor='center')

        l2oc_ksi_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h)
        l2oc_ksi_status.grid(row=10 + row, column=3 + col, sticky='s')
        l2oc_ksi_status.grid_propagate(False)
        self.gln_l2oc_ksi_status = Label(l2oc_ksi_status, text='', font=body_font, width=8)
        self.gln_l2oc_ksi_status.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L2SC"""
        l2sc_mix = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.7), height=int(body_h * 2))
        l2sc_mix.grid(row=12 + row, column=0 + col, sticky='w', padx=pad_x)
        l2sc_mix.grid_propagate(False)
        l2sc_mix_label = Label(l2sc_mix, text='ГЛН L2OC', font=body_font)
        l2sc_mix_label.place(rely=0.5, anchor='w')

        """GLONASS L2SC_p"""
        l2sc_p_title = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.3), height=body_h)
        l2sc_p_title.grid(row=12 + row, column=0 + col, sticky='en')
        l2sc_p_title.grid_propagate(False)
        l2sc_p_label = Label(l2sc_p_title, text='p', font=body_font)
        l2sc_p_label.place(relx=0.5, rely=0.5, anchor='center')

        l2sc_p_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h)
        l2sc_p_tu.grid(row=12 + row, column=1 + col, sticky='n')
        l2sc_p_tu.grid_propagate(False)
        self.gln_l2sc_p_tu = Label(l2sc_p_tu, text='8', font=body_font)
        self.gln_l2sc_p_tu.place(relx=0.5, rely=0.5, anchor='center')

        l2sc_p_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h)
        l2sc_p_fact.grid(row=12 + row, column=2 + col, sticky='n')
        l2sc_p_fact.grid_propagate(False)
        self.gln_l2sc_p_fact = Label(l2sc_p_fact, text='0', font=body_font)
        self.gln_l2sc_p_fact.place(relx=0.5, rely=0.5, anchor='center')

        l2sc_p_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h)
        l2sc_p_status.grid(row=12 + row, column=3 + col, sticky='n')
        l2sc_p_status.grid_propagate(False)
        self.gln_l2sc_p_status = Label(l2sc_p_status, text='', font=body_font, width=8)
        self.gln_l2sc_p_status.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L2SC_d"""
        l2sc_d_title = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.3), height=body_h)
        l2sc_d_title.grid(row=12 + row, column=0 + col, sticky='es')
        l2sc_d_title.grid_propagate(False)
        l2sc_d_label = Label(l2sc_d_title, text='d', font=body_font)
        l2sc_d_label.place(relx=0.5, rely=0.5, anchor='center')

        l2sc_d_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h)
        l2sc_d_tu.grid(row=12 + row, column=1 + col, sticky='s')
        l2sc_d_tu.grid_propagate(False)
        self.gln_l2sc_d_tu = Label(l2sc_d_tu, text='8', font=body_font)
        self.gln_l2sc_d_tu.place(relx=0.5, rely=0.5, anchor='center')

        l2sc_d_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h)
        l2sc_d_fact.grid(row=12 + row, column=2 + col, sticky='s')
        l2sc_d_fact.grid_propagate(False)
        self.gln_l2sc_d_fact = Label(l2sc_d_fact, text='0', font=body_font)
        self.gln_l2sc_d_fact.place(relx=0.5, rely=0.5, anchor='center')

        l2sc_d_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h)
        l2sc_d_status.grid(row=12 + row, column=3 + col, sticky='s')
        l2sc_d_status.grid_propagate(False)
        self.gln_l2sc_d_status = Label(l2sc_d_status, text='', font=body_font, width=8)
        self.gln_l2sc_d_status.place(relx=0.5, rely=0.5, anchor='center')

        """GPS L1"""
        gps_l1_title = Frame(window, relief='raised', borderwidth=1, width=name_w, height=body_h)
        gps_l1_title.grid(row=13 + row, column=0 + col, padx=pad_x)
        gps_l1_title.grid_propagate(False)
        gps_l1_label = Label(gps_l1_title, text='GPS L1', font=body_font)
        gps_l1_label.grid()

        gps_l1_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h)
        gps_l1_tu.grid(row=13 + row, column=1 + col)
        gps_l1_tu.grid_propagate(False)
        self.gps_l1_tu = Label(gps_l1_tu, text='9', font=body_font)
        self.gps_l1_tu.place(relx=0.5, rely=0.5, anchor='center')

        gps_l1_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h)
        gps_l1_fact.grid(row=13 + row, column=2 + col)
        gps_l1_fact.grid_propagate(False)
        self.gps_l1_fact = Label(gps_l1_fact, text='0', font=body_font)
        self.gps_l1_fact.place(relx=0.5, rely=0.5, anchor='center')

        gps_l1_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h)
        gps_l1_status.grid(row=13 + row, column=3 + col)
        gps_l1_status.grid_propagate(False)
        self.gps_l1_status = Label(gps_l1_status, text='', font=body_font, width=8)
        self.gps_l1_status.place(relx=0.5, rely=0.5, anchor='center')

        """GPS L2"""
        gps_l2_mix = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.7), height=int(body_h * 2))
        gps_l2_mix.grid(row=14 + row, column=0 + col, sticky='w', padx=pad_x)
        gps_l2_mix.grid_propagate(False)
        gps_l2_mix_label = Label(gps_l2_mix, text='GPS L2', font=body_font)
        gps_l2_mix_label.place(rely=0.5, anchor='w')

        """GPS L2L"""
        gps_l2_l_title = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.3), height=body_h)
        gps_l2_l_title.grid(row=14 + row, column=0 + col, sticky='en')
        gps_l2_l_title.grid_propagate(False)
        gps_l2_l_label = Label(gps_l2_l_title, text='L', font=body_font)
        gps_l2_l_label.place(relx=0.5, rely=0.5, anchor='center')

        gps_l2_l_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h)
        gps_l2_l_tu.grid(row=14 + row, column=1 + col, sticky='n')
        gps_l2_l_tu.grid_propagate(False)
        self.gps_l2_l_tu = Label(gps_l2_l_tu, text='8', font=body_font)
        self.gps_l2_l_tu.place(relx=0.5, rely=0.5, anchor='center')

        gps_l2_l_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h)
        gps_l2_l_fact.grid(row=14 + row, column=2 + col, sticky='n')
        gps_l2_l_fact.grid_propagate(False)
        self.gps_l2_l_fact = Label(gps_l2_l_fact, text='0', font=body_font)
        self.gps_l2_l_fact.place(relx=0.5, rely=0.5, anchor='center')

        gps_l2_l_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h)
        gps_l2_l_status.grid(row=14 + row, column=3 + col, sticky='n')
        gps_l2_l_status.grid_propagate(False)
        self.gps_l2_l_status = Label(gps_l2_l_status, text='', font=body_font, width=8)
        self.gps_l2_l_status.place(relx=0.5, rely=0.5, anchor='center')

        """GPS L2M"""
        gps_l2_m_title = Frame(window, relief='raised', borderwidth=1, width=int(name_w * 0.3), height=body_h)
        gps_l2_m_title.grid(row=14 + row, column=0 + col, sticky='es')
        gps_l2_m_title.grid_propagate(False)
        gps_l2_m_label = Label(gps_l2_m_title, text='M', font=body_font)
        gps_l2_m_label.place(relx=0.5, rely=0.5, anchor='center')

        gps_l2_m_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h)
        gps_l2_m_tu.grid(row=14 + row, column=1 + col, sticky='s')
        gps_l2_m_tu.grid_propagate(False)
        self.gps_l2_m_tu = Label(gps_l2_m_tu, text='8', font=body_font)
        self.gps_l2_m_tu.place(relx=0.5, rely=0.5, anchor='center')

        gps_l2_m_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h)
        gps_l2_m_fact.grid(row=14 + row, column=2 + col, sticky='s')
        gps_l2_m_fact.grid_propagate(False)
        self.gps_l2_m_fact = Label(gps_l2_m_fact, text='0', font=body_font)
        self.gps_l2_m_fact.place(relx=0.5, rely=0.5, anchor='center')

        gps_l2_m_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h)
        gps_l2_m_status.grid(row=14 + row, column=3 + col, sticky='s')
        gps_l2_m_status.grid_propagate(False)
        self.gps_l2_m_status = Label(gps_l2_m_status, text='', font=body_font, width=8)
        self.gps_l2_m_status.place(relx=0.5, rely=0.5, anchor='center')

        """СДКМ"""
        sdkm_title = Frame(window, relief='raised', borderwidth=1, width=name_w, height=body_h)
        sdkm_title.grid(row=15 + row, column=0 + col, padx=pad_x)
        sdkm_title.grid_propagate(False)
        sdkm_label = Label(sdkm_title, text='СДКМ', font=body_font)
        sdkm_label.grid()

        sdkm_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h)
        sdkm_tu.grid(row=15 + row, column=1 + col)
        sdkm_tu.grid_propagate(False)
        self.sdkm_tu = Label(sdkm_tu, text='1', font=body_font)
        self.sdkm_tu.place(relx=0.5, rely=0.5, anchor='center')

        sdkm_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h)
        sdkm_fact.grid(row=15 + row, column=2 + col)
        sdkm_fact.grid_propagate(False)
        self.sdkm_fact = Label(sdkm_fact, text='0', font=body_font)
        self.sdkm_fact.place(relx=0.5, rely=0.5, anchor='center')

        sdkm_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h)
        sdkm_status.grid(row=15 + row, column=3 + col)
        sdkm_status.grid_propagate(False)
        self.sdkm_status = Label(sdkm_status, text='', font=body_font, width=8)
        self.sdkm_status.place(relx=0.5, rely=0.5, anchor='center')

        """ШДПС"""
        sdps_title = Frame(window, relief='raised', borderwidth=1, width=name_w, height=body_h)
        sdps_title.grid(row=16 + row, column=0 + col, padx=pad_x)
        sdps_title.grid_propagate(False)
        sdps_label = Label(sdps_title, text='ШДПС', font=body_font)
        sdps_label.grid()

        sdps_tu = Frame(window, relief='raised', borderwidth=1, width=tu_w, height=body_h)
        sdps_tu.grid(row=16 + row, column=1 + col)
        sdps_tu.grid_propagate(False)
        self.sdps_tu = Label(sdps_tu, text='1', font=body_font)
        self.sdps_tu.place(relx=0.5, rely=0.5, anchor='center')

        sdps_fact = Frame(window, relief='raised', borderwidth=1, width=fact_w, height=body_h)
        sdps_fact.grid(row=16 + row, column=2 + col)
        sdps_fact.grid_propagate(False)
        self.sdps_fact = Label(sdps_fact, text='0', font=body_font)
        self.sdps_fact.place(relx=0.5, rely=0.5, anchor='center')

        sdps_status = Frame(window, relief='raised', borderwidth=1, width=status_w, height=body_h)
        sdps_status.grid(row=16 + row, column=3 + col)
        sdps_status.grid_propagate(False)
        self.sdps_status = Label(sdps_status, text='', font=body_font, width=8)
        self.sdps_status.place(relx=0.5, rely=0.5, anchor='center')

        pas_frame = Frame(window, height=20)
        pas_frame.grid(row=17)
