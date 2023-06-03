class FuzzyGasController:

    def __init__(self):
        pass

    def mem_close(self, x):
        if 0 <= x < 50:
            return -x / 50 + 1
        return 0

    def mem_moderate(self, x):
        if 40 <= x < 50:
            return x / 10 - 4
        if 50 <= x < 100:
            return -x / 50 + 2
        return 0

    def mem_far(self, x):
        if 90 <= x < 200:
            return x / 110 - 90 / 110
        if x >= 200:
            return 1
        return 0

    def mem_low_speed(self, x):
        if 0 <= x < 5:
            return x / 5
        if 5 <= x < 10:
            return -x / 5 + 2
        return 0

    def mem_medium_speed(self, x):
        if 0 <= x <= 15:
            return x / 15
        if 15 < x <= 30:
            return -x / 15 + 2
        return 0

    def mem_high_speed(self, x):
        if 25 <= x < 30:
            return x / 5 - 5
        if 30 <= x < 90:
            return -x / 60 + 9 / 6
        return 0

    def decide(self, center_dist):

        low = self.mem_close(center_dist)
        medium = self.mem_moderate(center_dist)
        high = self.mem_far(center_dist)

        def max_function(x):
            return max(min(low, self.mem_low_speed(x)),
                       min(high, self.mem_high_speed(x)),
                       min(medium, self.mem_medium_speed(x)))

        x = 0
        upper_bound = +90
        makhraj = 0.0
        soorat = 0.0
        while x < upper_bound:
            x = x + 0.1
            makhraj = makhraj + max_function(x) * 0.1
            soorat = soorat + max_function(x) * 0.1 * x
        if makhraj != 0:
            return float(soorat) / float(makhraj)
        return 0

