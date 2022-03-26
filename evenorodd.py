def even_odd(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"
if __name__=="__main__":
    print("to check odd or even")
    x = int(input("Enter a Number : "))
    result = even_odd(x)
    print(result)
