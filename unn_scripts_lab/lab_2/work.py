class EnumStrategy:
    @staticmethod
    def investor_work(investor, stonks):
        stocks = len(stonks)
        investor_result = 0
        result_stocks = []

        for i in range(2 ** stocks):
            res = []
            money = investor.money
            for j in range(stocks):
                if (i >> j) & 1:
                    if money - stonks[j].get_cost() >= 0:
                        res.append(stonks[j])
                        money -= stonks[j].get_cost()

            m_res = sum([stock.get_ye_result_after_n_days(investor.days) for stock in res])

            if m_res > investor_result:
                investor_result = m_res
                result_stocks = res

        investor.set_result(investor_result)
        return result_stocks


class DynamicStrategy:
    def __init__(self):
        pass
