class Router:
    def __init__(self, name, neighbours, initial_cost, initial_distance):
        self.name = name
        self.neighbours = neighbours
        self.cost = initial_cost.copy()
        self.hop = initial_cost.copy()


def print_tables(x):
    print("\nPrinting routing table of "+x.name)
    print("\nRouter  Distance  Hop")
    print("---------------------")
    for i in x.cost.keys():
        print("{:<6}  {:<8}  {:<3}".format(i, x.cost[i], x.hop[i]))


def update_tables(x):
    for i in x.neighbours:
        neighbour = globals()["node_"+i]
        for destination in x.cost.keys():
            opt = min(x.cost[destination],
                      neighbour.cost[destination]+neighbour.cost[x.name])
            if opt < x.cost[destination]:
                x.cost[destination] = opt
                x.hop[destination] = neighbour.name


n = 4
routers = ["A", "B", "C", "D"]
ini_cost = {i: 99999 for i in routers}
ini_dist = {i: "nil" for i in routers}
neighbours = [["A", "B", 8],
              ["B", "C", 2],
              ["C", "D", 3],
              ["D", "A", 5]]
node_A = Router("A", ["B", "D"], ini_cost, ini_dist)
node_B = Router("B", ["C", "A"], ini_cost, ini_dist)
node_C = Router("C", ["D", "B"], ini_cost, ini_dist)
node_D = Router("D", ["C", "A"], ini_cost, ini_dist)
for i in neighbours:
    node1, node2, cos = i
    var1 = globals()["node_" + node1]
    var2 = globals()["node_" + node2]
    var1.cost[node1] = 0
    var1.hop[node1] = node1
    var2.cost[node2] = 0
    var2.hop[node2] = node2
    var1.cost[node2] = cos
    var1.hop[node2] = node2
    var2.cost[node1] = cos
    var2.hop[node1] = node1


for iterate in range(5):
    print()
    print("iteration", iterate)
    update_tables(node_A)
    update_tables(node_B)
    update_tables(node_C)
    update_tables(node_D)
    print("after updation")
    print_tables(node_A)
    print_tables(node_B)
    print_tables(node_C)
    print_tables(node_D)
