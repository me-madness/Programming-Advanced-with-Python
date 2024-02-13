def choose_coins(coins, target):
    coins = coins.sort(reversed=True)
    index = 0
    used_coins = {}   # coin: time_used
    
    
    while target > 0 and index < len(coins):
        count_current_coins = target // coins[index]
        target = target % coins[index]
        
        if count_current_coins > 0:
            used_coins[coins[index]] = count_current_coins
            
        index += 1    



coins = [int(x) for x in input().split(", ")]
target = int(input())