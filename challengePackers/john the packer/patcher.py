BINARY_BASE = 0x0
ghidra_base = 0x00100000
ghidra_breakpoint = 0x0010136f
start = ghidra_breakpoint - ghidra_base

def patchBinary(binary, patch_file, address):
    with open(patch_file, 'rb') as f:
        patch = f.read()
    
    offset = address - BINARY_BASE
    patch_len = len(patch)
    binary = binary[:offset] + patch + binary[offset + patch_len:]
    return binary


with open('./chall', 'rb') as f:
    binary = f.read()

binary = patchBinary(binary, './patch', start)

with open('./patched_chall', 'wb') as f:
    f.write(binary)