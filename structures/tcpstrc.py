import ctypes import *
import struct

class tcp(structure):
    _fields_=[
        ("src", c_ushort),
        ("dest", c_ushort),
        ("seq_no", c_long),
        ("ack_no", c_long),
        ("offset", c_ubyte),
        ("reserved", c_ubyte),
        ("flag",  c_ubyte),
        ("window", c_ushort),
        ("checksum", c_ushort),
        ("urg_point", c_ushort),
        ]
    
def __new__(self,socket_buffer=None):

    return self.from_buffer_copy(socket_buffer)




def __init__(self,socket_buffer=None):
    

    self.src_address=socket.init_ntoa(struct.pack("@I",self.src))
   
    self.dest_address=socket.init_ntoa(struct.pack("@I",self.dest))

