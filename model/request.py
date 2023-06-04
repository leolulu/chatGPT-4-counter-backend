import time
from zoneinfo import ZoneInfo

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
        tz_east_8 = ZoneInfo("Asia/Shanghai")  # 东八区
        trigger_time_local = datetime.fromtimestamp(self.trigger_time_epoch)
        self.trigger_time_full = trigger_time_local.astimezone(tz_east_8).strftime("%Y-%m-%d %H:%M:%S")
        self.trigger_time_human = self._get_human_time(trigger_time_local.astimezone(tz_east_8))
        self.ert_epoch = self.trigger_time_epoch + CAP_TIME
        ert_time_local = datetime.fromtimestamp(self.ert_epoch)
        self.ert_time_human = self._get_human_time(ert_time_local.astimezone(tz_east_8))


if __name__ == "__main__":
    c = ChatGPTRequest(1)
    print(c.trigger_time_full)
    print(c.trigger_time_human)
    print(c.ert_time_human)
