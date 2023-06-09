def maxProfit(prices):
    profit, buy, sell = 0, 0, 1
    while sell < len(prices):
        diff = prices[sell] - prices[buy]
        profit = max(profit, diff)
        if prices[buy] > prices[sell]:
            buy = sell
        sell += 1
    return profit



print(maxProfit([2,1,4]))