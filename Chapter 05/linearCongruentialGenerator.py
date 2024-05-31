import matplotlib.pyplot as plt

def next_random(previous, n1, n2, n3):
    the_next = (previous * n1 + n2) % n3
    return the_next


def list_random(n1, n2, n3):
    output = [1]
    while len(output) <= n3:
        output.append(next_random(output[len(output) - 1], n1, n2, n3))
    return output


def overlapping_sums(the_list, sum_length):
    length_of_list = len(the_list)
    the_list.extend(the_list)
    output = []
    for n in range(0, length_of_list):
        output.append(sum(the_list[n:(n + sum_length)]))
    return output


overlap = overlapping_sums(list_random(211111, 111112, 300007), 12)
plt.hist(overlap, 20, facecolor = 'blue', alpha = 0.5)
plt.title('Results of the Overlapping Sums Test')
plt.xlabel('Sum of Elements of Overlapping Consecutive Sections of List')
plt.ylabel('Frequency of Sum')
plt.show()