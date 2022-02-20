import serial
from concurrent.futures import ThreadPoolExecutor, as_completed
from serial.tools.list_ports import comports
import time
from interface import *


class ParsingComports():
    def __init__(self):
        self.sputnik_values = {

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

        self.request = bytearray([16, 57, 1, 16, 3])
        self.check_request = bytearray([16, 57, 16, 3])
        self.stop_request = bytearray([16, 14, 16, 3])
        self.active_names = []
        self.active_ports = []
        self.is_run = True

    def check_connections(self):
        instance_ports = []
        access_ports = [i.device for i in comports()]
        print(access_ports)
        
        for port in access_ports:
            com = serial.Serial(port=port)
            com.parity = serial.PARITY_ODD
            com.baudrate = 115200
            com.bytesize = serial.EIGHTBITS
            com.timeout = 1

            com.write(self.check_request)
            instance_ports.append(com)

        time.sleep(1)
        for com in instance_ports:
            if com.in_waiting:
                self.active_names.append(com.port)
                com.reset_input_buffer()

        for i in instance_ports:
            i.__del__()       
        for port in Table.table_ports:
            if port.number in self.active_names:
                port.title['background'] = 'yellow'
                port.title_label['background'] = 'yellow'
            else:
                port.title['background'] = 'white'
                port.title_label['background'] = 'white'
        print(self.active_names)

    def init_comports(self):

        if self.active_names:
            for name in self.active_names:
                com = serial.Serial(port=name)
                com.parity = serial.PARITY_ODD
                com.baudrate = 115200
                com.bytesize = serial.EIGHTBITS
                com.timeout = 1

                self.active_ports.append(com)

        else:
            self.check_connections()
            for name in self.active_names:
                com = serial.Serial(port=name)
                com.parity = serial.PARITY_ODD
                com.baudrate = 115200
                com.bytesize = serial.EIGHTBITS
                com.timeout = 1

                self.active_ports.append(com)

        return self.active_ports

    def read_binr(self, com):
        response = b''
        while True:
            if com.in_waiting and com.in_waiting > 3:
                response += com.read(com.in_waiting)

                if (response[-1] == 3) and (response[-2] == 16) and (response[-3] != 16) and (len(response) >= 1924):
                    com.reset_input_buffer()
                    return (com.port, response)

    def parse_binr(self, com_response):
        com, response = com_response
        code_list = []
        response_clear = response.replace(bytes.fromhex('10') + bytes.fromhex('10'), bytes.fromhex('10'))

        start = 2
        for _ in range(96):
            code_list.append(int(response_clear[start:start + 1].hex(), 16))
            start += 20
        
        count_results = {sputnik: code_list.count(self.sputnik_values[sputnik]) for sputnik in self.sputnik_values}

        return (com, count_results)

    def rendering(self, com_results):
        com, results = com_results
        for table_port in Table.table_ports:
            if com == table_port.number:
                for result in results:
                    fact = getattr(table_port, result + '_fact')
                    fact['text'] = results[result]
                    status = getattr(table_port, result + '_status')

                    if int(getattr(table_port, result + '_tu')['text']) - int(fact['text']) <= 2 and int(fact['text']) != 0:
                        frame = getattr(table_port, result + '_status_frame')
                        frame['background'] = '#1db546'
                        status['background'] = '#1db546'
                    else:
                        frame = getattr(table_port, result + '_status_frame')
                        frame['background'] = '#ed1818'
                        status['background'] = '#ed1818'
   
def start():
    comport.is_run = True
    active_ports = comport.init_comports()
    [port.write(comport.request) for port in active_ports]

    def running():
        if comport.is_run:
            read_results = [comport.read_binr(port) for port in active_ports]
            parse_results = [comport.parse_binr(port) for port in read_results]
            [comport.rendering(port) for port in parse_results]
            Tk.after(window, 100, running)
        
    running()


def stop():
    comport.is_run = False
    for port in comport.active_ports.copy():
        port.write(comport.stop_request)
        port.reset_input_buffer()
        comport.active_ports.remove(port)
        del port
    
    print('Stop')


if __name__ == '__main__':
    comport = ParsingComports()
    
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
    check_conection = Button(frame_check, text='Проверка соединения', font='Times 10 bold', borderwidth=2, background='#d9e2fc', width=20, height=2, fg='blue', command=comport.check_connections)
    check_conection.place(relx=0.5, rely=0.5, anchor='center')

    frame_start = Frame(window, width=80, height=45, background='white')
    frame_start.grid(columnspan=3, column=14, row=37, pady=HEAD_H)
    frame_start.grid_propagate(False)
    start = Button(frame_start, text='Старт', font='Times 10 bold', borderwidth=2, background='#d9e2fc', width=10, height=2, fg='blue', command=start)
    start.place(relx=0.5, rely=0.5, anchor='center')

    frame_stop = Frame(window, width=80, height=45, background='white')
    frame_stop.grid(columnspan=3, column=16, row=37, pady=HEAD_H, sticky='e')
    frame_stop.grid_propagate(False)
    start = Button(frame_stop, text='Cтоп', font='Times 10 bold', borderwidth=2, background='#d9e2fc', width=10, height=2, fg='blue', command=stop)
    start.place(relx=0.5, rely=0.5, anchor='center')

    window.mainloop()
    
