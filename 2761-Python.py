import struct
import re
while True:
    try:
        entrada = input().split(" ", 3)
        a = entrada[0]
        b = entrada[1]
        b = struct.unpack('f', struct.pack('f', float(b)))[0]
        c = entrada[2]
        d = entrada[3][:50]
        print(str(a) + f"{b:.6f}" + c + d)
        print(f"{a}\t{b:.6f}\t{c}\t{d}")
        print("%10d%10.6f%10c%10s" % (int(a), b, c, d))

    except EOFError:
        break



