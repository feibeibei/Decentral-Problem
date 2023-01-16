from scipy.optimize import linprog

min_coefficient = [1, 1, 1, 1]
left_hand_side = [[2, -8, 0, -10], [-5, -2, 0, 0], [-3, 5, -10, 2]]
right_hand_side = [-50, -100, -25]
x1_bounds = (0, None)
x2_bounds = (0, None)
x3_bounds = (0, None)
x4_bounds = (0, None)
solution = linprog(min_coefficient, A_ub=left_hand_side, b_ub=right_hand_side, bounds=[
                   x1_bounds, x2_bounds, x3_bounds, x4_bounds], integrality=[1, 1, 1, 1])
x_values = solution.x
print("When x1 = %d, x2 = %d, x3 = %d, x4 = %d, we can invest the minimal amount of money to get the desired number of votes." %
      (x_values[0], x_values[1], x_values[2], x_values[3]))
