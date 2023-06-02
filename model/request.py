import time

from constants.constant import CAP_TIME


class ChatGPTRequest:
    def __init__(self, order_num) -> None:
        self.order_num = order_num
        # TODO: 新增记录这是那种gpt类型的属性，比如3.5、4、browser、plugin
        self.trigger_time_epoch = time.time()
        self.time_convert()

    def _get_human_time(self, time_struct):
        hour = time.strftime("%H", time_struct)
        minute = time.strftime("%M", time_struct)
        return f"{int(hour)}点{int(minute)}分"

    def time_convert(self):
        time_struct = time.localtime(self.trigger_time_epoch)
        self.trigger_time_full = time.strftime("%Y-%m-%d %H:%M:%S", time_struct)
        self.trigger_time_human = self._get_human_time(time_struct)
        self.ert_epoch = self.trigger_time_epoch + CAP_TIME
        self.ert_time_human = self._get_human_time(time.localtime(self.ert_epoch))


if __name__ == "__main__":
    c = ChatGPTRequest(1)
    print(c.trigger_time_full)
    print(c.trigger_time_human)
    print(c.ert_time_human)
