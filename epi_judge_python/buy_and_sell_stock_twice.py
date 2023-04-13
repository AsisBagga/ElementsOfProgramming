from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    max_profit = 0
    min_price = float('inf')
    profit_list = [0] * len(prices)
    for i in range(len(prices)):
        profit_of_the_day = max(max_profit, prices[i]-min_price)
        max_profit = max(profit_of_the_day, max_profit)
        min_price = min(prices[i], min_price)
        profit_list[i] = max_profit
        
    reverse_profit_list = [0] * len(prices)
    max_price = float('-inf')
    max_profit = 0
    for j in range(len(prices)-1, 0, -1):
        max_price = max(max_price, prices[j])
        max_profit = max(max_profit, max_price-prices[j])
        reverse_profit_list[j] = max_profit
    return max([reverse_profit_list[i]+ profit_list[i-1] for i in range(len(reverse_profit_list))])


if __name__ == '__main__':
#    print(buy_and_sell_stock_twice([12,11,13,9,12,8,14,13,15]))
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
