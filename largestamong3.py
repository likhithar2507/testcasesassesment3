def Largestamong3(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    elif z>x and z>y:
        return z
if __name__=="__main__":
    print("Enter 3 numbers to check the greatest ")
    x = int(input("Enter number 1: "))
    y = int(input("Enter number  2 : "))
    z = int(input("Enter number 3 : "))
    result = Largestamong3(x, y, z)
    print(result)