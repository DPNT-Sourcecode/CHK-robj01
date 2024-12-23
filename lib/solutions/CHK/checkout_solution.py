from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_table = {"A": {"price": 50, "offer": {"count": 3, "price": 130}},
                   "B": {"price": 30, "offer": {"count": 2, "price": 45}},
                   "C": {"price": 50, "offer": None},
                   "D": 15}
    skus_counter = Counter(skus)
    print(skus_counter)
    return None

