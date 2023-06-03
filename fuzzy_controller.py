class FuzzyController:

    def colse_L_membership(self, x):
        if 0 <= x < 50:
            return 1 - x / 50
        return 0

    def far_L_membership(self, x):
        if 50 < x <= 100:
            return x / 50 - 1
        return 0

    def moderate_L_membership(self, x):
        if 35 < x < 50:
            return x / 15 - 7 / 3
        if 50 <= x < 65:
            return 13 / 3 - x / 15
        return 0

    def colse_R_membership(self, x):
        if 0 <= x < 50:
            return 1 - x / 50
        return 0

    def far_R_membership(self, x):
        if 50 < x <= 100:
            return x / 50 - 1
        return 0

    def moderate_R_membership(self, x):
        if 35 < x < 50:
            return x / 15 - 7 / 3
        if 50 <= x < 65:
            return 13 / 3 - x / 15
        return 0




    def high_right_membership(self, x):
        if -50 <= x <= -20:
            return x / 30 + 50 / 30
        if -20 < x < -5:
            return -1 / 3 - x / 15
        return 0

    def high_left_membership(self, x):
        if 20 <= x < 50:
            return -x / 30 + 50 / 30
        if 5 < x < 20:
            return -1 / 3 + x / 15
        return 0

    def low_right_membership(self, x):
        if -10 > x > -20:
            return x / 10 + 2
        if -10 <= x < 0:
            return - x / 10
        return 0

    def low_left_membership(self, x):
        if 10 < x < 20:
            return -x / 10 + 2
        if 10 >= x > 0:
            return x / 10
        return 0

    def nothing_membership(self, x):
        if -10 < x <= 0:
            return x / 10 + 1
        if 10 > x > 0:
            return 1 - x / 10
        return 0

    def __init__(self):
        pass

    def decide(self, left_dist, right_dist):

        close_L = self.colse_L_membership(left_dist)
        moderate_L = self.moderate_L_membership(left_dist)
        far_L = self.far_L_membership(left_dist)
        close_R = self.colse_R_membership(right_dist)
        moderate_R = self.moderate_R_membership(right_dist)
        far_R = self.far_R_membership(right_dist)

        low_right = min(close_L, moderate_R)
        high_right = min(close_L, far_R)
        low_left = min(moderate_L, close_R)
        high_left = min(far_L, close_R)
        nothing = min(moderate_L, moderate_R)

        def max_function(x):
            return max(min(low_right, self.low_right_membership(x)),
                       min(high_right, self.high_right_membership(x)),
                       min(low_left, self.low_left_membership(x)),
                       min(high_left, self.high_left_membership(x)),
                       min(nothing, self.nothing_membership(x)))

        x = -50
        b = +50
        makhraj = 0.0
        soorat = 0.0
        while x < b:
            x = x + 0.1
            makhraj = makhraj + max_function(x) * 0.1
            soorat = soorat + max_function(x) * 0.1 * x
        if makhraj != 0:
            return float(soorat) / float(makhraj)
        return 0
