class Soda:
    def __init__(self, topping):
        self.topping = topping


    def show_my_drink(self):
        if self.topping == '':
            print('Обычная газировка')
        else:
            print(f'Газировка и {self.topping}')


drink = Soda(topping='')
drink.show_my_drink()