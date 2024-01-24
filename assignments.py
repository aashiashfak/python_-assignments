#question_1

# list_length =int(input("Enter your list length"))
# list_1 = []
# for i in range(list_length):
#       element = input(f"Enter element {i + 1}: ")
#       list_1.append(element)

# def find_maxElement(list2):
#         """
#         This function find maximum element in a list
#         """
#         maxElement = max(list2)
#         print(maxElement)
# find_maxElement(list_1)
# print(find_maxElement.__doc__)
#=================================================================

# question_2

def reverseString(str1):
    return str1[::-1]
strOg = "Hello world"
strReversed = reverseString(strOg)
# print(strReversed)
# #=================================================================

# # question_3 

def fsort_list(list1):
    for i in range(len(list1)-1):
        for j in range(i+1, len(list1)):
            if list1[i] > list1[j] :
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp
    return list1       
lista = [74,5,6,8,4,2345,345]     
sort_list = fsort_list(lista)
print(sort_list)  
print(sorted(lista))
# =================================================================

# question_4

def find_evenSum(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum=sum+i
    print(sum)
n = 12  
find_evenSum(n)  
#=================================================================

# question_5

# n = int(input("Enter a number to check it is prime or not: "))
# def check_prime(n):
#     if(n <= 1):
#         print("invalid number for checking")
#     else:
#         for i in range(2, n):
#             c = 0
#             if n % i == 0:
#                 c+=1
#                 break
#         if c == 0:
#             print(str(n)+"is a prime number")
#         else:
#             print(str(n)+"is not a prime number")
# check_prime(n)
# ------------------------ with allfunction ------------------------------------------
def checkPrime(n):
    return all(n % i != 0 for i in range(2, n))
print(checkPrime(7))
#=================================================================

# question_6

def find_secLargest(list1):
    secLarge =  sorted(list1)[-2]
    return secLarge
list_ul = [74,5,6,8,4,2345,345]
sl = find_secLargest(list_ul)
print(sl)
#=================================================================

# question_7

def remove_duplicate(list1):
    uniqList=[]
    for item in list1:
        if item not in uniqList:
            uniqList.append(item)
    return uniqList
listCheck = [1,3,4,4,3,5,6,1]
unilist = remove_duplicate(listCheck)
print(unilist)
#=================================================================

# question_8
   
def find_sum(list1):
    return sum(list1)
list_ul = [74,5,6,8,4,2345,345]
totalSum = find_sum(list_ul)
print(totalSum)
# # ==================

# #question_9

def generate_prime(n):
    if n <= 1:
        print("invalid number")
        return []
    primes = []
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break   
        if is_prime:
                primes.append(num)
    return primes         
n=30
prime = generate_prime(n)
print(prime)
# ------------------------ with allfunction ------------------------------------------
def genprime(n):
       return [i for i in range(2,n) if all(i % j != 0 for j in range(2, i))] 
print(genprime(20))
#=================================================================

# question_10 
def max_min(list1):
    maxnum = max(list1)
    minnum = min(list1)
    print (f"maximum num in list :{maxnum}\nminumu num in list :{minnum}")
list_ul = [74,5,6,8,4,2345,345]
max_min(list_ul)
#=================================================================

# question_11 

import math
def find_factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    # fact = math.factorial(n)?
    return fact 
n = 6
factorial = find_factorial(n)
print(factorial)
#=================================================================

# question_12

def check_palindrome(word):
    length = len(word)
    is_palindrome = True
    for i in range(length // 2):
        if word[i] != word[length -1 -i]:
            is_palindrome = False
            break
    if is_palindrome:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
text = "malayalam"
check_palindrome(text)

# --------------------------------------------------------------------------
def is_palindrome(word):
       length = len(word)
       return all(word[i] == word[length -1 -i] for i in range(length // 2))
print("pali  ",is_palindrome("aba"))
#=================================================================

# question_13

def isArmstrong(n):
    strN = str(n)
    tsum = 0
    count = len(strN)
    tsum = sum(int(i) ** count for i in strN)
    return tsum == n
print(isArmstrong(153)) 
# =================================================================

# question_14

def fibonacci_series(limit):
        a, b = 0, 1
        print(a, b, end=" ")
        while a + b <= limit:
                c = a + b
                print(c, end=" ")
                a, b = b, c
fibonacci_series(50)
print("\n0 1 1 2 3 5 8 13 21 34")
#=================================================================

# question_15

def sumOfAllprime(limit):
        if limit <=1:
                print("enter a greater number than one")
        sum = 0
        for i in range(2,limit+1):
                is_prime =True
                for j in range(2,i):
                        if i%j == 0:
                                is_prime = False
                                break
                if is_prime:
                        print(i, end=" ")
                        sum=sum+i
        return sum
n=10
totalSum = sumOfAllprime(n)
print(f"\nsum of all prime numbers : {totalSum}")
#=================================================================

# question_16

def sumOfMultiple3_5(limit):
        if limit <3:
                print("enter a number greater than 3")
                return 0
        sum=0
        for i in range(3,limit):
                if i % 3 == 0 or i% 5 == 0:
                        print(i ,end=" ")
                        sum+=i
        return sum
num = 16
totalSum = sumOfMultiple3_5(num)
if totalSum >=3:
        print(f"\ntotalSum :{totalSum}")
#=================================================================

# question_17

def sumOfAllEven(limit):
        sum = 0
        for i in range(limit):
                if i % 2 == 0:
                        print(i, end=" ")
                        sum += i
        return sum
num = 30
totalSum = sumOfAllEven(num) 
print(f"\ntotalSum : {totalSum}")
#=================================================================

# question_18

def setUnionList(list1, list2):
        union_set = set(list1) | set(list2)
        union_list = list(union_set)
        return union_list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
unitedlist = setUnionList(list1, list2)
print(unitedlist)
# ---------- with + operator --------
list3 = list1 + list2
print(list3)
#=================================================================

# question_19

def sumOfDigits(num):
        sum = 0
        numstr = str(num)
        for i in numstr:
                print(i ,end=" ")
                sum += int(i)
        return sum
n = 125 
digitSum = sumOfDigits(n)
print(f"\ndigits sum: {digitSum}")
#=================================================================

# question_20

def find_vowels(text):
        vowel="aeiouAEIOU"
        count =0
        for i in text:
                if i in vowel:
                        count+=1
        return count
text = "Iam a boy"
count = find_vowels(text)
print(f"count of vowels in text \"{text}\" is {count}")
#=================================================================






   








