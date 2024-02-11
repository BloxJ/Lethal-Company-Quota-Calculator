def find_combination(items, target):
    n = len(items)
    dp = [[0] * (target + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if items[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], items[i - 1] + dp[i - 1][j - items[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    result = []
    i, j = n, target
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            result.append(items[i - 1])
            j -= items[i - 1]
        i -= 1

    return result


def main():
    items = input("Enter the costs of items separated by space: ").split()
    items = [int(item) for item in items]
    target = int(input("Enter the target cost: "))

    combination = find_combination(items, target)
    total_cost = sum(combination)

    if total_cost < target:
        print("Error: Total cost is less than the target. Cannot proceed.")
    else:
        print("Items to sell:", combination)
        print("Total cost:", total_cost)


if __name__ == "__main__":
    main()