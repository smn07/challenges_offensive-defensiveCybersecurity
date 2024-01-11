#!/bin/bash

# List of inputs
inputs=()
for ((i=32; i<=126; i++)); do
    char=$(printf "\\$(printf '%03o' "$i")")
    inputs+=("flag{packer${char}}")
done

# Iterate over inputs
for input in "${inputs[@]}"
do
    # Run gdb with necessary commands
    output=$(gdb -q -ex "file ./john" \
                  -ex "break *0xYourAddress" \
                  -ex "run $input" \
                  -ex "info registers eax" \
                  -ex "quit" 2>&1)

    echo "$output"

    # # Check if eax is 1
    # if echo "$output" | grep -q "eax 0x1"; then
    #     echo "Correct input: $input"
    # else
    #     echo "Incorrect input: $input"
    # fi
done