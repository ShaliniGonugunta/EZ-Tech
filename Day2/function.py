# # # # def sumOfTwoNumbers(a,b):
# # # #     c=a+b
# # # #     return c
# # # # if __name__ == "__main__":
# # # #     print(sumOfTwoNumbers(3,5))

# # # # positional arguments:
# # # def sumOfNumbers(a,b):
# # #     return a+b
# # # c=sumOfNumbers(10,20)
# # # print(c)

# # # Default arguments
# # def mySelf(a,b):
# #     print(a,"\n",b)
# # mySelf("sri",b=24)

# def evenOrOdd(num):
#     if num%2==0:
#         return "Even"
#     else:
#         return "Odd"
# print(evenOrOdd(10))

# def leapYear(year):
#     if year%400==0 or (year%100!=0 and year%4==0):
#         return "Its a leap year"
#     else:
#         return "Its not a leap year"
# print(leapYear(2100))

def types(a):
    print(type(a))
    return None
types(10)