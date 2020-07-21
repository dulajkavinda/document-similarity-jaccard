from math import *

def euclidean_distance(x, y):
    return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))
print (euclidean_distance([0, 3, 4, 5], [0, 3, 4, 5]))

def manhattan_distance(x, y):
    return sum(abs(a - b) for a, b in zip(x, y))
print(manhattan_distance([10, 20, 130], [10, 20, 20]))

from decimal import Decimal
def nth_root(value, n_root):
    root_value = 1 / float(n_root)
    return round(Decimal(value) ** Decimal(root_value), 3)
def minkowski_distance(x, y, p_value):
    return nth_root(sum(pow(abs(a - b), p_value) for a, b in zip(x, y)), p_value)
print(minkowski_distance([0, 3, 4, 5], [0, 3, 4, 5], 3))


def square_rooted(x):
    return round(sqrt(sum([a * a for a in x])), 3)
def cosine_similarity(x, y):
    numerator = sum(a * b for a, b in zip(x, y))
    denominator = square_rooted(x) * square_rooted(y)
    return round(numerator / float(denominator), 3)
print(cosine_similarity([3, 45, 7, 2], [2, 54, 13, 15]))


def jaccard_similarity(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality / float(union_cardinality)
print(jaccard_similarity(["hello", "my", "name", "is", "dulaj","hello", "my", "name", "is", "dulaj","hello", "my", "name", "is", "dulaj","hello", "my", "name", "is", "dulaj","hello", "my", "name", "is", "dulaj"], ["hello", "my", "name", "is", "dulaj","hello", "my", "name", "is", "dulaj","hello", "my", "name", "is", "dulaj","hello", "my", "name", "is", "dulaj","hello", "my", "name", "is", "sdulaj"]))