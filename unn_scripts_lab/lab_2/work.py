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


class DPStrategy:
    @staticmethod
    def investor_work(investor, stonks):
        stocks = len(stonks)
        money_before = investor.money
        dp = [[0] * (money_before + 1)
              for _ in range(stocks + 1)]

        for i, (stock) in enumerate(stonks, 1):
            result = int(stock.get_ye_result_after_n_days(investor.days))
            cost = int(stock.get_cost())

            for j in range(money_before + 1):
                if cost > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + result)

        money_after = money_before
        for i in reversed(range(1, stocks + 1)):
            if dp[i][int(money_after)] != dp[i - 1][int(money_after)]:
                investor.get_stocks((stonks[i - 1]))
                money_after -= stonks[i - 1].get_cost()

        investor.set_result(dp[stocks][money_before])
        return investor.stocks[::-1]
