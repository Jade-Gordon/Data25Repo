# def add(x, y):
#     return x + y
#
# print(add(1, 2))
#
# # Now the lambda version of the above func:
# addition = lambda x, y: x + y
#
# print(addition(3, 4))

savings = [234, 555, 674, 78]

bonus = list(map(lambda x: x*1.1, savings))

print(bonus)