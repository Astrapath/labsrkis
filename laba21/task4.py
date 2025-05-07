from laba21.task3 import example


def count_it(sequence):
    counts = {}
    for digit in sequence:
        digit = int(digit)
        counts[digit] = counts.get(digit, 0) + 1
    sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    top3count = dict(sorted_counts[:3])
    return top3count
example = '1235343858342475083471833216'
print(example)
print(count_it(example))