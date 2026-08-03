# CustomException
class InvalidMarksError(Exception):# Extending the exception to Exception class
    def __init__(self, message = "Marks should be between 0 to 100"):
        self.message = message
        super().__init__(self.message)
    pass

try:
    marks = int(input("Enter the marks: "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError()
    print(f"Marks is {marks}")
except InvalidMarksError as e:
    print(f"Custom error: {e}")