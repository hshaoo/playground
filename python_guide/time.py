import time


def main():

    # worst
    start = time.time()
    nums = ""
    for n in range(20):
        nums += str(n)  
    # print(nums)
    stop = time.time()
    print(str(stop-start) + "s")

    # good
    start = time.time()
    nums = []
    for n in range(20):
        nums.append(str(n))
    # print ("".join(nums))
    stop = time.time()
    print(str(stop-start)+"s")

    # better
    start = time.time()
    nums = [str(n) for n in range(20)]
    # print("".join(nums))
    stop = time.time()
    print(str(stop - start) + "s")

    # best
    start = time.time()
    nums = map(str, range(20))
    # print("".join(nums))
    stop = time.time()
    print(str(stop - start) + "s")


main()
