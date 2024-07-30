def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    # Ініціалізуємо dp масив великими значеннями
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    # Масив для відстеження, які монети використовуються
    coin_used = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    # Відновлюємо використані монети
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

# Приклад використання
amount = 313
print(find_min_coins(amount))
