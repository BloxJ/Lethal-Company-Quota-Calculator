import readchar

print("Welcome to Lethal Company Quota Calcuator v1.1!")
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
    items = []
    while True:
        remaining_items = input("Enter the prices of your scrap separated by spaces: ").split()
        remaining_items = [int(item) for item in remaining_items]
        
        if not items:
            items = remaining_items
        else:
            for item in remaining_items:
                if item in items:
                    items.remove(item)

        target = int(input("Enter the quota amount: "))

        combination = find_combination(items, target)
        total_cost = sum(combination)

        if total_cost < target:
            print("Error: Prices of scrap are less than the target quota.")
            print("Press any key to exit...")
            k = readchar.readchar()
            break
        else:
            print("Prices of items to sell:", combination)
            print("Total amount to sell:", total_cost)

        choice = input("Do you want to add more costs of items? (yes/no): ").lower()
        if choice != 'yes':
            break


if __name__ == "__main__":
    main()