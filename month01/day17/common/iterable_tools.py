class IterableHelper:

    @staticmethod
    def find_all(iterable,func_condition):
        """
        在可迭代对象中,根据指定条件查找所有元素
        :param iterable:可迭代对象
        :param func_condition:函数类型的条件,一个参数,一个bool返回值
        :return:生成器,负责显示满足条件的数据
        """
        for item in iterable:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(iterable,func_condition):
        """
        在可迭代对象中,根据指定条件查找所有元素
        :param iterable:可迭代对象
        :param func_condition:函数类型的条件,一个参数,一个bool返回值
        :return:生成器,负责显示满足条件的数据
        """
        for item in iterable:
            if func_condition(item):
                return item

    @staticmethod
    def select(list01,func_condiction):
        for item in list01:
            yield func_condiction(item)

    @staticmethod
    def get_count(list01,func_condiction):
        count = 0
        for item in list01:
            if func_condiction(item):
                count += 1
        return count

    @staticmethod
    def delete_all(list01,func_condiction):
        count = 0
        for item in range(len(list01)-1,-1,-1):
            if func_condiction(list01[item]):
                del list01[item]
                count += 1
        return count

    @staticmethod
    def get_max(iterable, func_handle):
        max_value = iterable[0]
        for item in range(1, len(iterable)):
            if func_handle(max_value) < func_handle(iterable[item]):
                max_value = iterable[item]
        return max_value

    @staticmethod
    def order_by(iterable,func_condition):
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if func_condition(iterable[r]) > func_condition(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]
        return iterable