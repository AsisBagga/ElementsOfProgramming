from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:

    # Brute-force
    # initialize diff to 0
    # 1st For iterate from the back
    #   internallt iterate from front 
    #   and update diff if diffrence of(i-j)> diff
    #   return diff if diff>0
    '''    
    diff = 0
        # capturing selling price...
        for i in reversed(range(len(prices))):
            # capturing buying price hence goes till i only...
            for j in range(0, i):
                if prices[i] - prices[j] > diff:
                    #print(diff)
                    diff = prices[i] - prices[j]
        #print(diff)
        return diff if diff>0.0 else 0.0
    '''
    # Devide-Conqure Algorithm
    # We calculate real-time(i) profit calling it profit of the day and subtracting with minimum selling price captured so far
    # We capture the max profit by keep track of old profit of the day and compare with ith one
    # We capture max min sell price - same by keeping track of old prices
    min_price = float('inf')
    max_profit = 0.0
    # capturing buying price...
    for price in prices:
        profit_of_the_day = price - min_price
        # keeping track of max profit we got
        max_profit = max(profit_of_the_day, max_profit)
        # keeping track of min price gotten so far so that we drive the today profit
        min_price = min(price, min_price)
    return max_profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
