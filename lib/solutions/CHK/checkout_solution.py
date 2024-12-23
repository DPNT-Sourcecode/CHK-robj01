from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    price_table = {"A": {"price": 50, "offer": {"count": 3, "price": 130}},
                   "B": {"price": 30, "offer": {"count": 2, "price": 45}},
                   "C": {"price": 20, "offer": None},
                   "D": {"price": 15, "offer": None},
                   "E": {"price": 40, "offer": None},}
    total_price = 0

    skus_counter = Counter(skus)

    for item, count in skus_counter.items():
        if item not in price_table.keys(): return -1

        item_price = price_table[item]["price"]

        if not price_table[item]["offer"]:
            total_price += item_price * count
        else:
            offer_count = price_table[item]["offer"]["count"]
            offer_price = price_table[item]["offer"]["price"]

            total_price += (count//offer_count) * offer_price + (count%offer_count) * item_price

    return total_price
