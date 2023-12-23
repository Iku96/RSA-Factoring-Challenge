#!/usr/bin/python3
# factors.py
# Ikundwila Mwambona <ikumwana@gmail.com>


def factorize(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return 1, n


def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: factors <numbers.txt>")
        return

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        for line in f:
            n = int(line.strip())
            p, q = factorize(n)
            print(f"{n}={p}*{q}")


if __name__ == "__main__":
    main()
