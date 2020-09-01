import time


def loading():
    print("Loading:[" + "□"*25 + "]0%", end="\r")

    for j in range(26):
        print("Loading:[", end="")

        for i in range(j):
            print("■", end="")
            time.sleep(0.05)

        for t in range(25-j):
            print("□", end="")
            time.sleep(0.05)

        print("]", end="")
        print(str(4*j)+"%", end ='\r')

    print("\nLoading completed")


loading()