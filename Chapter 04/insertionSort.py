from timeit import default_timer as timer
import random, math
import matplotlib.pyplot as plt
import numpy as np

def insert_cabinet(cabinet, to_insert):
    check_location = len(cabinet) - 1
    insert_location = 0
    global stepcounter

    while (check_location >= 0):
        stepcounter += 1
        if to_insert > cabinet[check_location]:
            insert_location = check_location + 1
            check_location = -1
        check_location -= 1
    stepcounter += 1
    cabinet.insert(insert_location, to_insert)
    return cabinet


def insertion_sort(cabinet):
    newcabinet = []
    global stepcounter
    while len(cabinet) > 0:
        stepcounter += 1
        to_insert = cabinet.pop(0)
        newcabinet = insert_cabinet(newcabinet, to_insert)
    return newcabinet


# cabinet = [1, 2, 3, 3, 4, 6, 8, 12]
# newcabinet = insert_cabinet(cabinet, 5)

# start = timer()
size_of_cabinet = 10

def check_steps(size_of_cabinet):
    cabinet = [int(1000 * random.random()) for i in range(size_of_cabinet)]
    global stepcounter
    stepcounter = 0
    sortedcabinet = insertion_sort(cabinet)
    return stepcounter


random.seed(5040)
xs = list(range(1, 100))
ys = [check_steps(x) for x in xs]
ys_exp = [math.exp(x) for x in xs]
ys_squared = [x**2 for x in xs]
ys_threehalves = [x**1.5 for x in xs]
ys_cubed = [x**3 for x in xs]
ys_max = [((x**2 / 2) + (3 * x) / 2) for x in xs]
plt.plot(xs, ys)
axes = plt.gca()
axes.set_ylim([np.min(ys), np.max(ys) + 140])
plt.plot(xs, ys_exp)
plt.plot(xs, xs)
plt.plot(xs, ys_squared)
plt.plot(xs, ys_cubed)
plt.plot(xs, ys_threehalves)
plt.plot(xs, ys_max)
plt.title('Comparing Insertion Sort to Other Growth Rates')
plt.xlabel('Number of Files in Random Cabinet')
plt.ylabel('Steps Required to Sort Cabinet')
plt.show()

# end = timer()
# print(end - start)
# print(sortedcabinet)