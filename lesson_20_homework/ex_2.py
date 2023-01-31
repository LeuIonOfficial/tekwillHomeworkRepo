
class NumberList(list):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.append = args
        self.extend = kwargs

    def get_sum(self, **kwargs):
        i = sum(**kwargs)
        return i


sum_of_list = NumberList([1, 2, 3, 4, 5, 6])
print(NumberList.get_sum(sum_of_list))
