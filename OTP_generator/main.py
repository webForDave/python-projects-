import random

def main():
    ...


def get_length():
    while True:
        try:
            OTP_length = int(input('OPT length (4, 6, 8): ').strip())
            if type(OTP_length) != int or OTP_length not in [4, 6, 8]:
                raise ValueError
            return OTP_length
        except ValueError:
            break  


def get_otp():
    ...


if __name__ == '__main__':
    print(main())