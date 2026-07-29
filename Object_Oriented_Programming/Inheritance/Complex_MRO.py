# MRO (Method Resolution Order) tells Python the path to follow when
# a method is called on an object with multiple inheritance.
# Python does not just look at the first parent; it builds a safe order
# that keeps the inheritance structure consistent and avoids ambiguity.
#
# For class G(D, E, F), Python checks the class itself first, then its
# parents in a specific sequence so that the method is found in a predictable
# way. The final MRO becomes:
# G -> D -> E -> B -> F -> C -> A -> object
#
# Why this order?
# 1. G is checked first because the method is called on G.
# 2. D is placed before E because D appears first in G(D, E, F).
# 3. B is placed before F because B is a parent of D and appears before C
#    in the inheritance chain.
# 4. C is placed after F because F is listed before C in the class definition.
# 5. A is reached only after all more specific classes are checked.
# 6. object is the common base class at the end.
#
# This is why super().show() in each class passes the call to the next class
# in the MRO, not just to the immediate parent.

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B):
    def show(self):
        print("D")
        super().show()

class E(B):
    def show(self):
        print("E")
        super().show()

class F(C):
    def show(self):
        print("F")
        super().show()

class G(D, E, F):
    def show(self):
        print("G")
        super().show()

obj = G()
print(G.mro())
obj.show()