import struct
def operator(a, b, c, d):
    s = "001{0:03b}{1:02b}{2:01b}{3:02b}".format(a, b, c, d)
    return struct.pack("<H", int(s+'0'*(16-len(s)), 2))
def copy(a, b, c):
    s = "0001{0:02b}{1:01b}{2:02b}".format(a, b, c)
    return struct.pack("<H", int(s+'0'*(16-len(s)), 2))
def push(a, b):
    s = "01{0:02b}{1:08b}".format(a, b)
    return struct.pack("<H", int(s+'0'*(16-len(s)), 2))
def print_stack(a):
    s = "00001{0:02b}".format(a)
    return struct.pack("<H", int(s+'0'*(16-len(s)), 2))
def pop(a, b):
    s = "000000{0:02b}{1:02b}".format(a, b)
    return struct.pack("<H", int(s+'0'*(16-len(s)), 2))
def jmp(a, b):
    s = "1{0:01b}{1:014b}".format(a, b)
    return struct.pack("<H", int(s+'0'*(16-len(s)), 2))
def cmp(a, b):
    s = "000001{0:02b}{1:02b}".format(a, b)
    return struct.pack("<H", int(s+'0'*(16-len(s)), 2))

f = open("cat.bin", "w+b")
out = b""

out+=copy(0, 0, 2)
out+=copy(0, 0, 2)
out+=pop(0, 2)

out+=copy(0, 1, 0)
out+=pop(0, 0)
out+=push(2, 0)
out+=push(2, 0)
out+=push(2, 0)
out+=push(2, 1)
out+=operator(1, 1, 1, 2)
out+=pop(2, 2)
out+=pop(1, 2)
out+=copy(0, 0, 2)
out+=pop(0, 2)
out+=cmp(1, 2)
out+=jmp(1, 13)

out+=pop(1, 2)

out+=print_stack(2)
out+=pop(2, 0)
out+=push(2, 0)
out+=push(2, 0)
out+=push(2, 0)
out+=push(2, 1)
out+=operator(1, 1, 1, 2)
out+=pop(2, 2)
out+=pop(1, 2)
out+=copy(0, 0, 2)
out+=pop(0, 2)
out+=cmp(1, 2)
out+=jmp(1, 13)

f.write(out)
