import random

def main():
    return get_otp()


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
    OTP = []
    OTP_length = get_length()
    while OTP_length > len(OTP):
        otp_value = random.randint(0, 9)
        OTP.append(otp_value)
    
    return ''.join(map(str, OTP))


if __name__ == '__main__':
    print(main())