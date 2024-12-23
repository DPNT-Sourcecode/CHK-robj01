from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus_counter = Counter(skus)
    print(skus_counter)
    return None
