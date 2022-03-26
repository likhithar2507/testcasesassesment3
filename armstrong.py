def armstrong_number(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        return "Armstrong number"
    else:
        return "not an Armstrong number"
if __name__ == "__main__":
   print("to check armstrong or not")
   num = int(input("Enter the Number : "))
   result = armstrong_number(num)
   print(result)