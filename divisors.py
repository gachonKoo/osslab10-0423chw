import sys

def find_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python divisors.py <number>")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        if num <= 0:
            raise ValueError("Number must be positive")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    result = find_divisors(num)
    print(" ".join(map(str, result)))
