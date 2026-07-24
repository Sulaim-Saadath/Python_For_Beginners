sqr = [6,5,3,1,7]
new_sqr = [num * num for num in sqr]
print(new_sqr)

odd_numbers = [num for num in sqr if num % 2 != 0]
print(odd_numbers)

integers = [9, -7, 5, -2, -4, 5]
new_list = [0 if num < 0 else num for num in integers]
print(new_list)