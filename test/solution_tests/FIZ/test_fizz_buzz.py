from lib.solutions.FIZ import fizz_buzz_solution


class TestFizBuzz():
    def test_fiz_buzz(self):
        assert fizz_buzz_solution.compute(1, 2) == 3