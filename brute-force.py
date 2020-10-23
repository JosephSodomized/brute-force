import random


def dataset(n, capacity):
    data = []
    for i in range(n):
        #(weight, value)
        data.append((random.randint(1, capacity),
                     random.randint(1,  capacity)))
    return data

def possibilities(dataset):
    possibilities = [[]]
    for item in dataset:
        new = [possibility+[item] for possibility in possibilities]
        possibilities.extend(new)
    return possibilities
	
# random data set
while True:
    n = input('Number of available products: ')

    if n.isdecimal():
        n = int(n)
        break

while True:
    capacity = input('Backpack capacity: ')

    if capacity.isdecimal() and int(capacity) >= 1:
        capacity = int(capacity)
        break

print('Data (Products):')
data = dataset(n, capacity)
print(data)
print('--------')

#our data set
'''
data = [(59, 30), (3, 1), (23, 11), (8, 50), (9, 17), (12, 40), (62, 14), (13, 20), (5, 12), (5, 15)]
capacity = 50
'''
print('Possibilities')
possibilities = possibilities(data)
print(possibilities)
print('--------')

input("Press enter to close program")
