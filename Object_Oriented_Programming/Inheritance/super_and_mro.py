class A:
    def __init__(self):
        print("Iniside A")
class B(A):
    def __init__(self):
        super().__init__()
        print("Iniside B")
class C(A):
    def __init__(self):
        super().__init__()
        print("Inside C")
class D(B, C):
    def __init__(self):
        super().__init__()
        print("Inside D")
d = D()
