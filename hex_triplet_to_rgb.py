from datetime import datetime

def hex_to_rgb(hex_triplet:str):
    hex_triplet = hex_triplet.removeprefix("#").upper()
    r = hex_triplet[0:2]
    g = hex_triplet[2:4]
    b = hex_triplet[4:6]
    int_r = int(str(r),16)
    int_g = int(str(g),16)
    int_b = int(str(b), 16)
    return print(f"RGB of hex triplet #{hex_triplet}: rgb({int_r},{int_g},{int_b})")

def rgb_to_hex(r,g,b):
    if r > 255 or g > 255 or b > 255:
        raise ChildProcessError("fuck you")
    else:
        val_1 = hex(r).removeprefix("0x")
        val_2 = hex(g).removeprefix("0x")
        val_3 = hex(b).removeprefix("0x")
    return print(f"#{(str(val_1) + str(val_2) + str(val_3)).upper()}")

def rgb_to_hex_v2(list):
    r = list[0]
    g = list[1]
    b = list[2]
    if r > 255 or g > 255 or b > 255:
        raise ChildProcessError("fuck you")
    val_1 = hex(r).removeprefix("0x")
    val_2 = hex(g).removeprefix("0x")
    val_3 = hex(b).removeprefix("0x")
    return print(f"#{(str(val_1) + str(val_2) + str(val_3)).upper()}")

def func_speed(func,**kwargs):
    start = datetime.now()
    func(**kwargs)
    end = datetime.now()
    return print(end.microsecond - start.microsecond)

def speed(g):
    start = datetime.now()
    print(g)
    end = datetime.now()
    return print(end.microsecond - start.microsecond)

def read_speed(file):
    with open(file,"r") as read:
        start = datetime.now()
        for line in read:
            print(line)
        end = datetime.now()
        print(end.microsecond - start.microsecond)

if __name__ == "__main__":
    func_speed(rgb_to_hex,r=255,g=255,b=255)
    func_speed(rgb_to_hex_v2,list=[255,255,255])