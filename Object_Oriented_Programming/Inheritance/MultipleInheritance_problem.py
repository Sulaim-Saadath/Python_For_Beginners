class Father:
    def show(self):
        print("Inside the Father class")
class Mother:
    def show(self):
        print("Inside the Mother class")
class child(Father, Mother):
    pass
c = child()
c.show()