import random

"""
    this question basically asking us to find a approximate value for a^1/5 with the given margin of error. That's why
    in bisection method, we will choose the interval as (0,a), this way we will able to get close to the a^1/5
    by shrinking this interval

"""
def approx_calculator(a, margin_of_error):

        left_side = 0
        right_side = a
        while (abs(right_side - left_side) > margin_of_error):
            mid = (left_side + right_side) / 2
            if (pow(a,1/5) < mid):
                right_side = mid
            else:
                left_side = mid
        return (left_side + right_side) / 2

a = int(input("Enter the number: "))
margin_of_error = float(input("Enter the margin_of_error: "))

print(f'Approximate value for the given number {a} with respect to margin of error is', approx_calculator(a,margin_of_error))




