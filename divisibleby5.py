def divisibleby5 (num):
    if num % 5==0:
        return "divisible by 5"
    else:
        return "not divisible by 5"
if __name__=="__main__":
    print("to check the number is  divisible by 5 or not")
    num=int(input("Enter a Number : "))
    result=divisibleby5(num)
    print(result)