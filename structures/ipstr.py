import ctypes import *
import struct
class ip(strueture):
    _field_ ==[
        ("version",c_ubite,4), #c type unsing bite(without - or +)
        ("ihl",c_ubite,4),#ip heder length
        ("tos",c_ubite), #ip hedear ekak thina okama tika 
        ("un",c_ushort),
        ("len",c_ushort),
        ("id",c_ushort),
        ("offset",c_ushort),
        ("ttl",c_ubite),
        ("protocall",c_ubite),
        ("sum",c_ushort),
        ("src",c_unit32),
        ("dst",c_unit32),
        ]
        
def __new__(self,socket_buffer=None):

    return self.from_buffer_copy(socket_buffer)




def __init__(self,socket_buffer=None):

    self.src_address=socket.init_ntoa(struct.pack("@I",self.src))
    self.dst_address=socket.init_ntoa(struct.pack("@I",self.dst))
                                      
                                      
  
