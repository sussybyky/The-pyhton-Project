from test import *

# This is a Comment

string = t.String = "This is a String"
integer = t.Integer = 1
floating = t.Float = 3.4
boolean = t.Boolean = True
listf = t.List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tuplef = t.Tuple = (1, 2, 3, 4, 5, 6, 7, 8)
setf = t.Set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Following are a few System Functions

py.sys.out("Hello World")
py.sys.out(string)

py.sys.inp("Input: ")
x = t.Integer = py.sys.binaer(10)
py.sys.out(x)
# py.sys.close() # This Function is like exit()
b = t.Boolean = py.sys.istype(1, int)
py.sys.out(b)

# Following are other System Fuctions

py.fc.forif(1 == 1, py.sys.out("1 is 1"))
py.fc.loop()  # The Loop functions is still in progress
