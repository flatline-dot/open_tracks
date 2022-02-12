import serial
import threading
from serial.tools.list_ports import comports
from interface import *


threading_result = []
sputnik_values = {
    1: 'GPS',
    2: 'ГЛН',
    3: 'ГЛН L2',
    101: 'ГЛН L1OCp',
    100: 'ГЛН L1OCd',
    102: 'ГЛН L1SCd',
    105: 'ГЛН L2OCp',
    104: 'ГЛН L2КСИ',
    106: 'ГЛН L2SCd',
    50: 'GPS L2C-L',
    34: 'GPS L2C-M'
    }

request = b''
for i in ('10', '39', '10', '03'):
    request += bytes.fromhex(i)


def valid_ports():
    return [i.device for i in comports()]



def check_connections(table_ports):
    active_ports = [i.device for i in comports()]
    for table in table_ports:
        if table.number in active_ports:
            table.title['background'] = 'yellow'
            table.title_label['background'] = 'yellow'


def parse_binr(port):
    com = serial.Serial(port=port)
    com.parity = serial.PARITY_ODD
    com.baudrate = 115200
    com.bytesize = serial.EIGHTBITS
    com.timeout = 1

    com.write(request)
    response = com.read(4000)
    response_clear = response.replace(bytes.fromhex('10') + bytes.fromhex('10'), bytes.fromhex('10'))
    print(len(response_clear))

    response_list_systems = []
    
    result = {}

    start = 2
    for _ in range(96):
        response_list_systems.append(int(response_clear[start:start + 1].hex(), 16))
        start += 20
    print(response_list_systems)
    
    result = {sputnik_values[sputnik]: response_list_systems.count(sputnik) for sputnik in sputnik_values}
    result['device'] = port
    
    threading_result.append(result)
    return result


def render():
    global threading_result
    for res in threading_result:
        for frame in window.frame_ports:
            if res['device'] == frame._name.upper():
                del res['device']
                frame.content = res
                frame['text'] = window.get_str(frame._name.upper(), res)
                break
    threading_result = []


def running():
    ports = valid_ports()
    
    for port in ports:
        thread_ = threading.Thread(target=parse_binr, args=[port])
        thread_.start()
        thread_.join()

    render()


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
    start = Button(frame_start, text='Старт', font='Times 10 bold', borderwidth=2, background='#d9e2fc', width=10, height=2, fg='blue')
    start.place(relx=0.5, rely=0.5, anchor='center')

    frame_stop = Frame(window, width=80, height=45, background='white')
    frame_stop.grid(columnspan=3, column=16, row=37, pady=HEAD_H, sticky='e')
    frame_stop.grid_propagate(False)
    start = Button(frame_stop, text='Cтоп', font='Times 10 bold', borderwidth=2, background='#d9e2fc', width=10, height=2, fg='blue', highlightbackground='blue')
    start.place(relx=0.5, rely=0.5, anchor='center')



    window.mainloop()
    
    
