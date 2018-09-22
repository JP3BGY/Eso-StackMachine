import struct
outstr = "Hello World!\n"
out = b""
for i in outstr[::-1] :
    out+=struct.pack("<H", int("0100"+"{0:08b}".format(ord(i))+"0000", 2))

print(out)

a = open("HW.bin", "w+b")
a.write(out)
out = b""
for i in outstr:
    out+=struct.pack("<H", int("0000100000000000", 2))
    out+=struct.pack("<H", int("0000000000000000", 2))
a.write(out)

