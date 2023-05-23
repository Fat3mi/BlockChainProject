# سیدامید فاطمی - طراحی بلاک چین

#================================================> کتابخانه ها و فایل های مورد نیاز

import hashlib
import json

#================================================> 

def crypto_hash(*args):
    """
   sha256 هش کردن با استفاده از الگوریتم  
   UTF-8 و استفاده از انکدینگ 
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))

    joined_data = ''.join(stringified_args)

    return hashlib.sha256(joined_data.encode('UTF-8')).hexdigest()

#================================================> نمایش هش درصورت اجرای مستقیم

def main():
    print(f"crypto_hash(1): {crypto_hash(1,['omid','ali'],'two')}")
    print(f"crypto_hash(1): {crypto_hash('two',['omid','ali'],1)}")


if __name__ == '__main__':
    main()









