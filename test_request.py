from serial import Serial, PARITY_ODD
from time import sleep
com = Serial(port='COM3')
com.baudrate = 115200
#com.parity = PARITY_ODD

psi_mode = bytearray([16, 221, 1, 16, 3])
binr_mode = '$PORZA,0,115200,3*7E\r\n'.encode('ascii')


com.write(psi_mode)