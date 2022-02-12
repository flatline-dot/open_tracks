import serial
import threading
from serial.tools.list_ports import comports
from interface import *


threading_result = []
sputnik_values = {
    'gln_l1of': 2,
    'gln_l1sf': 5 ,
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

request = bytearray()
for code in ('10', '39', '10', '03'):
    request.append(int(code, 16))


def valid_ports():
    return [i.device for i in comports()]



def check_connections(table_ports):
    active_ports = (i.device for i in comports())
    for table in table_ports:
        if table.number in active_ports:
            table.title['background'] = 'yellow'
            table.title_label['background'] = 'yellow'


def parse_binr(table_port):
    com = serial.Serial(port=table_port.number)
    com.parity = serial.PARITY_ODD
    com.baudrate = 115200
    com.bytesize = serial.EIGHTBITS
    com.timeout = 1
    stop_read = bytearray([int('10', 16), int('03', 16)])

    com.write(request)
    
    response = com.read_until(stop_read)
    response_clear = response.replace(bytes.fromhex('10') + bytes.fromhex('10'), bytes.fromhex('10'))
    print(len(response_clear))
    code_list = []   
    count_results = {}

    start = 2
    for _ in range(96):
        code_list.append(int(response_clear[start:start + 1].hex(), 16))
        start += 20
    
    count_results = {sputnik: code_list.count(sputnik_values[sputnik]) for sputnik in sputnik_values}
       

    for result in count_results:
        if getattr(table_port, result + '_status')['background'] != 'green':

            fact = getattr(table_port, result + '_fact')
            fact['text'] = count_result[result]

            #if int(getattr(table_port, result + '_tu')['text']) - int(getattr(table_port, result + '_fact')) <= 2:
                #   status = getattr(table_port, result + '_status')
                #  status['background'] == 'green'
        else:
            continue


def running():
    active_ports = [i.device for i in comports()]
    table_ports = [port for port in Table.table_ports if port.number in active_ports]
    
    for table_port in table_ports:
        thread_ = threading.Thread(target=parse_binr, args=[port])
        thread_.start()
        thread_.join()



if __name__ == '__main__':
    Table(window, col=0, row=0, port='COM1')
    Table(window, col=4, row=0, port='COM2', pad_x=PAD_X)
    Table(window, col=8, row=0, port='COM3', pad_x=PAD_X)
    Table(window, col=12, row=0, port='COM4', pad_x=PAD_X)
    Table(window, col=16, row=0, port='COM5', pad_x=PAD_X)
    Table(window, col=20, row=0, port='COM6', pad_x=PAD_X)
    Table(window, col=24, row=0, port='COM7', pad_x=PAD_X)
    Table(window, col=28, row=0, port='COM8', pad_x=PAD_X)
    Table(window, col=0, row=19, port='COM9')
    Table(window, col=4, row=19, port='COM10', pad_x=PAD_X)
    Table(window, col=8, row=19, port='COM11', pad_x=PAD_X)
    Table(window, col=12, row=19, port='COM12', pad_x=PAD_X)
    Table(window, col=16, row=19, port='COM13', pad_x=PAD_X)
    Table(window, col=20, row=19, port='COM14', pad_x=PAD_X)
    Table(window, col=24, row=19, port='COM15', pad_x=PAD_X)
    Table(window, col=28, row=19, port='COM16', pad_x=PAD_X)

    frame_check = Frame(window, width=120, height=45, background='white')
    frame_check.grid(columnspan=4, column=10, row=37, pady=HEAD_H, sticky='we')
    frame_check.grid_propagate(False)
    check_conection = Button(frame_check, text='Проверка соединения', font='Times 10 bold', borderwidth=2, background='#d9e2fc', width=20, height=2, fg='blue', command=lambda: check_connections(Table.table_ports))
    check_conection.place(relx=0.5, rely=0.5, anchor='center')

    frame_start = Frame(window, width=80, height=45, background='white')
    frame_start.grid(columnspan=3, column=14, row=37, pady=HEAD_H)
    frame_start.grid_propagate(False)
    start = Button(frame_start, text='Старт', font='Times 10 bold', borderwidth=2, background='#d9e2fc', width=10, height=2, fg='blue', command=running)
    start.place(relx=0.5, rely=0.5, anchor='center')

    frame_stop = Frame(window, width=80, height=45, background='white')
    frame_stop.grid(columnspan=3, column=16, row=37, pady=HEAD_H, sticky='e')
    frame_stop.grid_propagate(False)
    start = Button(frame_stop, text='Cтоп', font='Times 10 bold', borderwidth=2, background='#d9e2fc', width=10, height=2, fg='blue', highlightbackground='blue')
    start.place(relx=0.5, rely=0.5, anchor='center')



    window.mainloop()
    
    
