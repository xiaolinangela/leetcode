def maxprofit(prices):
    min_price = float('inf')
    max_profit = 0
    i = 0
    while i < len(prices):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
        i += 1
    return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 2]
    prices1 = [7, 4, 3, 2, 1]

    print(maxprofit(prices1))
