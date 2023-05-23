# سیدامید فاطمی - طراحی بلاک چین
#================================================> کتابخانه ها و فایل های مورد نیاز 

from backend.blockchain.blockchain import Blockchain
from backend.config import SECONDS
import time

#================================================> ماین کردن 1000 بلوک و بدست آوردن مدت زمان و میانگین آن

blockchain = Blockchain()

times = []

for i in range(1000):
    start_time = time.time_ns()
    blockchain.add_block(i)
    end_time = time.time_ns()

    time_to_mine = (end_time - start_time) / SECONDS
    times.append(time_to_mine)

    average_time = sum(times) / len(times)

    print(f'New block difficulty: {blockchain.chain[-1].difficulty}')
    print(f'Time to mine new block: {time_to_mine}s')
    print(f'Average time to add blocks: {average_time}s\n')
