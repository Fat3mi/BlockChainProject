# سیدامید فاطمی - طراحی بلاک چین

# ================================================> کتابخانه ها و فایل های مورد نیاز

from backend.blockchain.block import Block

# ================================================> ساخت زنجیره بلوک ها


class Blockchain:
    """
    لیستی از اطلاعات و تراکنش های هش شده .
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):        
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

    def replace_chain(self, chain):
        """
        جایگذاری زنجیره ورودی بجای زنجیره محلی :
        * زنجیره ورودی باید طولانی تر از زنجیره محلی باشد
        * زنجیره ورودی باید به درستی شکل گرفته باشد
        """
        if len(chain) <= len(self.chain):
            raise Exception('Cannot Rplace. incoming chain is not longer than localchain')
        
        try:
            Blockchain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(f'Cannot Rplace. The incoming chain is invalid: {e}')

        self.chain = chain

    def to_json(self):
        """
        سریالایز کردن برای ارسال به ای پی آی
        """
        return list(map(lambda block: block.to_json(), self.chain))

    @staticmethod
    def is_valid_chain(chain):
        """
        اعتبار سنجی زنجیره
        * زنجیره باید با بلاک اولیه یا همان جنسیس شروع شود
        * بلاک ها باید به درستی شکل گرفته باشند
        """
        if chain[0] != Block.genesis():
            raise Exception('The genesis block is not valid!')
        
        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block, block)


# ================================================> نمایش اطلاعات زنجیره بلوک ها درصورت اجرای مستقیم


def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')
    blockchain.add_block('omid')

    print(blockchain)
    print(f'blockchain.py __name__: {__name__}')


if __name__ == '__main__':
    main()
