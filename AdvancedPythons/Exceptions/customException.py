# CustomException
class InvalidMarksError(Exception): # Extending the exception to Exception class
    pass

try:
    marks = int(input("Enter the marks: "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks should be between 0 to 100")
    print(f"Marks is {marks}")
except InvalidMarksError as e:
    print("Custom error:",e)