import serial
from concurrent.futures import ThreadPoolExecutor
from serial.tools.list_ports import comports
import time
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
for code in ('10', '39', '01', '10', '03'):
    request.append(int(code, 16))


def check_connections(table_ports):
    active_ports = [i.device for i in comports()]
    for table in table_ports:
        if table.number in active_ports:
            table.title['background'] = 'yellow'
            table.title_label['background'] = 'yellow'


def ports_init(name):
    com = Serial(port=name)
    com.parity = serial.PARITY_ODD
    com.baudrate = 115200
    com.bytesize = serial.EIGHTBITS
    com.timeout = 1
    return com


def read_binr(com):
    while True:
        response = b''
        start = time.time()
        if com.in_waiting:    
            while True:
                byte = com.read()
                if (byte == bytes.fromhex('03')) and (response[-1] == 16) and (response[-2] != 16):
                    response += byte
                    break
                else:
                    response += byte
            end = time.time()
            res = end - start
            print(len(response))
            print(res)
            return (com, response)
            
        else:
            return None
    

def parse_binr(com_response):
    start_s = time.time()
    com, response = com_response
    code_list = []
    response_clear = response.replace(bytes.fromhex('10') + bytes.fromhex('10'), bytes.fromhex('10'))

    start = 2
    for _ in range(96):
        code_list.append(int(response_clear[start:start + 1].hex(), 16))
        start += 20
    
    count_results = {sputnik: code_list.count(sputnik_values[sputnik]) for sputnik in sputnik_values}
    time.sleep(3)
    end = time.time()
    
    res = end - start_s
    print(res)
    return (com, count_results)


def rendering(com_results):
    com, results = com_results
    for table_port in Table.table_ports:
        if com.port == table_port.number:
            for result in results:
                fact = getattr(table_port, result + '_fact')
                fact['text'] = results[result]
                status = getattr(table_port, result + '_status')

                if int(getattr(table_port, result + '_tu')['text']) - int(fact['text']) <= 2 and int(fact['text']) != 0:
                    status['background'] = '#1db546'
                else:
                    status['background'] = '#ed1818'
        break



def running():
    listen_ports = [i.device for i in comports()]
    active_ports = [ports_init(port) for port in listen_ports]
    print(listen_ports)
    print(active_ports)
    [port.write(request) for port in active_ports]
    read_results = []
    parse_results = []
    while True:
        with ThreadPoolExecutor(len(active_ports)) as executor:
            features = [executor.submit(read_binr, port) for port in active_ports]
            for feature in features:
                read_results.append(feature.result())
                
        
            

        with ThreadPoolExecutor(len(active_ports)) as executor:
            features = [executor.submit(parse_binr, port) for port in read_results]
            for feature in features:
                parse_results.append(feature.result())

        print(parse_results)
        break
        #for port in parse_results:
            #rendering(port)


#def running():
#    active_ports = [i.device for i in comports()]
#    table_ports = [port for port in Table.table_ports if port.number in active_ports]
#    
#    for table_port in table_ports:
#        thread_ = threading.Thread(target=parse_binr, args=[table_port])
#        thread_.start()
#        #thread_.join()



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
    
    
