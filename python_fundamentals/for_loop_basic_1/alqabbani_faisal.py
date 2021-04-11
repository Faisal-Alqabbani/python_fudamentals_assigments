# Basic - Print all integers from 0 to 150.
def print_form_1_to_150():
    for i in range(1,151):
        print(i)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
def multiples_of_five():
    for i in range(5,1001):
        if i % 5 == 0:
            print(i)
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
def counting_the_dojo_way():
    for i in range(1, 101):
        if i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 ==0:
            print("Coding")

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
def sucker_huge():
    sum = 1
    for i in range(500001):
        sum += i
    print("The numbers sum is", sum)
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
def countdown_by_fours():
    for i in range(2018, 0, -4):
        print(i)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def flexible_counter():
    low_num = 2
    high_num = 9
    mult = 3
    for i in range(low_num + 1, high_num + 1, mult):
        print(i)
        
flexible_counter()
