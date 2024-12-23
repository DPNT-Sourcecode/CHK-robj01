from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_table = {"A": {"price": 50, "offer": {"count": 3, "price": 130}},
                   "B": {"price": 30, "offer": {"count": 2, "price": 45}},
                   "C": {"price": 20, "offer": None},
                   "D": {"price": 15, "offer": None}}
    total_price = 0

    skus_counter = Counter(skus)

    for item, count in skus_counter.items():
        if item not in price_table.keys(): return -1

        total_price += price_table[item]["price"] * count

    return None


