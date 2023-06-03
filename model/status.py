import time
from typing import List
from constants.constant import CAP_LIMIT, CAP_TIME


from model.request import ChatGPTRequest
from utils.time_util import seconds_to_hour_minute_second


class ChatGPTStatus:
    def __init__(self) -> None:
        self.requests: List[ChatGPTRequest] = []

    def receive_new_request(self):
        self.requests.append(ChatGPTRequest(len(self.requests)+1))

    def refresh_status(self):
        if self.requests and (time.time() - self.requests[0].trigger_time_epoch > CAP_TIME):
            self.requests.clear()

    def get_available_quantity(self) -> int:
        return CAP_LIMIT - len(self.requests)

    def get_usage_status(self):
        self.refresh_status()
        result = []
        result.append(f"当前状态：{'使用中' if self.requests else '空闲中'}")
        if self.requests:
            result.append(f"已使用{len(self.requests)}条，初次使用时间：{self.requests[0].trigger_time_human}，额度重置时间：{self.requests[0].ert_time_human}")
            result.append(f"剩余额度【{CAP_LIMIT-len(self.requests)}】条，重置剩余时间：【{seconds_to_hour_minute_second(self.requests[0].ert_epoch-time.time())}】")
        return '\n'.join(result)



