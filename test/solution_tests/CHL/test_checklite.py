from lib.solutions.CHL import checklite_solution


class TestCheckLite():
    def test_checklite(self):
        assert checklite_solution.compute(1, 2) == 3