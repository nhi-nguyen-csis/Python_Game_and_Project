import time

def get_number():
    while True:
        number_or_quit = input("Enter a starting number (greater than 0) or QUIT: ").lower()
        if number_or_quit.startswith('q'):
            return None
        if not number_or_quit.isdecimal() or number_or_quit == '0':
            continue
        else:
            number = int(number_or_quit)
            return number
def main():
    num = get_number()
    if not num:
        print("Goodbye!")
    else:
        print(f"{num} ", end='')
        while num != 1:
            if num % 2 == 0: # If n is even, the next number n is n / 2
                num //= 2
            else: # If n is odd, the next number n is n * 3 + 1
                num = 3 * num + 1
            time.sleep(0.09)
            print(f"{num} ", end='')



if __name__ == '__main__':
    main()