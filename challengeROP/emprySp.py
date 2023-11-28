from pwn import*


#p = remote("bin.training.offdef.it", 2014)
p = process("./emptyspaces")

gdb.attach(p,
'''
b read
''')

code = b"A"*64

input("WAIT")
p.send(code)

p.interactive()