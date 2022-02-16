import serial
from concurrent.futures import ThreadPoolExecutor
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

        self.request = bytearray()
        for code in ('10', '39', '01', '10', '03'):
            self.request.append(int(code, 16))

    def check_connections(self):
        self.active_names = []
        access_ports = [i.device for i in comports()]
        for port in access_ports:
            com = serial.Serial(port=port)
            com.parity = serial.PARITY_ODD
            com.baudrate = 115200
            com.bytesize = serial.EIGHTBITS
            com.timeout = 1

            com.write(self.request)
            if com.in_waiting:
                self.active_names.append(port)
                com.reset_input_buffer()
                com.__del__()

            else:
                com.__del__()

        for port in Table.table_ports:
            if port.number in self.active_names:
                port.title['background'] = 'yellow'
                port.title_label['background'] = 'yellow'

    def init_comports(self):
        active_ports = []
        if self.active_names:
            for name in self.active_names:
                com = serial.Serial(port=name)
                com.parity = serial.PARITY_ODD
                com.baudrate = 115200
                com.bytesize = serial.EIGHTBITS
                com.timeout = 1

                active_ports.append(com)

        else:
            self.check_connections()
            for name in self.active_names:
                com = serial.Serial(port=name)
                com.parity = serial.PARITY_ODD
                com.baudrate = 115200
                com.bytesize = serial.EIGHTBITS
                com.timeout = 1

                active_ports.append(com)

        return active_ports
