# سیدامید فاطمی - طراحی بلاک چین

#================================================> کتابخانه ها و فایل های مورد نیاز

import pytest
from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA

#================================================> تست های زنجیره بلوک های اطلاعات

# صحت هش بلوک اولیه
def test_blockchain_instance():
    blockchain = Blockchain()

    assert blockchain.chain[0].hashed == GENESIS_DATA['hashed']

# صحت ایجاد بلاک
def test_add_block():
    blockchain = Blockchain()
    data = 'test-data'
    blockchain.add_block(data)

    assert blockchain.chain[-1].data == data


# تولید سه بلاک برای تست
@pytest.fixture
def blockchain_three_block():
    blockchain = Blockchain()
    for i in range(3):
        blockchain.add_block(i)
    return blockchain

# صحت سلامت زنجیره
def test_is_valid_chain(blockchain_three_block):
    Blockchain.is_valid_chain(blockchain_three_block.chain)
    
# بررسی بلوک اولیه معیوب
def test_is_valid_chain_bad_genesis(blockchain_three_block):
    blockchain_three_block.chain[0].hashed = 'hackers_hash'

    with pytest.raises(Exception, match='The genesis block is not valid!'):
        Blockchain.is_valid_chain(blockchain_three_block.chain)

# صحت تعویض زنجیره معیوب برای حفط سلامت و جلوگیری از خرابکاری
def test_replace_chain(blockchain_three_block):
    blockchain = Blockchain()
    blockchain.replace_chain(blockchain_three_block.chain)

    assert blockchain.chain == blockchain_three_block.chain

# تعویض زنیجره کوتاه با بلند
def test_replace_chain_not_longer(blockchain_three_block):
    blockchain = Blockchain()

    with pytest.raises(Exception, match='Cannot Rplace. incoming chain is not longer than localchain'):
        blockchain_three_block.replace_chain(blockchain.chain)

# صحت اعتبار سنجی هش
def test_replace_chain_bad_chain(blockchain_three_block):
    blockchain = Blockchain()
    blockchain_three_block.chain[1].hashed = 'Hackers_data'
    
    with pytest.raises(Exception , match='The incoming chain is invalid'):
        print(blockchain.replace_chain(blockchain_three_block.chain))

 