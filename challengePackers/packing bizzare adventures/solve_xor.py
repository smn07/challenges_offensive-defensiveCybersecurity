# i have the equation x ^ a = b to solve for x

# from the first patch
# a = [0xb4, 0xaf, 0x73, 0xec, 0x5b, 0x21, 0x8a, 0x98, 0xcf, 0x45, 0xf2, 0x65, 0xcb, 0xe5, 0x48, 0xef]
# b = [0xd2, 0xc3, 0x12, 0x8b, 0x20, 0x58, 0xba, 0xed, 0xbd, 0x1a, 0x9c, 0x56, 0xb3, 0x91, 0x17, 0x9c]

#from the second patch
a_first = 0xa0e9997a1f26e55d
a_second = 0xf997be04d7255ecb

# transform a_first and a_second in a list of bytes
a = []
for i in range(8):
    a.append(a_first & 0xff)
    a_first >>= 8
for i in range(8):
    a.append(a_second & 0xff)
    a_second >>= 8

b_first = 0x8e9aa8252c50896d
b_second = 0x84e18d69e05c70e5

# transform b_first and b_second in a list of bytes
b = []
for i in range(8):
    b.append(b_first & 0xff)
    b_first >>= 8
for i in range(8):
    b.append(b_second & 0xff)
    b_second >>= 8

for i in range(len(a)):
    x = a[i] ^ b[i]
    print(chr(x), end='')

# flag = 'flag{y0ur_n3xt_s0lv3_1s...y7m3v}'