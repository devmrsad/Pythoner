def binary_search(list, target):
    list = sorted(list)
    first = 0
    last = len(list) - 1
    count = 0

    while first <= last:
        count += 1
        # roundUp
        midpoint = (first + last) // 2
        
        if list[midpoint] == target:
            return (midpoint, count)
        elif list[midpoint] < target:
            first = midpoint + 1
        elif list[midpoint] > target:
            last = midpoint - 1
    
    return None

def show_output(result):
    if result == None:
        print("Target not found!")
    else:
        print(f"The target found at index {result[0]}")
        print(f"search steps: {result[1]}")

def find_item(list, target):
    final = binary_search(list, target)
    show_output(final)

# find_item([your_list], your_target)

print("Feel free to do something with the source!")