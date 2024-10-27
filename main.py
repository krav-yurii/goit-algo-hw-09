def find_coins_greedy(amount, coins):
    coins = sorted(coins, reverse=True)  
    result = {}
    for coin in coins:
        count = amount // coin  
        if count > 0:
            result[coin] = count
            amount -= coin * count  
    return result

def find_min_coins(amount, coins):
    max_value = float('inf')
    min_coins = [0] + [max_value] * amount
    coin_used = [0] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    coin_used[i] = coin
                    
    if min_coins[amount] == max_value:
        return {}   
    
 
    result = {}
    i = amount
    while i > 0:
        coin = coin_used[i]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        i -= coin
    return result

if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    amount = 113
    
    greedy_result = find_coins_greedy(amount, coins)
    print(f"Жадібний алгоритм для суми {amount}: {greedy_result}")
    
    dp_result = find_min_coins(amount, coins)
    print(f"Динамічне програмування для суми {amount}: {dp_result}")
