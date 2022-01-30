import serial
import threading
from serial.tools.list_ports import comports
import time
from frontend import Interface


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


def check_connections():
    for i in window.frame_ports:
        if i['text'] in valid_ports():
            i['background'] = 'yellow'
        else:
            i['background'] = 'white'



def parse_binr(port):
    com = serial.Serial(port=port)
    com.parity = serial.PARITY_ODD
    com.baudrate = 115200
    com.bytesize = serial.EIGHTBITS
    com.timeout = 1

    com.write(request)
    response = com.read(2000)

    response_list_systems = []
    result = {}

    start = 2
    for _ in range(96):
        response_list_systems.append(int(response[start:start + 1].hex(), 16))
        start += 20

    result = {sputnik_values[sputnik]: response_list_systems.count(sputnik) for sputnik in sputnik_values}
    result['device'] = port
    print(result)
    threading_result.append(result)
    return result


def render():
    for res in threading_result:
        for frame in window.frame_ports:
            if res['device'] == frame._name:
                del res['device']
                frame.content = res
                frame['text'] = window.get_str(frame._name, res)


def running():
    ports = valid_ports()
    print(ports)
    for port in ports:
        thread_ = threading.Thread(target=parse_binr, args=[port])
        thread_.start()
        thread_.join()

    render()


if __name__ == '__main__':
    window = Interface()
    window.create_frame()
    window.create_button(check_connections, running)
    window.mainloop()
    
    
