import serial
import threading
import queue
from serial.tools.list_ports import comports
import time



list_comports = [i.device for i in comports()]

queued = queue.Queue()

sputnik_values = {
    1: 'GPS',
    2: 'CLN',
    3: 'GLN L2',
    33: 'GLN L2',
    4: 'SBAS',
    5: 'GLN PC',
    17: 'GLN PC',
    6: 'GLN L2 PC',
    49: 'GLN L2 PC',
    8: 'Galileo E1B',
    24: 'Galileo E1C',
    40: 'Galileo E5a Data',
    56: 'Galileo E5a Pilot',
    72: 'Galileo E5b Data',
    88: 'Galileo E5b Pilot',
    65: 'GLN 3D',
    81: 'GLN 3P',
    193: 'GLN L3_T',
    130: 'GPS_T',
    129: 'GLN_T',
    161: 'GLN L2_T',
    162: 'GPS L2_T',
    34: 'GPS L2C-M',
    50: 'GPS L2C-L',
    194: 'GPS L5_T',
    66: 'GPS L5i',
    82: 'GPS L5q',
    68: 'SBAS L5i',
    84: 'SBAS L5q',
    9: 'BDS B1I'
    }

request = b''
for i in ['10', '39', '10', '03']:
    request += bytes.fromhex(i)


def parse_binr(port, request, queued):
    com = serial.Serial(port=port)
    com.parity = serial.PARITY_ODD
    com.baudrate = 115200
    com.bytesize = serial.EIGHTBITS
    com.timeout = 5

    systems_result = []
    channals = {'device': port}
    com.write(request)
    
    response = com.read(2000)
    
    start = 2
    for _ in range(96):
        systems_result.append(response[start:start + 1])
        start += 20

    # channals_test = [int(i.hex(), 16) for i in result]
    

    for num, system in enumerate(systems_result):
        if int(system.hex(), 16) in sputnik_values:
            channals[num + 1] = sputnik_values[int(system.hex(), 16)]
        else:
            channals[num + 1] = 'Выкл.'
            
    queued.put(channals)
    return channals


def running(list_comports, request, queued):
    for port in list_comports:
        thread_ = threading.Thread(target=parse_binr, args=(port, request, queued))
        thread_.start()
        thread_.join()
    

    
if __name__ == '__main__':
    #for port in list_comports:
        #res = parse_binr(port, request)
        #for num, sput in enumerate(res):
            #print(num + 1, sputnik_values.setdefault(sput, 'Выкл'))
    start = time.time()
    running(list_comports, request, queued)
    print(queued.get())
    end = time.time()
    print(end - start)
    
    
