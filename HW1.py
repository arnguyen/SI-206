#The goal of this homework is to practice basic debugging

# fix compiler errors in the code below.  It should print the string Hello World
def print_hello_world():
    print("Hello World")

# fix compiler errors in the code below.  It should print the variable twice
def print_twice(word):
    print(word)
    print(word)

# fix compiler errors in the code below.  It should print "Even" if even and
#"Odd" if odd
def even_or_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

# fix errors in the code below.  It should return the number of times the target is found in the list
def count_target(num_list, target):
    total = 0
    for num in num_list:
        if num == target:
            total += 1
    return total

# fix errors in the code below.  It should return the number of negative numbers in the list.
def count_neg(num_list):
    count = 0
    for num in num_list:
        if num < 0:
            count += 1
    return count
    
# fix the following to return true when the first and last item in a list
# are the same value and false otherwise
def values_match(nums):
    return nums[0] == nums[-1]

# fix the function below to work correctly
# >= 90 should print A
# >= 80 should print B
# >= 70 should print C
# >= 60 should print D
# otherwise print E
def calc_grade(total):
    if total >= 90:
        print("A")
    elif total >= 80:
        print("B")
    elif total >= 70:
        print("C")
    elif total >= 60:
        print("D")
    else:
        print("E")

# Loop printing the numbers from 10 to 5 (inclusive)
def print_liftoff():
    for x in range(10, 4, -1):
        print(x)

# Return true if all the values are positive and false otherwise
def check_all_positive(num_list):
    for num in num_list:
        if num < 0:
            return False
    return True

# Return the index of the maximum value in the list
def getIndexMaximum(numList):

    # init the maximum
    maximum = numList[0]
    max_index = 0

    # loop through the rest of the list
    for index in range(1, len(numList)):

        # get current at index
        current = numList[index]

        # if new max
        if current > maximum:

            # reset max
            maximum = current
            max_index = index

    return max_index

# testing the print_hello_world function - should print "Hello World"
print("testing print_hello_world")
print_hello_world()
print("")

# testing the print_twice function - should print "Hi" twice
print("testing print_twice")
print_twice("Hi")
print("")

# testing the even_or_odd function
# it should print Odd first and then Even
print("testing even_or_odd")
even_or_odd(5)
even_or_odd(4)
print("")

# testing the count target in list.  
# it should print 3 and 0
print("testing count_target")
print(count_target([1,1,2,3,2,2], 2))
print(count_target([1,1,2,3,2,2], -3))
print("")

# testing the count of negative numbers in a list
# it should print 0 and 3
print("testing count_neg")
print(count_neg([1, 3, 90, 2038]))
print(count_neg([-1, 3, -5, 2, -9]))
print("")

# testing the values_match function - should print False, True
print("testing values_match")
print(values_match([1,2,2]))
print(values_match([1,2,1]))
print("")

# testing the calc_grade function - should print A, B, C, D, E
print("testing calc_grade")
calc_grade(95)
calc_grade(82)
calc_grade(78)
calc_grade(60)
calc_grade(59)
print("")

# testing the countdown function - should print 10, 9, 8, 7, 6, 5
print("testing print_liftoff")
print_liftoff()
print("")

# testing check_all_positive - should print True and False
print("testing check_all_positive")
print(check_all_positive([3, 2, 1]))
print(check_all_positive([1, -2, 1]))
print("")

# testing the getIndexMaximum - should print 0 and 2
print("testing getIndexMaximum")
print(getIndexMaximum([50, 32, 20]))
print(getIndexMaximum([-30, 20, 90]))
print("")

