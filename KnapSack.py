class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(W, arr):
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)
    finalvalue = 0.0

    for item in arr:
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.profit
        else:
            finalvalue += item.profit * W / item.weight
            break

    return finalvalue

if __name__ == "__main__":
    # Accepting user input for knapsack weight
    W = float(input("Enter the knapsack weight: "))

    # Accepting user input for items
    arr = []
    n = int(input("Enter the number of items: "))
    for i in range(n):
        profit = float(input(f"Enter the profit for item {i + 1}: "))
        weight = float(input(f"Enter the weight for item {i + 1}: "))
        arr.append(Item(profit, weight))

    # Calculating the maximum value using fractional knapsack
    max_val = fractionalKnapsack(W, arr)

    # Printing the maximum value obtained
    print("Maximum value obtained is:", max_val)
