import random

def dataset(n, capacity):   
    data = []
    for i in range(n):
        #(weight, value)
        data.append((random.randint(1, capacity), random.randint(1,  capacity)))
    return data

#random data set
while True:
    n = input('Number of available products: ')
    
    if n.isdecimal():
        n = int(n)
        break

while True:
    capacity  = input('Backpack capacity: ')
    
    if capacity.isdecimal() and int(capacity)>=1:
        capacity = int(capacity)
        break

print('Data (Products):')
data = dataset(n, capacity)
print(data)
print('--------')

input("Press enter to close program")
