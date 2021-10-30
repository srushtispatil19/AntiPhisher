def a():
    test = [1,2,3,4,5,6]
    print("In fuction a")
    return test;

def b():
    print("In function b")
    t = a();
    print(t)

a()
b()
