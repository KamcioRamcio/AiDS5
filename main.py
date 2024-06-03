import backpack as bp
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--generate', action='store_true')
    parser.add_argument('--from-file', action='store_true')
    args = parser.parse_args()
    
    backpack = bp.Backpack()
    
    if args.generate:
        size = get_size()
        max_weight = get_max_weight()
        max_value = get_max_value()
        capacity = get_capacity()
        backpack.generate(size, max_weight, max_value, capacity)
        best_set, best_value = backpack.best_set_pd()
        best_set1, best_value1 = backpack.best_set_bt()
        print("value , weight , name")
        for item in backpack.items:
            print(item)
        print(f"Best set dynamic programing: {best_set}")
        print(f"Best value dynamic programing: {best_value}")
        print()
        print(f"Best set brute force: {best_set1}")
        print(f"Best value brute force: {best_value1}")
    elif args.from_file:
        filename = get_file_name()
        try:
            backpack.from_file(filename)
            print("value , weight , name")
            best_set, best_value = backpack.best_set_pd()
            best_set1, best_value1 = backpack.best_set_bt()
            for item in backpack.items:
                print(item)
            print(f"Best set dynamic programing: {best_set}")
            print(f"Best value dynamic programing: {best_value}")
            print()
            print(f"Best set brute force: {best_set1}")
            print(f"Best value brute force: {best_value1}")
        except:
            print("Error while reading the file. You can generate a file to see how it sould look like")
    while True:
        command = get_command()
        if command == 'generate':
            size = get_size()
            max_weight = get_max_weight()
            max_value = get_max_value()
            capacity = get_capacity()
            backpack.generate(size, max_weight, max_value, capacity)
            print("value , weight , name")
            for item in backpack.items:
                print(item)
        elif command == 'to_file':
            filename = get_file_name()
            backpack.to_file(filename)
        elif command == 'from_file':
            filename = get_file_name()
            try:
                backpack.from_file(filename)
                print("value , weight , name")
                for item in backpack.items:
                    print(item)
            except:
                print("Error while reading the file. You can generate a file to see how it sould look like")
        elif command == 'best_set_pd':
            best_set, best_value = backpack.best_set_pd()
            print(f"Best set: {best_set}")
            print(f"Best value: {best_value}")
        elif command == 'best_set_bt':
            best_set, best_value = backpack.best_set_bt()
            print(f"Best set: {best_set}")
            print(f"Best value: {best_value}")
        elif command == 'help':
            help()
        elif command == 'exit':
            break
        else:
            print("Unknown command. Type 'help' to display available commands.")
    
def help():
    print('--- Help ---')
    print('Commands:')
    print('generate - generate a new backpack')
    print('to_file - save the backpack to a file')
    print('from_file - load the backpack from a file')
    print('best_set_pd - find the best set of items using dynamic programming')
    print('best_set_bt - find the best set of items using brute force')
    print('help - display this help message')
    print('exit - exit the program')

def get_size():
    print("Enter the number of items in the backpack certenly there are 15 items in the collection so you can choose from 0 to 15 items.")
    while True:
        try:
            size = int(input("Enter the number of items: "))
            if size < 0:
                raise ValueError
            return size
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")
    
def get_max_weight():
    print("Enter the maximum weight of the backpack feel free to choose any weight you want")
    while True:
        try:
            max_weight = int(input("Enter the maximum weight: "))
            if max_weight < 0:
                raise ValueError
            return max_weight
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")
# przez to jak to piszę to wygląda na wygenerowane XDds
def get_max_value():
    print("Enter the maximum value of item in the backpack feel free to choose any value you want")
    while True:
        try:
            max_value = int(input("Enter the maximum value: "))
            if max_value < 0:
                raise ValueError
            return max_value
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

def get_capacity():
    print("Enter the capacity of the backpack feel free to choose any capacity you want")
    while True:
        try:
            capacity = int(input("Enter the capacity: "))
            if capacity < 0:
                raise ValueError
            return capacity
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

def get_file_name():
    return input("Enter the file name(with extension like .txt): ")


def get_command():
    return input('command> ').lower()





if __name__ == "__main__":
    main()