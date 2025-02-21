#!/usr/bin/python3
# Prints the ASCII alphabet in lowercase, excluding 'q' and 'e', without a newline

for char in range(97, 123):  # ASCII values for 'a' to 'z'
    if chr(char) not in {'q', 'e'}:  # Skip 'q' and 'e'
        print("{}".format(chr(char)), end="")
