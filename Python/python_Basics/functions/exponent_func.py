# Creating an exponent func in a for loop

def raise_to_power(base_num, pow_num):
    result = 1 # where we store the math
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 4))