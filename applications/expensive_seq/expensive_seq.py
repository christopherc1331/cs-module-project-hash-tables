# Your code here

my_dict = {}


def expensive_seq(x, y, z):
    # Your code here
    check_key = (x, y, z)

    if check_key in my_dict:
        return my_dict[check_key]
    else:
        v = None
        if x <= 0:
            v = y + z
        else:
            v = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + \
                expensive_seq(x-3, y+3, z*3)

        my_dict[check_key] = v

        return v


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
