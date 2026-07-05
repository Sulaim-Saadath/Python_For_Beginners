# match 
day = int(input("Enter the day number "))
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case _:
        print("Invalid day")

month = int(input("Enter the month in number: "))
match month:
    case 3 | 4 | 5:
        print("Summer")
    case 6 | 7 | 8:
        print("Rainy")
    case 9 | 10 | 11 | 12:
        print("Winter")
    case _:
        print("Invalid seasons")
    