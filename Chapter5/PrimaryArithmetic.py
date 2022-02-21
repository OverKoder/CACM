import sys


def main():

    for line in sys.stdin:
        a, b = [int(n) for n in line.split()]
        if a == 0 and b == 0:
            continue
        carry = 0
        carry_count = 0
        while (a > 0 or b > 0):
            a_digit, b_digit = a % 10 ,  b % 10
            a, b = a // 10, b // 10
            aux = a_digit + b_digit + carry
            carry = aux // 10
            carry_count += carry
        
        if carry_count == 0:
            print("No carry operation.")
        elif carry_count == 1:
            print(carry_count, "carry operation.")
        else:
            print(carry_count, "carry operations.")

if __name__ == "__main__":
    main()