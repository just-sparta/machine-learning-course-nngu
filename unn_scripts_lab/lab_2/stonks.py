class Investor:
    def __init__(self, days, lots, money):
        self.days = int(days + 30)
        self.lots = int(lots)
        self.money = int(money)
        self.end_result = None

        self.stocks = []

    def get_stocks(self, stock):
        if self.money >= stock.get_cost():
            self.stocks.append(stock)
            self.money -= stock.get_cost()

    def set_result(self, result):
        self.end_result = result

    def get_result(self):
        return self.end_result


class Stock:
    def __init__(self, day, name, price, count):
        self.day = int(day)
        self.name = name
        self.price = float(price) * 10
        self.count = int(count)

        self.cost = self.get_cost()

    def __str__(self):
        return f'{self.day} {self.name} {self.price / 10} {self.count}'

    def __repr__(self):
        return str(self)

    def get_cost(self):
        return self.price * self.count

    @staticmethod
    def add(line):
        day, name, price, count = line.split()
        return Stock(day, name, price, count)

    def get_ye_result_after_n_days(self, n):
        return (n - self.day - self.price + 1000) * self.count
