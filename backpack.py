import random
import itertools

class Backpack:
    def __init__(self):
        self.collection = [
            "Knife",
            "Firestarter",
            "Water Bottle",
            "Water Purification Tablets",
            "First Aid Kit",
            "Compass",
            "Map",
            "Rope",
            "Tarp",
            "Sleeping Bag",
            "Flashlight",
            "Multi-tool",
            "Duct Tape",
            "Hatchet",
            "Whistle",
            "Fishing Rod",
        ]
        self.items = []
        self.dif_items = 0

    def generate(self, items, max_weight, max_value, max_capacity):
        if items <= len(self.collection):
            self.items = [
                (random.randint(1, max_value), random.randint(1, max_weight),self.collection[i])
                for i in range(items)
            ]
            self.capacity = random.randint(max_capacity // 2, max_capacity)
        else:
            print("Error: Not enough items in the collection")
            
    def to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(f"{self.capacity}\n")
            file.write(f"{len(self.items)}\n")
            for item in self.items:
                value, weight, name = item
                file.write(f"{value} {weight} {name}\n")
    def from_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.capacity = int(lines[0])
            self.dif_items = int(lines[1])
            self.items = []
            for line in lines[2:]:
                parts = line.split()
                value = int(parts[0])
                weight = int(parts[1])
                name = " ".join(parts[2:])
                self.items.append((value, weight, name))
            print(self.items)
    def best_set_pd(self):
        n = len(self.items)
        value = [[0 for _ in range(self.capacity+1)] for _ in range(n+1)]
        
        for i in range(1, n+1):
            for w in range(1, self.capacity+1):
                value[i][w] = value[i-1][w]
                if self.items[i-1][1] <= w:
                    value[i][w] = max(value[i][w], value[i-1][w-self.items[i-1][1]] + self.items[i-1][0])
        best_value = value[n][self.capacity]
        best_set = []
        w = self.capacity
        for i in range(n, 0, -1):
            if value[i][w] != value[i-1][w]:
                best_set.append(self.items[i-1])
                w -= self.items[i-1][1]
        return best_set, best_value
                
    
    def best_set_bt(self):
        best_value = 0
        best_set = []
        for i in range(len(self.items)+1):
            for info in itertools.combinations(self.items, i):
                value = sum([item[0] for item in info])
                weight = sum([item[1] for item in info])
                if weight <= self.capacity and value > best_value:
                    best_value = value
                    best_set = info
        return best_set, best_value
            
    
        






    