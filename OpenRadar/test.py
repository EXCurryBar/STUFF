import mmwave as mm
import socket
from mmwave.dataloader import DCA1000
from mmwave.dataloader.radars import TI
try:
    dca = TI()
    adc_data = dca._read_buffer()
    radar_cube = mm.dsp.range_processing(adc_data)
except socket.error as serror: 
    print("Error: ", serror)
