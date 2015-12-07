from symbol import break_stmt


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


'''
#----------------------------------------#
Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

def question_17():
    depositKey = 'D'
    withdrawalKey = 'W'
    accHistory = {depositKey: [], withdrawalKey: []}

    while True:
        transaction = input()
        if not transaction:
            break
        else:
            transactionData = transaction.split()
            assert len(transactionData) == 2
            if not transactionData[0] in accHistory:
                continue
            accHistory.get(transactionData[0]).append(int(transactionData[1]))

    netVal = sum(x for x in accHistory.get(depositKey)) - sum(y for y in accHistory.get(withdrawalKey))
    print('Net value = {:d}'.format(netVal))


'''
#----------------------------------------#
Question 18
Level 3

Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
def question_18():

    def is_valid_length(passw):
        return len(passw) >= 6 and len(passw)  <= 12

    def match_rule(pattern, passw):
        import re
        return re.search(pattern, passw)

    patterns = ('[a-z]','\d+','[A-Z]','[$#@]','^(?!.*\s).*$')

    inputPasswords = input().split(',')

    for psw in inputPasswords:
        containsAllSymbols = True

        for pattern in patterns:
            if not match_rule(pattern, psw):
                containsAllSymbols = False
                break

        if containsAllSymbols and is_valid_length(psw):
            print(psw)

'''
#----------------------------------------#
Question 19
Level 3

Question:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string,
age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use itemgetter to enable multiple sort keys.
'''
def question_19():
    from collections import namedtuple
    import operator
    Student = namedtuple('Student', 'name age score')

    students = list()

    while True:
        s = input()
        if not s:
            break
        else:
            studentData = s.split(',')
            assert len(studentData) == 3
            students.append(Student(studentData[0],
                                    studentData[1],
                                    studentData[2]))

    students.sort(key=operator.attrgetter('name','age','score'))
    print(students)

'''
#----------------------------------------#
Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
'''
class Simple7BaseGenerator(object):

    def __init__(self, n):
        limit = n
        current = 0

    def gen_7_base_num(self):
        while self.current < self.limit:

# help(re)




















































































































    



















        
        
