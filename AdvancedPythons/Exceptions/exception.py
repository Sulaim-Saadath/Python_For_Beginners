# print("Program Started")
# try:
#     a = 10 / 0 # Exception
# except (ZeroDivisionError) as e:
#     print(f"Error occured {e}")
#     print("Thank you")
    
# Multiple Exception
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num # Zero Division exception, value Error
#     print(result)
# except ZeroDivisionError:
#     print("Error, Cannot be divided by zero")
# except ValueError:
#     print("Error, Only Integer is accepted")
# # Generic Excption Always placed in last
# except:
#     print("Unexcpected Error is occured")
    
# try - except with else
# try: 
#     b = int(input())
#     res = 10/b
# except:
#     print("Error occured")
# else:
#     print("Executed without any unexpected errors.")

# try-except and finally
try: 
    b = int(input())
    res = 10/b
except:
    print("Error occured")
finally:
    print("Inside finally block, this line is executed either exception occurs or not.")
