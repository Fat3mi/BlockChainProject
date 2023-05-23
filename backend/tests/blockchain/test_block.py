# سیدامید فاطمی - طراحی بلاک چین

#================================================> کتابخانه ها و فایل های مورد نیاز

import pytest
import time
from backend.config import MINE_RATE, SECONDS
from backend.blockchain.block import Block, GENESIS_DATA
from backend.util.hex_to_binary import hex_to_binary

#================================================> تست های مربوط به بلوک اطلاعات

# صحت ماینینگ
def test_mine_block():
    last_block = Block.genesis()
    data = 'test-data'
    block = Block.mine_block(last_block, data)

    assert isinstance(block,Block)
    assert block.data == data
    assert block.last_hash == last_block.hashed
    assert hex_to_binary(block.hashed)[0:block.difficulty] == '0' * block.difficulty
    

# صحت بلوک اولیه
def test_genesis():
    genesis = Block.genesis()

    assert isinstance(genesis, Block)
    for key, value in GENESIS_DATA.items():
        getattr(genesis, key) == value

 # تست سریع تر از میانگین   
def test_quickly_mined_block():

    last_block = Block.mine_block(Block.genesis(),'omid')
    mined_block = Block.mine_block(last_block,'fatemi')

    assert mined_block.difficulty == last_block.difficulty + 1

# تست کند تر از میانگین
def test_slowly_mined_block():

    last_block = Block.mine_block(Block.genesis(),'omid')
    time.sleep(MINE_RATE / SECONDS)
    mined_block = Block.mine_block(last_block,'fatemi')

    assert mined_block.difficulty == last_block.difficulty - 1

# تست مجدودیت سختی شبکه
def test_mined_block_difficulty_limits_at_1():
    last_block = Block(time.time_ns(), 'test_last_hash', 'test_hash', 'test_data', 1, 0)

    time.sleep(MINE_RATE / SECONDS)
    mined_block = Block.mine_block(last_block,'fatemi')

    assert mined_block.difficulty == 1

# اینستنس ها برای کاهش کد
@pytest.fixture
def last_block():
    return Block.genesis()

@pytest.fixture
def block(last_block):
    return Block.mine_block(last_block, 'test_data')

# صحت بلوک اطلاعات
def test_is_valid_block(last_block, block):
    Block.is_valid_block(last_block, block)


# بررسی بلوک های خراب
def test_is_valid_block_bad_last_hash(last_block, block):
    block.last_hash = 'hackers_last_hash'

    with pytest.raises(Exception, match='The Block last_hash Is not Correct! '):
        Block.is_valid_block(last_block, block)


# بررسی اثبات کار معیوب
def test_is_valid_block_bad_pow(last_block, block):
    block.hashed = 'fff'

    with pytest.raises(Exception, match='Ther Block havent requirment of PoW'):
        Block.is_valid_block(last_block, block) 


# تصحیح سختی شبکه
def test_is_valid_block_jumped_difficulty(last_block, block):
    jumped_difficulty = 10
    block.difficulty = jumped_difficulty
    block.hashed = f'{"0" * jumped_difficulty}111abc'
    
    with pytest.raises(Exception, match='the block difficulty must only adjust ny 1'):
        Block.is_valid_block(last_block, block) 

# تصحیح هش معیوب
def test_is_valid_block_bad_block_hash(last_block, block):
    block.hashed = '0000000000000000bbbabc'

    with pytest.raises(Exception, match='The Block Hash Is not Correct'):
        Block.is_valid_block(last_block, block) 
   