cities = ['Delhi', 'kolkata', 'pune', 'Bangalore', 'Mumbai', 'Chennai']

def length(lst):
    lth = 0
    for i in lst:
        lth = lth + 1
    return lth

print("Length of the cities list is {}".format(length(cities)))

def print_list(lst):
    for i in lst:
        print(i)

print_list(cities)
        

    