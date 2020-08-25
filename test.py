#encoding: Utf-8
class Countup:
    def __init__(self, max=5, count=0):
        self.__max = max
        self.__count = count

    # __maxのゲッター
    def get_max(self):
        return self.__max

    # __countのゲッター
    def get_count(self):
        return self.__count

    # __maxのセッター
    def set_max(self, max):
        self.__max = max

    # __countのセッター
    def set_count(self, count):
        self.__count = count

    # maxプロパティの定義
    max = property(get_max, set_max)
    # countプロパティの定義
    count = property(get_count, set_count)

    def counting_machine(self):
        if self.count < self.max:
            print('It is still smaller than 5.')
        else:
            print('It is done')
        self.count += 1


if __name__ == '__main__':

    cm = Countup()
    cm.max = 2
    for i in range(5):
        print('Is it already done?')
        cm.counting_machine()
