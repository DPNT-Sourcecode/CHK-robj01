from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        a = [[1,2,3],[3,4,5],[7,8,9]]
        c = [i for num in a for i in num]
        print(c)
        assert checkout_solution.checkout("STXYZ") == -1

