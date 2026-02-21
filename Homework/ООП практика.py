class Numbers:
    def __init__(self):
        self.list_of_numbers = sorted([-25, -10, -7, -3, 2, 4, 8, 10])
        self.sum_for_zero = []

    def sort_num_for_zero(self):
        n = len(self.list_of_numbers)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    val_i = self.list_of_numbers[i]
                    val_j = self.list_of_numbers[j]
                    val_k = self.list_of_numbers[k]
                    if val_i + val_j + val_k == 0:
                        self.sum_for_zero.append([val_i, val_j, val_k])

        print(self.sum_for_zero)


res = Numbers()
res.sort_num_for_zero()
