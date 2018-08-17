import argparse           # before working this program refer to" work with this python program.pdf "
import binascii

p=argparse.ArgumentParser()
p.add_argument("-o","--file",required=True) # command py hexa.py -o (file)with extention
args = p.parse_args()

def bind(x):
    return(x[b:b+4] for b in range (0,len(x),4))#div-->x[b:b+4] get hexa values into x and dividing 4bit{for b in range (0,len(x),4)},get fist 4 bit in x([b:b+4]) 

def xxd():
    try:
        file=open(args.file,"r")

    except IOError:
        print('An error occured trying to read the file.')
        quit()

    noline=0
    line=0
    leng=0
    c=0
    fread=file.read()
    repls=fread.replace(" ",".")
    repls=fread.replace("\n",".")
    hexa=binascii.hexlify(fread.encode("utf-8")).decode("utf-8")

    
    leng=int(len(fread))
    if leng <16:
        line=1

    else:
        line=leng/16 + 1

    for y in range(int(line)):
        div=hexa[c:c+32]#([c:c+32])bit 32 issarha thina ewa gannawa,divide hexa value in to 32 bit using([c:c+32])
        stri=repls[c:c+16]#replace karapuwa 16 bit kotas walata kadanawa
        
        wri="{:#08x}".format(noline)+ " : "
        wri+=" ".join(bind(div))
        wri+="   " + stri  
        noline=noline+16
        c=c+16

        print(wri)

xxd()

        
        
        
    
            
