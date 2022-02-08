import time
from tkinter import *

window = Tk()
window.wm_state('zoomed')
window.title('review')
window['background'] = 'white'

name_w = int(window.winfo_screenwidth() / 18.8)
tu_w = int(window.winfo_screenwidth() / 64)
fact_w = int(window.winfo_screenwidth() / 53.3)
status_w = int(window.winfo_screenwidth() / 40)
head_h = int(window.winfo_screenheight() / 33.3)
body_h = int(window.winfo_screenheight() / 50)
print(head_h)
pad_x = (int(window.winfo_screenwidth() / 70), 0)


class Headers():
    def __init__(self, window, col=0, row=0, port=None, name_w=0, tu_w=0, fact_w=0, status_w=0, head_h=0, pad_x=(0, 0), body_font='Times 8', body_h=body_h):
        self.number = port

        """Headers"""
        title = Frame(window, borderwidth=1, relief=RAISED)
        title.grid(row=0 + row, column=col, columnspan=4, sticky='ew', padx=pad_x)
        title_label = Label(title, text='COM' + port, font='Arial 12')
        title_label.grid()

        frame_names = Frame(window, relief=RAISED, borderwidth=1, width=name_w, height=head_h)
        frame_names.grid(column=0 + col, row=1 + row, padx=pad_x)
        frame_names.grid_propagate(False)
        label_names = Label(frame_names, text='Диапозон', borderwidth=1, font='Times 10')
        label_names.place(relx=0.5, rely=0.5, anchor='center')

        frame_const = Frame(window, relief=RAISED, borderwidth=1, width=tu_w, height=head_h)
        frame_const.grid(row=1 + row, column=1 + col)
        frame_const.grid_propagate(False)
        label_const = Label(frame_const, text='ТУ', font='Times 10')
        label_const.place(relx=0.5, rely=0.5, anchor='center')

        frame_count = Frame(window, relief=RAISED, borderwidth=1, width=fact_w, height=head_h)
        frame_count.grid(row=1 + row, column=2 + col)
        frame_count.grid_propagate(False)
        frame_count = Label(frame_count, text='Факт.', font='Times 10')
        frame_count.place(relx=0.5, rely=0.5, anchor='center')

        frame_status = Frame(window, relief=RAISED, borderwidth=1, width=status_w, height=head_h)
        frame_status.grid(row=1 + row, column=3 + col)
        frame_status.grid_propagate(False)
        label_status = Label(frame_status, text='Cтатус', font='Times 10')
        label_status.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L1OF"""
        gln_l1of = Frame(window, relief=RAISED, borderwidth=1, width=name_w, height=body_h)
        gln_l1of.grid(row=2 + row, column=0 + col, padx=pad_x)
        gln_l1of.grid_propagate(False)
        self.gln_l1of_label = Label(gln_l1of, text='ГЛН L1OF', font=body_font)
        self.gln_l1of_label.grid()

        gln_l1of_tu = Frame(window, relief=RAISED, borderwidth=1, width=tu_w, height=body_h)
        gln_l1of_tu.grid(row=2 + row, column=1+col)
        gln_l1of_tu.grid_propagate(False)
        self.gln_l1of_tu_label = Label(gln_l1of_tu, text='8', font=body_font)
        self.gln_l1of_tu_label.value = 8
        self.gln_l1of_tu_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l1of_fact = Frame(window, relief=RAISED, borderwidth=1, width=fact_w, height=body_h)
        gln_l1of_fact.grid(row=2 + row, column=2 + col)
        gln_l1of_fact.grid_propagate(False)
        self.gln_l1of_fact_label = Label(gln_l1of_fact, text='', font=body_font)
        self.gln_l1of_fact_label.value = 0
        self.gln_l1of_fact_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l1of_status = Frame(window, relief=RAISED, borderwidth=1, width=status_w, height=body_h)
        gln_l1of_status.grid(row=2 + row, column=3 + col)
        gln_l1of_status.grid_propagate(False)
        self.gln_l1of_status_label = Label(gln_l1of_status, text='', font=body_font)
        self.gln_l1of_status_label.value = False
        self.gln_l1of_status_label.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L1SF"""
        gln_l1sf = Frame(window, relief=RAISED, borderwidth=1, width=name_w, height=body_h)
        gln_l1sf.grid(row=3 + row, column=0 + col, padx=pad_x)
        gln_l1sf.grid_propagate(False)
        gln_l1sf_label = Label(gln_l1sf, text='ГЛН L1SF', font=body_font)
        gln_l1sf_label.grid()

        gln_l1sf_tu = Frame(window, relief=RAISED, borderwidth=1, width=tu_w, height=body_h)
        gln_l1sf_tu.grid(row=3 + row, column=1 + col)
        gln_l1sf_tu.grid_propagate(False)
        self.gln_l1sf_tu_label = Label(gln_l1sf_tu, text='8', font=body_font)
        self.gln_l1sf_tu_label.value = 8
        self.gln_l1sf_tu_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l1sf_fact = Frame(window, relief=RAISED, borderwidth=1, width=fact_w, height=body_h)
        gln_l1sf_fact.grid(row=3 + row, column=2 + col)
        gln_l1sf_fact.grid_propagate(False)
        self.gln_l1sf_fact_label = Label(gln_l1sf_fact, text='', font=body_font)
        self.gln_l1sf_fact_label.value = 0
        self.gln_l1sf_fact_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l1sf_status = Frame(window, relief=RAISED, borderwidth=1, width=status_w, height=body_h)
        gln_l1sf_status.grid(row=3 + row, column=3 + col)
        gln_l1sf_status.grid_propagate(False)
        self.gln_l1sf_status_label = Label(gln_l1sf_status, text='', font=body_font)
        self.gln_l1sf_status_label.value = False
        self.gln_l1sf_status_label.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L2OF"""
        gln_l2of = Frame(window, relief=RAISED, borderwidth=1, width=name_w, height=body_h)
        gln_l2of.grid(row=4 + row, column=0 + col, padx=pad_x)
        gln_l2of.grid_propagate(False)
        self.gln_l2of_label = Label(gln_l2of, text='ГЛН L2OF', font=body_font)
        self.gln_l2of_label.grid()

        gln_l2of_tu = Frame(window, relief=RAISED, borderwidth=1, width=tu_w, height=body_h)
        gln_l2of_tu.grid(row=4 + row, column=1 + col)
        gln_l2of_tu.grid_propagate(False)
        self.gln_l2of_tu_label = Label(gln_l2of_tu, text='8', font=body_font)
        self.gln_l2of_tu_label.value = 8
        self.gln_l2of_tu_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l2of_fact = Frame(window, relief=RAISED, borderwidth=1, width=fact_w, height=body_h)
        gln_l2of_fact.grid(row=4 + row, column=2 + col)
        gln_l2of_fact.grid_propagate(False)
        self.gln_l2of_fact_label = Label(gln_l2of_fact, text='', font=body_font)
        self.gln_l2of_fact_label.value = 0
        self.gln_l2of_fact_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l2of_status = Frame(window, relief=RAISED, borderwidth=1, width=status_w, height=body_h)
        gln_l2of_status.grid(row=4 + row, column=3 + col)
        gln_l2of_status.grid_propagate(False)
        self.gln_l2of_status_label = Label(gln_l2of_status, text='', font=body_font)
        self.gln_l2of_status_label.value = False
        self.gln_l2of_status_label.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L2SF"""
        gln_l2sf = Frame(window, relief=RAISED, borderwidth=1, width=name_w, height=body_h)
        gln_l2sf.grid(row=5 + row, column=0 + col, padx=pad_x)
        gln_l2sf.grid_propagate(False)
        self.gln_l2sf_label = Label(gln_l2sf, text='ГЛН L2SF', font=body_font)
        self.gln_l2sf_label.grid()

        gln_l2sf_tu = Frame(window, relief=RAISED, borderwidth=1, width=tu_w, height=body_h)
        gln_l2sf_tu.grid(row=5 + row, column=1 + col)
        gln_l2sf_tu.grid_propagate(False)
        self.gln_l2sf_tu_label = Label(gln_l2sf_tu, text='8', font=body_font)
        self.gln_l2sf_tu_label.value = 8
        self.gln_l2sf_tu_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l2sf_fact = Frame(window, relief=RAISED, borderwidth=1, width=fact_w, height=body_h)
        gln_l2sf_fact.grid(row=5 + row, column=2 + col)
        gln_l2sf_fact.grid_propagate(False)
        self.gln_l2sf_fact_label = Label(gln_l2sf_fact, text='', font=body_font)
        self.gln_l2sf_fact_label.value = 0
        self.gln_l2sf_fact_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l2sf_status = Frame(window, relief=RAISED, borderwidth=1, width=status_w, height=body_h)
        gln_l2sf_status.grid(row=5 + row, column=3 + col)
        gln_l2sf_status.grid_propagate(False)
        self.gln_l2sf_status_label = Label(gln_l2sf_status, text='', font=body_font)
        self.gln_l2sf_status_label.value = False
        self.gln_l2sf_status_label.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L1OC"""
        gln_l1oc_mix = Frame(window, relief=RAISED, borderwidth=1, width=int(name_w * 0.7), height=body_h * 2)
        gln_l1oc_mix.grid(row=6 + row, column=0 + col, sticky='w', padx=pad_x)
        gln_l1oc_mix.grid_propagate(False)
        self.gln_l1oc_mix_label = Label(gln_l1oc_mix, text='ГЛН L1OC', font=body_font)
        self.gln_l1oc_mix_label.place(rely=0.5, anchor='w')

        """GLONASS L1OCp"""
        gln_l1oc_p = Frame(window, relief=RAISED, borderwidth=1, width=int(name_w * 0.3), height=body_h)
        gln_l1oc_p.grid(row=6 + row, column=0 + col, sticky='en')
        gln_l1oc_p.grid_propagate(False)
        self.gln_l1oc_p_label = Label(gln_l1oc_p, text='p', font=body_font)
        self.gln_l1oc_p_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l1oc_p_tu = Frame(window, relief=RAISED, borderwidth=1, width=tu_w, height=body_h)
        gln_l1oc_p_tu.grid(row=6 + row, column=1 + col, sticky='n')
        gln_l1oc_p_tu.grid_propagate(False)
        self.gln_l1oc_p_tu_label = Label(gln_l1oc_p_tu, text='8', font=body_font)
        self.gln_l1oc_p_tu_label.value = 8
        self.gln_l1oc_p_tu_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l1oc_p_fact = Frame(window, relief=RAISED, borderwidth=1, width=fact_w, height=body_h)
        gln_l1oc_p_fact.grid(row=6 + row, column=2 + col, sticky='n')
        gln_l1oc_p_fact.grid_propagate(False)
        self.gln_l1oc_p_fact_label = Label(gln_l1oc_p_fact, text='', font=body_font)
        self.gln_l1oc_p_fact_label.value = 0
        self.gln_l1oc_p_fact_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l1oc_p_status = Frame(window, relief=RAISED, borderwidth=1, width=status_w, height=body_h)
        gln_l1oc_p_status.grid(row=6 + row, column=3 + col, sticky='n')
        gln_l1oc_p_status.grid_propagate(False)
        self.gln_l1oc_p_status_label = Label(gln_l1oc_p_status, text='', font=body_font)
        self.gln_l1oc_p_status_label.value = False
        self.gln_l1oc_p_status_label.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L1OCd"""
        gln_l1oc_d = Frame(window, relief=RAISED, borderwidth=1, width=int(name_w * 0.3), height=body_h)
        gln_l1oc_d.grid(row=6 + row, column=0 + col, sticky='es')
        gln_l1oc_d.grid_propagate(False)
        self.gln_l1oc_d_label = Label(gln_l1oc_d, text='d', font=body_font)
        self.gln_l1oc_d_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l1oc_d_tu = Frame(window, relief=RAISED, borderwidth=1, width=tu_w, height=body_h)
        gln_l1oc_d_tu.grid(row=6 + row, column=1 + col, sticky='s')
        gln_l1oc_d_tu.grid_propagate(False)
        self.gln_l1oc_d_tu_label = Label(gln_l1oc_d_tu, text='8', font=body_font)
        self.gln_l1oc_d_tu_label.value = 8
        self.gln_l1oc_d_tu_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l1oc_d_fact = Frame(window, relief=RAISED, borderwidth=1, width=fact_w, height=body_h)
        gln_l1oc_d_fact.grid(row=6 + row, column=2 + col, sticky='s')
        gln_l1oc_d_fact.grid_propagate(False)
        self.gln_l1oc_d_fact_label = Label(gln_l1oc_d_fact, text='', font=body_font)
        self.gln_l1oc_d_fact_label.value = 0
        self.gln_l1oc_d_fact_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l1oc_d_status = Frame(window, relief=RAISED, borderwidth=1, width=status_w, height=body_h)
        gln_l1oc_d_status.grid(row=6 + row, column=3 + col, sticky='s')
        gln_l1oc_d_status.grid_propagate(False)
        self.gln_l1oc_d_status_label = Label(gln_l1oc_d_status, text='', font=body_font)
        self.gln_l1oc_d_status_label.value = False
        self.gln_l1oc_d_status_label.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L1SC"""
        gln_l1sc_mix = Frame(window, relief=RAISED, borderwidth=1, width=int(name_w * 0.7), height=int(body_h *2))
        gln_l1sc_mix.grid(row=8 + row, column=0 + col, sticky='w', padx=pad_x)
        gln_l1sc_mix.grid_propagate(False)
        self.gln_l1sc_mix_label = Label(gln_l1sc_mix, text='ГЛН L1SC', font=body_font)
        self.gln_l1sc_mix_label.place(rely=0.5, anchor='w')

        """GLONASS L1SC_p"""
        gln_l1sc_p = Frame(window, relief=RAISED, borderwidth=1, width=int(name_w * 0.3), height=body_h)
        gln_l1sc_p.grid(row=8 + row, column=0 + col, sticky='en')
        gln_l1sc_p.grid_propagate(False)
        self.gln_l1sc_p_label = Label(gln_l1sc_p, text='p', font=body_font)
        self.gln_l1sc_p_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l1sc_p_tu = Frame(window, relief=RAISED, borderwidth=1, width=tu_w, height=body_h)
        gln_l1sc_p_tu.grid(row=8 + row, column=1 + col, sticky='n')
        gln_l1sc_p_tu.grid_propagate(False)
        self.gln_l1sc_p_tu_label = Label(gln_l1sc_p_tu, text='8', font=body_font)
        self.gln_l1sc_p_tu_label.value = 8
        self.gln_l1sc_p_tu_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l1sc_p_fact = Frame(window, relief=RAISED, borderwidth=1, width=fact_w, height=body_h)
        gln_l1sc_p_fact.grid(row=8 + row, column=2 + col, sticky='n')
        gln_l1sc_p_fact.grid_propagate(False)
        self.gln_l1sc_p_fact_label = Label(gln_l1sc_p_fact, text='', font=body_font)
        self.gln_l1sc_p_fact_label.value = 0
        self.gln_l1sc_p_fact_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l1sc_p_status = Frame(window, relief=RAISED, borderwidth=1, width=status_w, height=body_h)
        gln_l1sc_p_status.grid(row=8 + row, column=3 + col, sticky='n')
        gln_l1sc_p_status.grid_propagate(False)
        self.gln_l1sc_p_status_label = Label(gln_l1sc_p_status, text='', font=body_font)
        self.gln_l1sc_p_status_label.value = False
        self.gln_l1sc_p_status_label.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L1SCd"""
        gln_l1sc_d = Frame(window, relief=RAISED, borderwidth=1, width=int(name_w * 0.3), height=body_h)
        gln_l1sc_d.grid(row=8 + row, column=0 + col, sticky='es')
        gln_l1oc_d.grid_propagate(False)
        self.gln_l1sc_d_label = Label(gln_l1sc_d, text='d', font=body_font)
        self.gln_l1sc_d_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l1sc_d_tu = Frame(window, relief=RAISED, borderwidth=1, width=tu_w, height=body_h)
        gln_l1sc_d_tu.grid(row=8 + row, column=1 + col, sticky='s')
        gln_l1sc_d_tu.grid_propagate(False)
        self.gln_l1sc_d_tu_label = Label(gln_l1sc_d_tu, text='8', font=body_font)
        self.gln_l1sc_d_tu_label.value = 8
        self.gln_l1sc_d_tu_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l1sc_d_fact = Frame(window, relief=RAISED, borderwidth=1, width=fact_w, height=body_h)
        gln_l1sc_d_fact.grid(row=8 + row, column=2 + col, sticky='s')
        gln_l1sc_d_fact.grid_propagate(False)
        self.gln_l1sc_d_fact_label = Label(gln_l1sc_d_fact, text='', font=body_font)
        self.gln_l1sc_d_fact_label.value = 0
        self.gln_l1sc_d_fact_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l1sc_d_status = Frame(window, relief=RAISED, borderwidth=1, width=status_w, height=body_h)
        gln_l1sc_d_status.grid(row=8 + row, column=3 + col, sticky='s')
        gln_l1sc_d_status.grid_propagate(False)
        self.gln_l1sc_d_status_label = Label(gln_l1sc_d_status, text='', font=body_font)
        self.gln_l1sc_d_status_label.value = False
        self.gln_l1sc_d_status_label.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L2OC"""
        gln_l2oc_mix = Frame(window, relief=RAISED, borderwidth=1, width=int(name_w * 0.7), height=int(body_h * 2))
        gln_l2oc_mix.grid(row=10 + row, column=0 + col, sticky='w', padx=pad_x)
        gln_l2oc_mix.grid_propagate(False)
        self.gln_l2oc_mix_label = Label(gln_l2oc_mix, text='ГЛН L2OC', font=body_font)
        self.gln_l2oc_mix_label.place(rely=0.5, anchor='w')

        """GLONASS L2OCp"""
        gln_l2oc_p = Frame(window, relief=RAISED, borderwidth=1, width=int(name_w * 0.3), height=body_h)
        gln_l2oc_p.grid(row=10 + row, column=0 + col, sticky='en')
        gln_l1oc_p.grid_propagate(False)
        self.gln_l2oc_p_label = Label(gln_l2oc_p, text='p', font=body_font)
        self.gln_l2oc_p_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l2oc_p_tu = Frame(window, relief=RAISED, borderwidth=1, width=tu_w, height=body_h)
        gln_l2oc_p_tu.grid(row=10 + row, column=1 + col, sticky='n')
        gln_l2oc_p_tu.grid_propagate(False)
        self.gln_l2oc_p_tu_label = Label(gln_l2oc_p_tu, text='8', font=body_font)
        self.gln_l2oc_p_tu_label.value = 8
        self.gln_l2oc_p_tu_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l2oc_p_fact = Frame(window, relief=RAISED, borderwidth=1, width=fact_w, height=body_h)
        gln_l2oc_p_fact.grid(row=10 + row, column=2 + col, sticky='n')
        gln_l2oc_p_fact.grid_propagate(False)
        self.gln_l2oc_p_fact_label = Label(gln_l2oc_p_fact, text='', font=body_font)
        self.gln_l2oc_p_fact_label.value = 0
        self.gln_l2oc_p_fact_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l2oc_p_status = Frame(window, relief=RAISED, borderwidth=1, width=status_w, height=body_h)
        gln_l2oc_p_status.grid(row=10 + row, column=3 + col, sticky='n')
        gln_l2oc_p_status.grid_propagate(False)
        self.gln_l2oc_p_status_label = Label(gln_l2oc_p_status, text='', font=body_font)
        self.gln_l2oc_p_status_label.value = False
        self.gln_l2oc_p_status_label.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L2OC_КСИ"""
        gln_l2oc_d = Frame(window, relief=RAISED, borderwidth=1, width=int(name_w * 0.3), height=body_h)
        gln_l2oc_d.grid(row=10 + row, column=0 + col, sticky='es')
        gln_l1oc_d.grid_propagate(False)
        self.gln_l2oc_d_label = Label(gln_l2oc_d, text='КСИ', font=body_font)
        self.gln_l2oc_d_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l2oc_d_tu = Frame(window, relief=RAISED, borderwidth=1, width=tu_w, height=body_h)
        gln_l2oc_d_tu.grid(row=10 + row, column=1 + col, sticky='s')
        gln_l2oc_d_tu.grid_propagate(False)
        self.gln_l2oc_d_tu_label = Label(gln_l2oc_d_tu, text='8', font=body_font)
        self.gln_l2oc_d_tu_label.value = 8
        self.gln_l2oc_d_tu_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l2oc_d_fact = Frame(window, relief=RAISED, borderwidth=1, width=fact_w, height=body_h)
        gln_l2oc_d_fact.grid(row=10 + row, column=2 + col, sticky='s')
        gln_l2oc_d_fact.grid_propagate(False)
        self.gln_l2oc_d_fact_label = Label(gln_l2oc_d_fact, text='', font=body_font)
        self.gln_l2oc_d_fact_label.value = 0
        self.gln_l2oc_d_fact_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l2oc_d_status = Frame(window, relief=RAISED, borderwidth=1, width=status_w, height=body_h)
        gln_l2oc_d_status.grid(row=10 + row, column=3 + col, sticky='s')
        gln_l2oc_d_status.grid_propagate(False)
        self.gln_l2oc_d_status_label = Label(gln_l2oc_d_status, text='', font=body_font)
        self.gln_l2oc_d_status_label.value = False
        self.gln_l2oc_d_status_label.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L2SC"""
        gln_l2sc_mix = Frame(window, relief=RAISED, borderwidth=1, width=int(name_w * 0.7), height=int(body_h * 2))
        gln_l2sc_mix.grid(row=12 + row, column=0 + col, sticky='w', padx=pad_x)
        gln_l2sc_mix.grid_propagate(False)
        self.gln_l2sc_mix_label = Label(gln_l2sc_mix, text='ГЛН L2OC', font=body_font)
        self.gln_l2sc_mix_label.place(rely=0.5, anchor='w')

        """GLONASS L2SCp"""
        gln_l2sc_p = Frame(window, relief=RAISED, borderwidth=1, width=int(name_w * 0.3), height=body_h)
        gln_l2sc_p.grid(row=12 + row, column=0 + col, sticky='en')
        gln_l2sc_p.grid_propagate(False)
        self.gln_l2sc_p_label = Label(gln_l2sc_p, text='p', font=body_font)
        self.gln_l2sc_p_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l2sc_p_tu = Frame(window, relief=RAISED, borderwidth=1, width=tu_w, height=body_h)
        gln_l2sc_p_tu.grid(row=12 + row, column=1 + col, sticky='n')
        gln_l2sc_p_tu.grid_propagate(False)
        self.gln_l2sc_p_tu_label = Label(gln_l2sc_p_tu, text='8', font=body_font)
        self.gln_l2sc_p_tu_label.value = 8
        self.gln_l2sc_p_tu_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l2sc_p_fact = Frame(window, relief=RAISED, borderwidth=1, width=fact_w, height=body_h)
        gln_l2sc_p_fact.grid(row=12 + row, column=2 + col, sticky='n')
        gln_l2sc_p_fact.grid_propagate(False)
        self.gln_l2sc_p_fact_label = Label(gln_l2sc_p_fact, text='', font=body_font)
        self.gln_l2sc_p_fact_label.value = 0
        self.gln_l2sc_p_fact_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l2sc_p_status = Frame(window, relief=RAISED, borderwidth=1, width=status_w, height=body_h)
        gln_l2sc_p_status.grid(row=12 + row, column=3 + col, sticky='n')
        gln_l2sc_p_status.grid_propagate(False)
        self.gln_l2sc_p_status_label = Label(gln_l2sc_p_status, text='', font=body_font)
        self.gln_l2sc_p_status_label.value = False
        self.gln_l2sc_p_status_label.place(relx=0.5, rely=0.5, anchor='center')

        """GLONASS L2SCd"""
        gln_l2sc_d = Frame(window, relief=RAISED, borderwidth=1, width=int(name_w * 0.3), height=body_h)
        gln_l2sc_d.grid(row=12 + row, column=0 + col, sticky='es')
        gln_l2sc_d.grid_propagate(False)
        self.gln_l2sc_d_label = Label(gln_l2sc_d, text='d', font=body_font)
        self.gln_l2sc_d_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l2sc_d_tu = Frame(window, relief=RAISED, borderwidth=1, width=tu_w, height=body_h)
        gln_l2sc_d_tu.grid(row=12 + row, column=1 + col, sticky='s')
        gln_l2sc_d_tu.grid_propagate(False)
        self.gln_l2sc_d_tu_label = Label(gln_l2sc_d_tu, text='8', font=body_font)
        self.gln_l2sc_d_tu_label.value = 8
        self.gln_l2sc_d_tu_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l2sc_d_fact = Frame(window, relief=RAISED, borderwidth=1, width=fact_w, height=body_h)
        gln_l2sc_d_fact.grid(row=12 + row, column=2 + col, sticky='s')
        gln_l2sc_d_tu.grid_propagate(False)
        self.gln_l2sc_d_fact_label = Label(gln_l2sc_d_fact, text='', font=body_font)
        self.gln_l2sc_d_fact_label.value = 0
        self.gln_l2sc_d_fact_label.place(relx=0.5, rely=0.5, anchor='center')

        gln_l2sc_d_status = Frame(window, relief=RAISED, borderwidth=1, width=status_w, height=body_h)
        gln_l2sc_d_status.grid(row=12 + row, column=3 + col, sticky='s')
        gln_l2sc_d_tu.grid_propagate(False)
        self.gln_l2sc_d_status_label = Label(gln_l2sc_d_status, text='', font=body_font)
        self.gln_l2sc_d_status_label.value = False
        self.gln_l2sc_d_status_label.place(relx=0.5, rely=0.5, anchor='center')


        pas_frame = Frame(window, height=50)
        pas_frame.grid(row=13)
















a = Headers(window, col=0, row=0, port=str(1), name_w=name_w, tu_w=tu_w, fact_w=fact_w, status_w=status_w, head_h=head_h)
Headers(window, col=4, row=0, port=str(2), name_w=name_w, tu_w=tu_w, fact_w=fact_w, status_w=status_w, head_h=head_h, pad_x=pad_x)
Headers(window, col=8, row=0, port=str(3), name_w=name_w, tu_w=tu_w, fact_w=fact_w, status_w=status_w, head_h=head_h, pad_x=pad_x)
Headers(window, col=12, row=0, port=str(4), name_w=name_w, tu_w=tu_w, fact_w=fact_w, status_w=status_w, head_h=head_h, pad_x=pad_x)
Headers(window, col=16, row=0, port=str(5), name_w=name_w, tu_w=tu_w, fact_w=fact_w, status_w=status_w, head_h=head_h, pad_x=pad_x)
Headers(window, col=20, row=0, port=str(6), name_w=name_w, tu_w=tu_w, fact_w=fact_w, status_w=status_w, head_h=head_h, pad_x=pad_x)
Headers(window, col=24, row=0, port=str(7), name_w=name_w, tu_w=tu_w, fact_w=fact_w, status_w=status_w, head_h=head_h, pad_x=pad_x)
Headers(window, col=28, row=0, port=str(8), name_w=name_w, tu_w=tu_w, fact_w=fact_w, status_w=status_w, head_h=head_h, pad_x=pad_x)


Headers(window, col=0, row=19, port=str(9), name_w=name_w, tu_w=tu_w, fact_w=fact_w, status_w=status_w, head_h=head_h)
Headers(window, col=4, row=19, port=str(10), name_w=name_w, tu_w=tu_w, fact_w=fact_w, status_w=status_w, head_h=head_h, pad_x=pad_x)
Headers(window, col=8, row=19, port=str(11), name_w=name_w, tu_w=tu_w, fact_w=fact_w, status_w=status_w, head_h=head_h, pad_x=pad_x)
Headers(window, col=12, row=19, port=str(12), name_w=name_w, tu_w=tu_w, fact_w=fact_w, status_w=status_w, head_h=head_h, pad_x=pad_x)
Headers(window, col=16, row=19, port=str(13), name_w=name_w, tu_w=tu_w, fact_w=fact_w, status_w=status_w, head_h=head_h, pad_x=pad_x)
Headers(window, col=20, row=19, port=str(14), name_w=name_w, tu_w=tu_w, fact_w=fact_w, status_w=status_w, head_h=head_h, pad_x=pad_x)
Headers(window, col=24, row=19, port=str(15), name_w=name_w, tu_w=tu_w, fact_w=fact_w, status_w=status_w, head_h=head_h, pad_x=pad_x)
Headers(window, col=28, row=19, port=str(16), name_w=name_w, tu_w=tu_w, fact_w=fact_w, status_w=status_w, head_h=head_h, pad_x=pad_x)

window.mainloop()
