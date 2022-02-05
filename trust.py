from tkinter import *

window = Tk()
size_width = window.winfo_screenwidth()
size_height = window.winfo_screenheight()
window.wm_state('zoomed')
#window.geometry(f"{size_width}x{size_height}")
print(size_width * 0.3)

class Headers():
    def __init__(self, window, size_width, col, pad):
        self.title = Frame(window, height=3, borderwidth=1, relief=RAISED)
        self.title.grid(row=0, column=col, columnspan=4, sticky='ew')
        self.title_label = Label(self.title, text='COM', borderwidth=1, width=4)
        self.title_label.grid()


        self.frame_names = Frame(window, height=5, relief=RAISED, borderwidth=1)
        self.frame_names.grid(column=0 + col, row=1, sticky='e')
        self.label_names = Label(self.frame_names, text='Диапозон', borderwidth=1, font=f'Times {int(size_width * 0.00625)}', width=int(size_width * 0.0087), height=2,
                            background='silver', )
        self.label_names.grid()

        self.frame_const = Frame(window, height=5, relief=RAISED, borderwidth=1)
        self.frame_const.grid(row=1, column=1 + col,)
        self.label_const = Label(self.frame_const, text='ТУ', borderwidth=1, font=f'Times {int(size_width * 0.00625)}', width=int(size_width * 0.0022), height=2,
                            background='silver', )
        self.label_const.grid()

        self.frame_count = Frame(window, height=5, relief=RAISED, borderwidth=1)
        self.frame_count.grid(row=1, column=2 + col)
        self.frame_count = Label(self.frame_count, text='Факт.', borderwidth=1, font=f'Times {int(size_width * 0.00625)}', width=int(size_width * 0.003), height=2,
                            background='silver')
        self.frame_count.grid()

        self.frame_status = Frame(window, height=5, relief=RAISED, borderwidth=1)
        self.frame_status.grid(row=1, column=3 + col)
        self.label_status = Label(self.frame_status, text='Cтатус', borderwidth=1, font=f'Times {int(size_width * 0.00625)}', width=int(size_width * 0.0037), height=2,
                             background='silver')
        self.label_status.grid()




Headers(window, size_width, 0, 0)
Headers(window, size_width, 4, 5)
Headers(window, size_width, 8, 5)
Headers(window, size_width, 12, 5)
Headers(window, size_width, 16, 5)
Headers(window, size_width, 20, 5)
Headers(window, size_width, 24, 5)
Headers(window, size_width, 28, 5)

window.mainloop()
