class Food:
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def getDensity(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        return f"{self.name} : < {str(self.getValue())}, {str(self.getCost())} >"

def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu



def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue = 0.0
    totalCost = 0.0

    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()

    return(result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print(f"Total value of items = {val}")
    for item in taken:
        print(f"   {item}")

def testGreedys(foods, maxUnits):
    print(f"Use greedy by value to allocate {maxUnits} calories")
    testGreedy(foods, maxUnits, Food.getValue)
    print(f"\nUse greedy by cost to allocate {maxUnits} calories")
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    print(f"\nUse greedy by density to allocate {maxUnits} calories")
    testGreedy(foods, maxUnits, Food.getDensity)


names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 1000)