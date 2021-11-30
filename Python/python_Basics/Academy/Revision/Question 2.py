# Identification num
# def compute_check_digit(identification_number: str) -> int:
#     # sum the digits
#     # result * 3
#     # add the digits in odd positions
#     #take last digit of the result ->
#     # if not 0, - digit from 10
#     # return result
#     counter = 1
#     result = 0
#     odd_number = []
#     even_number = []
#     for digit in id_num:
#         if  in digit != 0:
#             return 10 - i
#             result += 1
#         elif i in digit % 2 == 0:
#             print(sum(i))
#             return +=
#     else:
#     return result
# func which takes a str input of a big num
# loop through the num and create 2 totals, even pos
# even totals * 3 + odd totals
#
# 10 - last digit

def function1(id_number: str):
    even_count = 0
    odd_count = 0
    count = 0
    for digit in id_number:
        if count % 2 == 0:
            even_count += int(digit)
        else:
            odd_count += int(digit)
        count += 1
    result = even_count * 3 + odd_count
    last_digit = str(result)[-1]
    if last_digit == "0":
        return 0
    else:
        return 10 - int(last_digit)

print(function1("1212789"))
#def compute_check_digit(identification_num):

