from unittest import TestCase, main
import sys
import os

from run_module.review_model import ParsingComports

sys.path.append(os.path.abspath('run_module'))

from review_model import *


class InfoTracksReadTest(TestCase):
    def test_info_read(self):
        com = Serial(port='COM1')
        com.parity = PARITY_ODD
        com.baudrate = 115200
        com.bytesize = EIGHTBITS
        com.timeout = 1
        com.warm_request = False
        com.vector_status = False
        self.assertEqual(comport.info_tracks_read(com), (com, False))

    def test_info_read_warm(self):
        com = Serial(port='COM1')
        com.parity = PARITY_ODD
        com.baudrate = 115200
        com.bytesize = EIGHTBITS
        com.timeout = 1
        com.warm_request = True
        com.vector_status = False
        com.warm_restart_start = 0
        self.assertEqual(comport.info_tracks_read(com), (com, False))

    def test_info_read_warm_time(self):
        com = Serial(port='COM1')
        com.parity = PARITY_ODD
        com.baudrate = 115200
        com.bytesize = EIGHTBITS
        com.timeout = 1
        com.warm_request = True
        com.vector_status = False
        com.warm_restart_start = time()
        self.assertEqual(comport.info_tracks_read(com), (com, False))

    def test_info_read_reqiest(self):
        comport = ParsingComports()
        com = Serial(port='COM1')
        com.parity = PARITY_ODD
        com.baudrate = 115200
        com.bytesize = EIGHTBITS
        com.timeout = 1
        com.warm_request = False
        com.vector_status = False
        com.warm_restart_start = time()
        com.write(comport.check_request)
        sleep(1)
        self.assertEqual(comport.info_tracks_read(com)[-3:], bytearray([]))
        self.assert
if __name__ == '__main__':
    main()