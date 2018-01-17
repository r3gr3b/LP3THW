# EX 15 from LP3THW

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
close(txt)

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
close(txt)