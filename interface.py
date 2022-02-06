from tkinter import *

window = Tk()
window.wm_state('zoomed')
window.title('review')


class Headers():
    def __init__(self, window, col, row, number):
        self.number = number
        self.col_width_0 = int(window.winfo_screenwidth() * 0.0087)
        self.col_width_1 = int(window.winfo_screenwidth() * 0.0022)
        self.col_width_2 = int(window.winfo_screenwidth() * 0.003)
        self.col_width_3 = int(window.winfo_screenwidth() * 0.0037)
        self.row_height = int(window.winfo_screenheight() * 0.002)
        self.headers_font_size = int(window.winfo_screenwidth() * 0.0068)
        self.title_font_size = int(window.winfo_screenwidth() * 0.009)
        self.body_font_size = int(window.winfo_screenwidth() * 0.00625)

        """Headers"""
        self.title = Frame(window, borderwidth=1, relief=RAISED)
        self.title.grid(row=0 + row, column=col, columnspan=4, sticky='ew')
        self.title_label = Label(self.title, text='COM' + number, borderwidth=0, font=f'Arial {self.title_font_size}', anchor='center')
        self.title_label.grid()

        self.frame_names = Frame(window, relief=RAISED, borderwidth=1, highlightthickness=0, highlightbackground='silver', highlightcolor='silver', background='silver')
        self.frame_names.grid(column=0 + col, row=1 + row, sticky='ewns')
        self.label_names = Label(self.frame_names, text='Диапозон', borderwidth=1, font=f'Times {self.headers_font_size}', width=self.col_width_0, height=self.row_height, background='silver', highlightthickness=0, highlightbackground='red')
        self.label_names.grid()

        self.frame_const = Frame(window, relief=RAISED, borderwidth=1, highlightthickness=0, highlightbackground='silver')
        self.frame_const.grid(row=1 + row, column=1 + col,)
        self.label_const = Label(self.frame_const, text='ТУ', borderwidth=1, font=f'Times {self.headers_font_size}', width=self.col_width_1, height=self.row_height, background='silver')
        self.label_const.grid()

        self.frame_count = Frame(window, relief=RAISED, borderwidth=1, highlightthickness=0, highlightbackground='silver')
        self.frame_count.grid(row=1 + row, column=2 + col)
        self.frame_count = Label(self.frame_count, text='Факт.', borderwidth=1, font=f'Times {self.headers_font_size}', width=self.col_width_2, height=self.row_height, background='silver')
        self.frame_count.grid()

        self.frame_status = Frame(window, relief=RAISED, borderwidth=1, highlightthickness=0, highlightbackground='silver')
        self.frame_status.grid(row=1 + row, column=3 + col)
        self.label_status = Label(self.frame_status, text='Cтатус', borderwidth=1, font=f'Times {self.headers_font_size}', width=self.col_width_3, height=self.row_height, background='silver')
        self.label_status.grid()

        """GLONASS L1OF"""
        self.gln_l1of = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1of.grid(row=2 + row, column=0 + col)
        self.gln_l1of_label = Label(self.gln_l1of, text='ГЛН L1OF', borderwidth=1, width=self.col_width_0, font=f'Times {self.body_font_size}', anchor='w')
        self.gln_l1of_label.grid()

        self.gln_l1of_tu = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1of_tu.grid(row=2 + row, column=1+col)
        self.gln_l1of_tu_label = Label(self.gln_l1of_tu, text='8', borderwidth=1, width=self.col_width_1, font=f'Times {self.body_font_size}')
        self.gln_l1of_tu_label.value = 8
        self.gln_l1of_tu_label.grid()

        self.gln_l1of_fact = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1of_fact.grid(row=2 + row, column=2 + col)
        self.gln_l1of_fact_label = Label(self.gln_l1of_fact, text='', borderwidth=1, width=self.col_width_2, font=f'Times {self.body_font_size}')
        self.gln_l1of_fact_label.value = 0
        self.gln_l1of_fact_label.grid()
        self.gln_l1of_status = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1of_status.grid(row=2 + row, column=3 + col)
        self.gln_l1of_status_label = Label(self.gln_l1of_status, text='', borderwidth=1, width=self.col_width_3, font=f'Times {self.body_font_size}')
        self.gln_l1of_status_label.value = False
        self.gln_l1of_status_label.grid()

        """GLONASS L1SF"""
        self.gln_l1sf = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1sf.grid(row=3 + row, column=0 + col)
        self.gln_l1sf_label = Label(self.gln_l1sf, text='ГЛН L1SF', borderwidth=1, width=self.col_width_0, font=f'Times {self.body_font_size}', anchor='w')
        self.gln_l1sf_label.grid()

        self.gln_l1sf_tu = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1sf_tu.grid(row=3 + row, column=1 + col)
        self.gln_l1sf_tu_label = Label(self.gln_l1sf_tu, text='8', borderwidth=1, width=self.col_width_1, font=f'Times {self.body_font_size}')
        self.gln_l1sf_tu_label.value = 8
        self.gln_l1sf_tu_label.grid()

        self.gln_l1sf_fact = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1sf_fact.grid(row=3 + row, column=2 + col)
        self.gln_l1sf_fact_label = Label(self.gln_l1sf_fact, text='', borderwidth=1, width=self.col_width_2, font=f'Times {self.body_font_size}')
        self.gln_l1sf_fact_label.value = 0
        self.gln_l1sf_fact_label.grid()

        self.gln_l1sf_status = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1sf_status.grid(row=3 + row, column=3 + col)
        self.gln_l1sf_status_label = Label(self.gln_l1sf_status, text='', borderwidth=1, width=self.col_width_3, font=f'Times {self.body_font_size}')
        self.gln_l1sf_status_label.value = False
        self.gln_l1sf_status_label.grid()

        """GLONASS L2OF"""
        self.gln_l2of = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2of.grid(row=4 + row, column=0 + col)
        self.gln_l2of_label = Label(self.gln_l2of, text='ГЛН L2OF', borderwidth=1, width=self.col_width_0, font=f'Times {self.body_font_size}', anchor='w')
        self.gln_l2of_label.grid()

        self.gln_l2of_tu = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2of_tu.grid(row=4 + row, column=1 + col)
        self.gln_l2of_tu_label = Label(self.gln_l2of_tu, text='8', borderwidth=1, width=self.col_width_1, font=f'Times {self.body_font_size}')
        self.gln_l2of_tu_label.value = 8
        self.gln_l2of_tu_label.grid()

        self.gln_l2of_fact = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2of_fact.grid(row=4 + row, column=2 + col)
        self.gln_l2of_fact_label = Label(self.gln_l2of_fact, text='', borderwidth=1, width=self.col_width_2, font=f'Times {self.body_font_size}')
        self.gln_l2of_fact_label.value = 0
        self.gln_l2of_fact_label.grid()

        self.gln_l2of_status = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2of_status.grid(row=4 + row, column=3 + col)
        self.gln_l2of_status_label = Label(self.gln_l2of_status, text='', borderwidth=1, width=self.col_width_3, font=f'Times {self.body_font_size}')
        self.gln_l2of_status_label.value = False
        self.gln_l2of_status_label.grid()

        """GLONASS L2SF"""
        self.gln_l2sf = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2sf.grid(row=5 + row, column=0 + col)
        self.gln_l2sf_label = Label(self.gln_l2sf, text='ГЛН L2SF', borderwidth=1, width=self.col_width_0, font=f'Times {self.body_font_size}', anchor='w')
        self.gln_l2sf_label.grid()

        self.gln_l2sf_tu = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2sf_tu.grid(row=5 + row, column=1 + col)
        self.gln_l2sf_tu_label = Label(self.gln_l2sf_tu, text='8', borderwidth=1, width=self.col_width_1, font=f'Times {self.body_font_size}')
        self.gln_l2sf_tu_label.value = 8
        self.gln_l2sf_tu_label.grid()

        self.gln_l2sf_fact = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2sf_fact.grid(row=5 + row, column=2 + col)
        self.gln_l2sf_fact_label = Label(self.gln_l2sf_fact, text='', borderwidth=1, width=self.col_width_2, font=f'Times {self.body_font_size}')
        self.gln_l2sf_fact_label.value = 0
        self.gln_l2sf_fact_label.grid()

        self.gln_l2sf_status = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2sf_status.grid(row=5 + row, column=3 + col)
        self.gln_l2sf_status_label = Label(self.gln_l2sf_status, text='', borderwidth=1, width=self.col_width_3, font=f'Times {self.body_font_size}')
        self.gln_l2sf_status_label.value = False
        self.gln_l2sf_status_label.grid()

        """GLONASS L1OCp"""
        self.gln_l1oc_mix = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1oc_mix.grid(row=6 + row, column=0 + col, sticky='wns', rowspan=2)
        self.gln_l1oc_mix_label = Label(self.gln_l1oc_mix, text='ГЛН L1OC', borderwidth=1, width=int(self.col_width_0 * 0.75), anchor='w', font=f'Times {self.body_font_size}')
        self.gln_l1oc_mix_label.grid(ipady=8)

        self.gln_l1oc_p = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1oc_p.grid(row=6 + row, column=0 + col, sticky='en')
        self.gln_l1oc_p_label = Label(self.gln_l1oc_p, text='p', borderwidth=1, width=int(self.col_width_0 * 0.25), font=f'Times {self.body_font_size}')
        self.gln_l1oc_p_label.grid()

        self.gln_l1oc_p_tu = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1oc_p_tu.grid(row=6 + row, column=1 + col, sticky='n')
        self.gln_l1oc_p_tu_label = Label(self.gln_l1oc_p_tu, text='8', borderwidth=1, width=self.col_width_1, font=f'Times {self.body_font_size}')
        self.gln_l1oc_p_tu_label.value = 8
        self.gln_l1oc_p_tu_label.grid()

        self.gln_l1oc_p_fact = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1oc_p_fact.grid(row=6 + row, column=2 + col, sticky='n')
        self.gln_l1oc_p_fact_label = Label(self.gln_l1oc_p_fact, text='', borderwidth=1, width=self.col_width_2, font=f'Times {self.body_font_size}')
        self.gln_l1oc_p_fact_label.value = 0
        self.gln_l1oc_p_fact_label.grid()

        self.gln_l1oc_p_status = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1oc_p_status.grid(row=6 + row, column=3 + col, sticky='n')
        self.gln_l1oc_p_status_label = Label(self.gln_l1oc_p_status, text='', borderwidth=1, width=self.col_width_3, font=f'Times {self.body_font_size}')
        self.gln_l1oc_p_status_label.value = False
        self.gln_l1oc_p_status_label.grid()

        """GLONASS L1OCd"""
        self.gln_l1oc_d = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1oc_d.grid(row=7 + row, column=0 + col, sticky='es')
        self.gln_l1oc_d_label = Label(self.gln_l1oc_d, text='d', borderwidth=1, width=int(self.col_width_0 * 0.25), font=f'Times {self.body_font_size}')
        self.gln_l1oc_d_label.grid()

        self.gln_l1oc_d_tu = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1oc_d_tu.grid(row=7 + row, column=1 + col, sticky='s')
        self.gln_l1oc_d_tu_label = Label(self.gln_l1oc_d_tu, text='8', borderwidth=1, width=self.col_width_1, font=f'Times {self.body_font_size}')
        self.gln_l1oc_d_tu_label.value = 8
        self.gln_l1oc_d_tu_label.grid()

        self.gln_l1oc_d_fact = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1oc_d_fact.grid(row=7 + row, column=2 + col, sticky='s')
        self.gln_l1oc_d_fact_label = Label(self.gln_l1oc_d_fact, text='', borderwidth=1, width=self.col_width_2, font=f'Times {self.body_font_size}')
        self.gln_l1oc_d_fact_label.value = 0
        self.gln_l1oc_d_fact_label.grid()

        self.gln_l1oc_d_status = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1oc_d_status.grid(row=7 + row, column=3 + col, sticky='s')
        self.gln_l1oc_d_status_label = Label(self.gln_l1oc_d_status, text='', borderwidth=1, width=self.col_width_3, font=f'Times {self.body_font_size}')
        self.gln_l1oc_d_status_label.value = False
        self.gln_l1oc_d_status_label.grid()

        """GLONASS L1SCp"""
        self.gln_l1sc_mix = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1sc_mix.grid(row=8 + row, column=0 + col, sticky='wns', rowspan=2)
        self.gln_l1sc_mix_label = Label(self.gln_l1sc_mix, text='ГЛН L1SC', borderwidth=1, width=int(self.col_width_0 * 0.75), anchor='w', font=f'Times {self.body_font_size}')
        self.gln_l1sc_mix_label.grid(ipady=8)

        self.gln_l1sc_p = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1sc_p.grid(row=8 + row, column=0 + col, sticky='en')
        self.gln_l1sc_p_label = Label(self.gln_l1sc_p, text='p', borderwidth=1, width=int(self.col_width_0 * 0.25), font=f'Times {self.body_font_size}')
        self.gln_l1sc_p_label.grid()

        self.gln_l1sc_p_tu = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1sc_p_tu.grid(row=8 + row, column=1 + col, sticky='n')
        self.gln_l1sc_p_tu_label = Label(self.gln_l1sc_p_tu, text='8', borderwidth=1, width=self.col_width_1, font=f'Times {self.body_font_size}')
        self.gln_l1sc_p_tu_label.value = 8
        self.gln_l1sc_p_tu_label.grid()

        self.gln_l1sc_p_fact = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1sc_p_fact.grid(row=8 + row, column=2 + col, sticky='n')
        self.gln_l1sc_p_fact_label = Label(self.gln_l1sc_p_fact, text='', borderwidth=1, width=self.col_width_2, font=f'Times {self.body_font_size}')
        self.gln_l1sc_p_fact_label.value = 0
        self.gln_l1sc_p_fact_label.grid()

        self.gln_l1sc_p_status = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1sc_p_status.grid(row=8 + row, column=3 + col, sticky='n')
        self.gln_l1sc_p_status_label = Label(self.gln_l1sc_p_status, text='', borderwidth=1, width=self.col_width_3, font=f'Times {self.body_font_size}')
        self.gln_l1sc_p_status_label.value = False
        self.gln_l1sc_p_status_label.grid()

        """GLONASS L1SCd"""
        self.gln_l1sc_d = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1sc_d.grid(row=9 + row, column=0 + col, sticky='es')
        self.gln_l1sc_d_label = Label(self.gln_l1sc_d, text='d', borderwidth=1, width=int(self.col_width_0 * 0.25), font=f'Times {self.body_font_size}')
        self.gln_l1sc_d_label.grid()

        self.gln_l1sc_d_tu = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1sc_d_tu.grid(row=9 + row, column=1 + col, sticky='s')
        self.gln_l1sc_d_tu_label = Label(self.gln_l1sc_d_tu, text='8', borderwidth=1, width=self.col_width_1, font=f'Times {self.body_font_size}')
        self.gln_l1sc_d_tu_label.value = 8
        self.gln_l1sc_d_tu_label.grid()

        self.gln_l1sc_d_fact = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1sc_d_fact.grid(row=9 + row, column=2 + col, sticky='s')
        self.gln_l1sc_d_fact_label = Label(self.gln_l1sc_d_fact, text='', borderwidth=1, width=self.col_width_2, font=f'Times {self.body_font_size}')
        self.gln_l1sc_d_fact_label.value = 0
        self.gln_l1sc_d_fact_label.grid()

        self.gln_l1sc_d_status = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l1sc_d_status.grid(row=9 + row, column=3 + col, sticky='s')
        self.gln_l1sc_d_status_label = Label(self.gln_l1sc_d_status, text='', borderwidth=1, width=self.col_width_3, font=f'Times {self.body_font_size}')
        self.gln_l1sc_d_status_label.value = False
        self.gln_l1sc_d_status_label.grid()

        """GLONASS L2OC"""
        self.gln_l2oc_mix = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2oc_mix.grid(row=10 + row, column=0 + col, sticky='wns', rowspan=2)
        self.gln_l2oc_mix_label = Label(self.gln_l2oc_mix, text='ГЛН L2OC', borderwidth=1, width=int(self.col_width_0 * 0.75), anchor='w', font=f'Times {self.body_font_size}')
        self.gln_l2oc_mix_label.grid(ipady=8)

        self.gln_l2oc_p = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2oc_p.grid(row=10 + row, column=0 + col, sticky='en')
        self.gln_l2oc_p_label = Label(self.gln_l2oc_p, text='p', borderwidth=1, width=int(self.col_width_0 * 0.25), font=f'Times {self.body_font_size}')
        self.gln_l2oc_p_label.grid()

        self.gln_l2oc_p_tu = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2oc_p_tu.grid(row=10 + row, column=1 + col, sticky='n')
        self.gln_l2oc_p_tu_label = Label(self.gln_l2oc_p_tu, text='8', borderwidth=1, width=self.col_width_1, font=f'Times {self.body_font_size}')
        self.gln_l2oc_p_tu_label.value = 8
        self.gln_l2oc_p_tu_label.grid()

        self.gln_l2oc_p_fact = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2oc_p_fact.grid(row=10 + row, column=2 + col, sticky='n')
        self.gln_l2oc_p_fact_label = Label(self.gln_l2oc_p_fact, text='', borderwidth=1, width=self.col_width_2, font=f'Times {self.body_font_size}')
        self.gln_l2oc_p_fact_label.value = 0
        self.gln_l2oc_p_fact_label.grid()

        self.gln_l2oc_p_status = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2oc_p_status.grid(row=10 + row, column=3 + col, sticky='n')
        self.gln_l2oc_p_status_label = Label(self.gln_l2oc_p_status, text='', borderwidth=1, width=self.col_width_3, font=f'Times {self.body_font_size}')
        self.gln_l2oc_p_status_label.value = False
        self.gln_l2oc_p_status_label.grid()

        """GLONASS L2OC_КСИ"""
        self.gln_l2oc_d = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2oc_d.grid(row=11 + row, column=0 + col, sticky='es')
        self.gln_l2oc_d_label = Label(self.gln_l2oc_d, text='КСИ', borderwidth=1, width=int(self.col_width_0 * 0.25), font=f'Times {self.body_font_size}')
        self.gln_l2oc_d_label.grid()

        self.gln_l2oc_d_tu = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2oc_d_tu.grid(row=11 + row, column=1 + col, sticky='s')
        self.gln_l2oc_d_tu_label = Label(self.gln_l2oc_d_tu, text='8', borderwidth=1, width=self.col_width_1, font=f'Times {self.body_font_size}')
        self.gln_l2oc_d_tu_label.value = 8
        self.gln_l2oc_d_tu_label.grid()

        self.gln_l2oc_d_fact = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2oc_d_fact.grid(row=11 + row, column=2 + col, sticky='s')
        self.gln_l2oc_d_fact_label = Label(self.gln_l2oc_d_fact, text='', borderwidth=1, width=self.col_width_2, font=f'Times {self.body_font_size}')
        self.gln_l2oc_d_fact_label.value = 0
        self.gln_l2oc_d_fact_label.grid()

        self.gln_l2oc_d_status = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2oc_d_status.grid(row=11 + row, column=3 + col, sticky='s')
        self.gln_l2oc_d_status_label = Label(self.gln_l2oc_d_status, text='', borderwidth=1, width=self.col_width_3, font=f'Times {self.body_font_size}')
        self.gln_l2oc_d_status_label.value = False
        self.gln_l2oc_d_status_label.grid()

        """GLONASS L2SCp"""
        self.gln_l2sc_mix = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2sc_mix.grid(row=12 + row, column=0 + col, sticky='wns', rowspan=2)
        self.gln_l2sc_mix_label = Label(self.gln_l2sc_mix, text='ГЛН L2OC', borderwidth=1, width=int(self.col_width_0 * 0.75), anchor='w', font=f'Times {self.body_font_size}')
        self.gln_l2sc_mix_label.grid(ipady=8)

        self.gln_l2sc_p = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2sc_p.grid(row=12 + row, column=0 + col, sticky='en')
        self.gln_l2sc_p_label = Label(self.gln_l2sc_p, text='p', borderwidth=1, width=int(self.col_width_0 * 0.25), font=f'Times {self.body_font_size}')
        self.gln_l2sc_p_label.grid()

        self.gln_l2sc_p_tu = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2sc_p_tu.grid(row=12 + row, column=1 + col, sticky='n')
        self.gln_l2sc_p_tu_label = Label(self.gln_l2sc_p_tu, text='8', borderwidth=1, width=self.col_width_1, font=f'Times {self.body_font_size}')
        self.gln_l2sc_p_tu_label.value = 8
        self.gln_l2sc_p_tu_label.grid()

        self.gln_l2sc_p_fact = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2sc_p_fact.grid(row=12 + row, column=2 + col, sticky='n')
        self.gln_l2sc_p_fact_label = Label(self.gln_l2sc_p_fact, text='', borderwidth=1, width=self.col_width_2, font=f'Times {self.body_font_size}')
        self.gln_l2sc_p_fact_label.value = 0
        self.gln_l2sc_p_fact_label.grid()

        self.gln_l2sc_p_status = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2sc_p_status.grid(row=12 + row, column=3 + col, sticky='n')
        self.gln_l2sc_p_status_label = Label(self.gln_l2sc_p_status, text='', borderwidth=1, width=self.col_width_3, font=f'Times {self.body_font_size}')
        self.gln_l2sc_p_status_label.value = False
        self.gln_l2sc_p_status_label.grid()

        """GLONASS L2SCd"""
        self.gln_l2sc_d = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2sc_d.grid(row=13 + row, column=0 + col, sticky='es')
        self.gln_l2sc_d_label = Label(self.gln_l2sc_d, text='d', borderwidth=1, width=int(self.col_width_0 * 0.25), font=f'Times {self.body_font_size}')
        self.gln_l2sc_d_label.grid()

        self.gln_l2sc_d_tu = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2sc_d_tu.grid(row=13 + row, column=1 + col, sticky='s')
        self.gln_l2sc_d_tu_label = Label(self.gln_l2sc_d_tu, text='8', borderwidth=1, width=self.col_width_1, font=f'Times {self.body_font_size}')
        self.gln_l2sc_d_tu_label.value = 8
        self.gln_l2sc_d_tu_label.grid()

        self.gln_l2sc_d_fact = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2sc_d_fact.grid(row=13 + row, column=2 + col, sticky='s')
        self.gln_l2sc_d_fact_label = Label(self.gln_l2sc_d_fact, text='', borderwidth=1, width=self.col_width_2, font=f'Times {self.body_font_size}')
        self.gln_l2sc_d_fact_label.value = 0
        self.gln_l2sc_d_fact_label.grid()

        self.gln_l2sc_d_status = Frame(window, relief=RAISED, borderwidth=1)
        self.gln_l2sc_d_status.grid(row=13 + row, column=3 + col, sticky='s')
        self.gln_l2sc_d_status_label = Label(self.gln_l2sc_d_status, text='', borderwidth=1, width=self.col_width_3, font=f'Times {self.body_font_size}')
        self.gln_l2sc_d_status_label.value = False
        self.gln_l2sc_d_status_label.grid()

        """GPS L1"""
        self.gps_l1 = Frame(window, relief=RAISED, borderwidth=1)
        self.gps_l1.grid(row=14 + row, column=0 + col)
        self.gps_l1_label = Label(self.gps_l1, text='GPS L1', borderwidth=1, width=self.col_width_0, font=f'Times {self.body_font_size}', anchor='w')
        self.gps_l1_label.grid()

        self.gps_l1_tu = Frame(window, relief=RAISED, borderwidth=1)
        self.gps_l1_tu.grid(row=14 + row, column=1 + col)
        self.gps_l1_tu_label = Label(self.gps_l1_tu, text='9', borderwidth=1, width=self.col_width_1, font=f'Times {self.body_font_size}')
        self.gps_l1_tu_label.value = 9
        self.gps_l1_tu_label.grid()

        self.gps_l1_fact = Frame(window, relief=RAISED, borderwidth=1)
        self.gps_l1_fact.grid(row=14 + row, column=2 + col)
        self.gps_l1_fact_label = Label(self.gps_l1_fact, text='', borderwidth=1, width=self.col_width_2, font=f'Times {self.body_font_size}')
        self.gps_l1_fact_label.value = 0
        self.gps_l1_fact_label.grid()

        self.gps_l1_status = Frame(window, relief=RAISED, borderwidth=1)
        self.gps_l1_status.grid(row=14 + row, column=3 + col)
        self.gps_l1_status_label = Label(self.gps_l1_status, text='', borderwidth=1, width=self.col_width_3, font=f'Times {self.body_font_size}')
        self.gps_l1_status_label.value = False
        self.gps_l1_status_label.grid()

        """GPS L2"""
        self.gps_l2_mix = Frame(window, relief=RAISED, borderwidth=1)
        self.gps_l2_mix.grid(row=15 + row, column=0 + col, sticky='wns', rowspan=2)
        self.gps_l2_mix_label = Label(self.gps_l2_mix, text='ГЛН L2OC', borderwidth=1, width=int(self.col_width_0 * 0.75), anchor='w', font=f'Times {self.body_font_size}')
        self.gps_l2_mix_label.grid(ipady=8)

        self.gps_l2_l = Frame(window, relief=RAISED, borderwidth=1)
        self.gps_l2_l.grid(row=15 + row, column=0 + col, sticky='en')
        self.gps_l2_l_label = Label(self.gps_l2_l, text='L', borderwidth=1, width=int(self.col_width_0 * 0.25), font=f'Times {self.body_font_size}')
        self.gps_l2_l_label.grid()

        self.gps_l2_l_tu = Frame(window, relief=RAISED, borderwidth=1)
        self.gps_l2_l_tu.grid(row=15 + row, column=1 + col, sticky='n')
        self.gps_l2_l_tu_label = Label(self.gps_l2_l_tu, text='8', borderwidth=1, width=self.col_width_1, font=f'Times {self.body_font_size}')
        self.gps_l2_l_tu_label.value = 8
        self.gps_l2_l_tu_label.grid()

        self.gps_l2_l_fact = Frame(window, relief=RAISED, borderwidth=1)
        self.gps_l2_l_fact.grid(row=15 + row, column=2 + col, sticky='n')
        self.gps_l2_l_fact_label = Label(self.gps_l2_l_fact, text='', borderwidth=1, width=self.col_width_2, font=f'Times {self.body_font_size}')
        self.gps_l2_l_label.value = 0
        self.gps_l2_l_fact_label.grid()

        self.gps_l2_l_status = Frame(window, relief=RAISED, borderwidth=1)
        self.gps_l2_l_status.grid(row=15 + row, column=3 + col, sticky='n')
        self.gps_l2_l_status_label = Label(self.gps_l2_l_status, text='', borderwidth=1, width=self.col_width_3, font=f'Times {self.body_font_size}')
        self.gps_l2_l_status_label.value = False
        self.gps_l2_l_status_label.grid()

        """GPS L2M"""
        self.gps_l2_m = Frame(window, relief=RAISED, borderwidth=1)
        self.gps_l2_m.grid(row=16 + row, column=0 + col, sticky='es')
        self.gps_l2_m_label = Label(self.gps_l2_m, text='M', borderwidth=1, width=int(self.col_width_0 * 0.25), font=f'Times {self.body_font_size}')
        self.gps_l2_m_label.grid()

        self.gps_l2_m_tu = Frame(window, relief=RAISED, borderwidth=1)
        self.gps_l2_m_tu.grid(row=16 + row, column=1 + col, sticky='s')
        self.gps_l2_m_tu_label = Label(self.gps_l2_m_tu, text='8', borderwidth=1, width=self.col_width_1, font=f'Times {self.body_font_size}')
        self.gps_l2_m_tu_label.value = 8
        self.gps_l2_m_tu_label.grid()

        self.gps_l2_m_fact = Frame(window, relief=RAISED, borderwidth=1)
        self.gps_l2_m_fact.grid(row=16 + row, column=2 + col, sticky='s')
        self.gps_l2_m_fact_label = Label(self.gps_l2_m_fact, text='', borderwidth=1, width=self.col_width_2, font=f'Times {self.body_font_size}')
        self.gps_l2_m_fact_label.value = 0
        self.gps_l2_m_fact_label.grid()

        self.gps_l2_m_status = Frame(window, relief=RAISED, borderwidth=1)
        self.gps_l2_m_status.grid(row=16 + row, column=3 + col, sticky='s')
        self.gps_l2_m_status_label = Label(self.gps_l2_m_status, text='', borderwidth=1, width=self.col_width_3, font=f'Times {self.body_font_size}')
        self.gps_l2_m_status_label.value = False
        self.gps_l2_m_status_label.grid()


        """СДКМ"""
        self.sdkm = Frame(window, relief=RAISED, borderwidth=1)
        self.sdkm.grid(row=17 + row, column=0 + col)
        self.sdkm_label = Label(self.sdkm, text='СДКМ', borderwidth=1, width=self.col_width_0, font=f'Times {self.body_font_size}', anchor='w')
        self.sdkm_label.grid()

        self.sdkm_tu = Frame(window, relief=RAISED, borderwidth=1)
        self.sdkm_tu.grid(row=17 + row, column=1 + col)
        self.sdkm_tu_label = Label(self.sdkm_tu, text='9', borderwidth=1, width=self.col_width_1, font=f'Times {self.body_font_size}')
        self.sdkm_tu_label.value = 9
        self.sdkm_tu_label.grid()

        self.sdkm_fact = Frame(window, relief=RAISED, borderwidth=1)
        self.sdkm_fact.grid(row=17 + row, column=2 + col)
        self.sdkm_fact_label = Label(self.sdkm_fact, text='', borderwidth=1, width=self.col_width_2, font=f'Times {self.body_font_size}')
        self.sdkm_fact_label.value = 0
        self.sdkm_fact_label.grid()

        self.sdkm_status = Frame(window, relief=RAISED, borderwidth=1)
        self.sdkm_status.grid(row=17 + row, column=3 + col)
        self.sdkm_status_label = Label(self.sdkm_status, text='', borderwidth=1, width=self.col_width_3, font=f'Times {self.body_font_size}')
        self.sdkm_status_label.value = False
        self.sdkm_status_label.grid()

        """ШДПС"""
        self.sdps = Frame(window, relief=RAISED, borderwidth=1)
        self.sdps.grid(row=18 + row, column=0 + col)
        self.sdps_label = Label(self.sdps, text='ШДПС', borderwidth=1, width=self.col_width_0, font=f'Times {self.body_font_size}', anchor='w')
        self.sdps_label.grid()

        self.sdps_tu = Frame(window, relief=RAISED, borderwidth=1)
        self.sdps_tu.grid(row=18 + row, column=1 + col)
        self.sdps_tu_label = Label(self.sdps_tu, text='9', borderwidth=1, width=self.col_width_1, font=f'Times {self.body_font_size}')
        self.sdps_tu_label.value = 9
        self.sdps_tu_label.grid()

        self.sdps_fact = Frame(window, relief=RAISED, borderwidth=1)
        self.sdps_fact.grid(row=18 + row, column=2 + col)
        self.sdps_fact_label = Label(self.sdps_fact, text='', borderwidth=1, width=self.col_width_2, font=f'Times {self.body_font_size}')
        self.sdps_fact_label.value = 0
        self.sdps_fact_label.grid()

        self.sdps_status = Frame(window, relief=RAISED, borderwidth=1)
        self.sdps_status.grid(row=18 + row, column=3 + col)
        self.sdps_status_label = Label(self.sdps_status, text='', borderwidth=1, width=self.col_width_3, font=f'Times {self.body_font_size}')
        self.sdps_status_label.value = False
        self.sdps_status_label.grid()


Headers(window, 0, 0, str(1))
Headers(window, 4, 0, str(2))
Headers(window, 8, 0, str(3))
Headers(window, 12, 0, str(4))
Headers(window, 16, 0, str(5))
Headers(window, 20, 0, str(5))
Headers(window, 24, 0, str(7))
Headers(window, 28, 0, str(8))


Headers(window, 0, 19, str(9))
Headers(window, 4, 19, str(10))
Headers(window, 8, 19, str(11))
Headers(window, 12, 19, str(12))
Headers(window, 16, 19, str(13))
Headers(window, 20, 19, str(14))
Headers(window, 24, 19, str(15))
Headers(window, 28, 19, str(16))

window.mainloop()
