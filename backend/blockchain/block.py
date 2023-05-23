# سیدامید فاطمی - طراحی بلاک چین

# ================================================> کتابخانه ها و فایل های مورد نیاز

import time
from backend.util.crypto_hash import crypto_hash
from backend.util.hex_to_binary import hex_to_binary
from backend.config import MINE_RATE

# ================================================> اطلاعات اولین بلوک اطلاعات

GENESIS_DATA = {
    'timestamp': 1,
    'last_hash': 'genesis_last_hash',
    'hashed': 'genesis_hash',
    'data': [],
    'difficulty': 3,
    'nonce': 'genesis_nonce'
}

# ================================================> تولید بلوک اطلاعات


class Block:
    """
    محل نگهداری اطلاعات 
    و محلی برای نگهداری تراکنس ها
    """

    def __init__(self, timestamp, last_hash, hashed, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hashed = hashed
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce
    
    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hashed: {self.hashed}, '
            f'data: {self.data}, '
            f'difficulty: {self.difficulty}, '
            f'nonce: {self.nonce}) '
        )
    
    # برای مقایسه دو شی (بصورت دیکشنری)
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def to_json(self):
        """
        سریالایز کردن بلوک بصورت دیکشنری برای استفاده در ای پی آی
        """
        return self.__dict__

    @staticmethod  
    def mine_block(last_block, data):
        """
        ماینینگ بلاک بر اساس هش قبلی و دیتا تا هش بلاک به 0 برسد
        """
        timestamp = time.time_ns()
        last_hash = last_block.hashed
        difficulty = Block.adjust_difficulty(last_block, timestamp)
        nonce = 0
        hashed = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        while hex_to_binary(hashed)[0:difficulty] != '0' * difficulty:
            nonce += 1
            timestamp = time.time_ns()
            difficulty = Block.adjust_difficulty(last_block, timestamp)
            hashed = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        return Block(timestamp, last_hash, hashed, data, difficulty, nonce)

    @staticmethod
    def genesis():
        """
        ساخت اولین بلاک (بلاک مادر)
        """
        return Block(**GENESIS_DATA)

    @staticmethod
    def adjust_difficulty(last_block, new_timestamp):
        """
        تنظیم سختی شبکه بر اساس میانگین سرعت ماینینگ 
        اگر بلاک سریع تر ماین شد سختی افزایش پیدا میکند 
        اگر بلاک کند تر ماین شد سختی کاهش پیدا میکند 
        """
        if (new_timestamp - last_block.timestamp) < MINE_RATE:
            return last_block.difficulty + 1

        if (last_block.difficulty - 1) > 0:
            return last_block.difficulty - 1
        
        return 1

    @staticmethod
    def is_valid_block(last_block, block):
        """
        اعتبار سنجی بلاک ها طبق قوانین زیر :
        * بلاک باید حاوی هش قبلی خود بصورت کامل و سالم باشد 
        * بلاک باید دارای استاندار های اثبات کار  باشد 
        * سختی شبکه باید یک باشد
        * بلاک باید دارای ترکیب درستی از اطلاعات باشد
        """
        if block.last_hash != last_block.hashed:
            raise Exception('The Block last_hash Is not Correct! ')
        
        if hex_to_binary(block.hashed)[0:block.difficulty] != '0' * block.difficulty:
            raise Exception('Ther Block havent requirment of PoW')
        
        if abs(last_block.difficulty - block.difficulty) > 1:
            raise Exception('the block difficulty must only adjust ny 1')

        reconstructed_hash = crypto_hash(
            block.timestamp,
            block.last_hash,
            block.data,
            block.nonce,
            block.difficulty

        )

        if block.hashed != reconstructed_hash:
            raise Exception('The Block Hash Is not Correct')


# ================================================> نمایش اطلاعات بلوک اطلاعات درصورت اجرای مستقیم

def main():
    genesis_block = Block.genesis()
    bad_blcok = Block.mine_block(genesis_block, 'omid')
    bad_blcok.last_hash = 'hacker_data'

    try:
        Block.is_valid_block(genesis_block, bad_blcok)
    except Exception as e:
        print(f'Block Validation : {e}')


if __name__ == '__main__':
    main()
