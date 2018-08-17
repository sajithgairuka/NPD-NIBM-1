import ctypes import *
import struct

class udp(strueture):
    _fields_=[
        ("src", c_ushort),
        ("dest", c_ushort),
        ("length", c_short),
        ("checksum", c_short),
        ]
    
def __new__(self,socket_buffer=None):
    return self.from_buffer_copy(socket_buffer)




def __init__(self,socket_buffer=None):
    self.src_address=socket.init_ntoa(struct.pack("@I",self.src))
    self.dest_address=socket.init_ntoa(struct.pack("@I",self.dest))
    
