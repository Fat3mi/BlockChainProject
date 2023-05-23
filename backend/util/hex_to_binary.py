# سیدامید فاطمی - طراحی بلاک چین

#================================================> کتابخانه ها و فایل های مورد نیاز

from backend.util.crypto_hash import crypto_hash


#================================================> ایجاد دیکشنری از معادل های هگزادسیمال به باینری

HEX_TO_BINARY_TABLE = {
    '0': '0000' ,
    '1': '0001' ,
    '2': '0010' ,
    '3': '0011' ,
    '4': '0100' ,
    '5': '0101' ,
    '6': '0110' ,
    '7': '0111' ,
    '8': '1000' ,
    '9': '1001' ,
    'a': '1010' ,
    'b': '1011' ,
    'c': '1100' ,
    'd': '1101' ,
    'e': '1110' ,
    'f': '1111' ,
}

#================================================> تبدیل هش هگزادسیمال  به هش باینری

def hex_to_binary(hex_string):
    binary_string = ''

    for char in hex_string:
        binary_string += HEX_TO_BINARY_TABLE[char]

    return binary_string

def main():
    number = 1992
    hex_number = hex(number)[2:]
    print(f'hex number : {hex_number}')

    binary_number = hex_to_binary(hex_number)
    print(f'binary number : {binary_number}')

    orginal_number = int(binary_number, 2)
    print(f'orginal number : {orginal_number}')

    hex_to_binary_crypto_hash = hex_to_binary(crypto_hash('test-data'))
    print(f'binary crypto hash : {hex_to_binary_crypto_hash}')


#================================================> نمایش عدد ، باینری ، هگزادسیمال و هش درصورت اجرای مستقیم

if __name__ == "__main__":
    main()

