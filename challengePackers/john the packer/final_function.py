key = [0x4c, 0x0f, 0x00, 0x01, 0x16, 0x10, 0x07, 0x09, 0x38, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xdd, 0xe7, 0x6f, 0xa6, 0x1c, 0x00, 0x00, 0x00, 0xf8, 0xfc, 0x7a, 0x35, 0x27, 0x02, 0x00, 0x00, 0x15, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x54, 0x6c, 0x15, 0x5c, 0x6c, 0x01, 0x00, 0x00, 0xdd, 0xe7, 0x6f, 0xa6, 0x1c, 0x00, 0x00, 0x00, 0x66, 0xce, 0x3e, 0xe9, 0x9d, 0x00, 0x00, 0x00, 0x54, 0x6c, 0x15, 0x5c, 0x6c, 0x01, 0x00, 0x00, 0x54, 0x6c, 0x15, 0x5c, 0x6c, 0x01, 0x00, 0x00, 0x41, 0x42, 0x44, 0xf3, 0x56, 0x07, 0x00, 0x00, 0xc5, 0xa4, 0x60, 0x46, 0x01, 0x00, 0x00, 0x00, 0xdd, 0xe7, 0x6f, 0xa6, 0x1c, 0x00, 0x00, 0x00 ]

flag = [ord('-')]

for i in range(0, len(key)):
    flag.append(key[i] ^ flag[i])

print(''.join([chr(x) for x in flag]))

# flag = flag{packer-4_3-1337&-annoying______________________e}