import time
from datetime import datetime

import arrow

from constants.constant import CAP_TIME


class ChatGPTRequest:
    def __init__(self, order_num) -> None:
        self.order_num = order_num
        # TODO: 新增记录这是那种gpt类型的属性，比如3.5、4、browser、plugin
        self.trigger_time_epoch = time.time()
        self.time_convert()

    def time_convert(self):
        trigger_time_local = arrow.get(self.trigger_time_epoch).to('Asia/Shanghai')
        self.trigger_time_full = trigger_time_local.format('YYYY-MM-DD HH:mm:ss')
        self.trigger_time_human = trigger_time_local.format('h点m分')
        self.ert_epoch = self.trigger_time_epoch + CAP_TIME
        ert_time_local =  arrow.get(self.ert_epoch).to('Asia/Shanghai') 
        self.ert_time_human = ert_time_local.format('h点m分')


if __name__ == "__main__":
    c = ChatGPTRequest(1)
    print(c.trigger_time_full)
    print(c.trigger_time_human)
    print(c.ert_time_human)
