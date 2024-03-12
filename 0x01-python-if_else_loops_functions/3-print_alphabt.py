#!/usr/bin/python3
for letter in range(97, 123):
    character = chr(letter)
    if character == 'q' or character == 'e':
        continue
    print(f"{character}", end = "")
