
def question_1():
    candidates = []
    for c in range(2000, 3201):
        if c % 7 == 0 and not c % 5 == 0:
            candidates.append(str(c))
    print (','.join(candidates))

def _factorial(n):
    if n == 0:
        return 1
    else:
        return n * _factorial(n - 1)

def question_2():
    n = int(input())
    print(_factorial(n))

def question_3():
    n = int(input())
    dict = {}
    for i in range(1, n + 1):
        dict[i] = i * i
    
    print(dict)

def question_4():
    nums = str(input())    
    l = nums.split(',')
    print(l)
    print(tuple(l))


class Question5Class(object):

    def __init__(self):
        self.word = ""
    
    def getString(self):
        self.word = input()
        
    def printString(self):
        print(self.word.upper())

def question_5():
    o = Question5Class()
    o.getString()
    o.printString()

'''
#----------------------------------------#
Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example,
if the output received is 26.0, it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input. '''        
    
C = 50
H = 30

def question_6():
    values = [x for x in input().split(',')]
    result = list()
    for d in values:
        q = ((2 * C * int(d)) / H) ** 0.5
        result.append(str(int(q)))
    print(','.join(result))    

'''
#----------------------------------------#
Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] '''

def question_7():
    dimensions = [int(x) for x in input().split(',')]
    assert len(dimensions) == 2
    result = [[x * y for x in range(dimensions[1])] for y in range(dimensions[0])]
    print(result)
    

'''
#----------------------------------------#
Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

def question_8():
    words = input().split(',')
    words.sort()
    print(words)

'''
#----------------------------------------#
Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
def question_11():
    numbers = [x for x in input().split(',') if int(x,2) % 5 == 0]
    print(''.join(numbers))

'''
#----------------------------------------#
Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
def question_12():
    result = []
    for n in range(1000,3001):               
        temp = n
        while temp > 1:                
            if temp % 2 != 0:
                break            
            temp //= 10             
        if temp < 1:
            result.append(n)
    print(result)

'''
#----------------------------------------#
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
import re

def question_13():
    phrase = input()
    lettersRegex = re.compile(r'[A-Z]', re.IGNORECASE)
    lettersCnt = sum(1 for n in lettersRegex.finditer(phrase))
    numbersRegex = re.compile(r'\d')
    numbersCnt = sum(1 for n in numbersRegex.finditer(phrase))
    print('LETTERS {:d}'.format(lettersCnt))
    print('DIGITS {:d}'.format(numbersCnt))

'''
#----------------------------------------#
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

def question_14():
    sentence = input()
    upperCaseRegex = re.compile(r'[A-Z]')
    lowerCaseRegex = re.compile(r'[a-z]')
    upperCaseCnt = sum(1 for n in re.finditer(upperCaseRegex, sentence))
    lowerCaseCnt = sum(1 for n in re.finditer(lowerCaseRegex, sentence))
    print('UPPER CASE {:d}'.format(upperCaseCnt))
    print('LOWER CASE {:d}'.format(lowerCaseCnt))

'''
#----------------------------------------#
Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
def question_15():
    a = input()
    expression = 'a+aa+aaa+aaaa'.replace(r'a', a)
    print(eval(expression))

'''
#----------------------------------------#
Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1, 9, 25, 49, 81

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
def question_16():
    inputList = input().split(',')
    outputList = [int(x)**2 for x in inputList if int(x) % 2 == 1]
    print(','.join(outputList))













































































































    



















        
        
