import sys


def main():
    cases = int(input())
    for case in range(cases):

        number_str = sys.stdin.readline()[:-1]
        reverse = number_str[::-1]
        number = int(number_str)
        pal_counter = 0

        while(True):
            number += int(reverse)
            pal_counter += 1
            number_str = str(number)
            reverse = number_str[::-1]
            if number_str == reverse:
                break



        print(pal_counter, number)

        
    return

if __name__ == "__main__":
    main()