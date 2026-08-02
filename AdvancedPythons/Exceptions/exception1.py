try:
    a = int(input("Enter a value: "))
    b = int(input("Enter b value: "))
    num = input().split()
    list1 = []
    for n in num:
        list1.append(int(n))
    res = a/b
    print(list1[5])
# except ZeroDivisionError as e:
#     print("Inside ex1")
#     print(e)
# except IndexError as e1:
#     print("Inside ex2")
#     print(e1)
# except ValueError as e2:
#     print("Inside ex3")
#     print(e2)
#                       OR
# except (ZeroDivisionError, IndexError, ValueError) as e:
#     print(e)
#                         OR
except (Exception) as e:
    print(e)
finally:
    print("Program ends")
    
