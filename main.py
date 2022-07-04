class grandParent:
    def __init__(self):
        print("Grandparent's init")

    def temp(self):
        print("Temporary function")

class parent(grandParent):
    def code(self):
        print("Python.py")

class child(parent):
    def fun(self):
        print("Fun.py")

obj = child()
obj.code()
obj.fun()
obj.temp()
