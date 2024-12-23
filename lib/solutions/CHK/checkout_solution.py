from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string



def checkout(skus):

    class item:
        def __init__(self, name, price):
            self.name = name
            self.price = price
            self.count = 0

        class cross_offer:
            @staticmethod
            def get():
                return None

        class offer:
            @staticmethod
            def get():
                return None

    class A(item):
        def __init__(self):
            super().__init__("A", 50)

        class offer:
            @staticmethod
            def get():
                count = A.count
                total_item_value = 0

                total_item_value += (count // 5) * 200

                count = count % 5
                total_item_value += (count // 3) * 130

                count = count % 3
                total_item_value += count * 50
                return total_item_value

    class B(item):
        def __init__(self):
            super().__init__("B", 30)

        class offer:
            @staticmethod
            def get(count):
                total_item_value = 0

                total_item_value += (count // 2) * 45

                count = count % 2
                total_item_value += count * 30

                return total_item_value

    class C(item):
        def __init__(self):
            super().__init__("C", 20)

    class D(item):
        def __init__(self):
            super().__init__("D", 15)

    class E(item):
        def __init__(self):
            super().__init__("E", 40)

        class cross_offer:
            @staticmethod
            def get():
                B.count = B.count - 1 if B.count >= 1 else 0
                print("Applied!")

    def item_count():
        skus_counter = Counter(skus)
        for item, count in skus_counter.items():
            if item not in price_table.keys(): return -1

            item_object = price_table[item]
            item_object.count = count

    def cross_offer_get():
        for item in price_table.values():
            item.cross_offer.get()

    A, B, C, D, E = A(), B(), C(), D(), E()

    price_table = {"A": A,
                   "B": B,
                   "C": C,
                   "D": D,
                   "E": E}

    total_price = 0

    item_count()
    print(A.count, B.count, C.count, D.count, E.count)
    cross_offer_get()

    print(A.count, B.count, C.count, D.count, E.count)

    return None





