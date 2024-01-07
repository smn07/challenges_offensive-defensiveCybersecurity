BINARY_BASE = 0x0
ghidra_base = 0x00100000
ghidra_patch = 0x001011cd
start = ghidra_patch - ghidra_base

def patchBinary(binary, patch_file, address):
    with open(patch_file, 'rb') as f:
        patch = f.read()
    
    offset = address - BINARY_BASE
    patch_len = len(patch)
    binary = binary[:offset] + patch + binary[offset + patch_len:]
    return binary


with open('./patched_dynamism', 'rb') as f:
    binary = f.read()

binary = patchBinary(binary, './first', start)

with open('./patched_dynamism1', 'wb') as f:
    f.write(binary)