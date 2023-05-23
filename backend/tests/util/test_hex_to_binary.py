# سیدامید فاطمی - طراحی بلاک چین

#================================================> کتابخانه ها و فایل های مورد نیاز

from backend.util.hex_to_binary import hex_to_binary

#================================================> تست صحت هش کننده هگزادسیمال به باینری

def test_hex_to_binary():
    orginal_number = 1371
    hex_number = hex(orginal_number)[2:]
    binary_number = hex_to_binary(hex_number)

    assert int(binary_number, 2) == orginal_number