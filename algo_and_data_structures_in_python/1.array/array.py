# usually this is called an array - but in python it is called list
# if you want to use an array - then you use Numpy array
my_list = [1, 5, 10, 4]

print(my_list)

my_list_2 = ["Hello World", 10, 4.5] # mixed data type

print(my_list_2)

del my_list[0] # delete the first item

### Interview question

## Reverse an Array
    # Given an A array of integers - reverse this A array in linear running time using constant memory

# O(N) linear running time where N is the number of letter in string s N=len(s)
def reverse(nums):
    
    # pointing to the first itme
    start_index = 0
    # index of the last item
    end_index = len(nums)-1

    while end_index > start_index:

        # keep swapping the items
        nums[start_index], nums[end_index] =  nums[end_index], nums[start_index]

        start_index = start_index + 1
        end_index = end_index -1



n =  [1, 2, 3, 4]
reverse(n)
print(n)

## Palindrome of a string

# it has O(s) so basically linear running time complexity as far as the number
# of letters in the string is concerns
def palindrome_python(s):
    if s==s[::-1]: # s[::-1] reverse the order of the string
        return True
    
    return False

s = "madam"

print(palindrome_python(s))

## Integer reversion

def integer_reversion(n=1234):
    """
    We are after the last digit in every iteration
        We can get it with the modulo operator: the last digit is the remainder when dividing by 10

    We have to make sure we remove that digit from the original number 
        so we just have to divide the original number by 10

    Example of 1234:
        The first iteration
            remainder = 4, reversed_int = 4 and n = 123
        The second iteration
            remainder = 3, reverse_int = 43 and n = 12
        The third iteration
            remainder = 2, reverse_int = 432 and n = 1
        The forth iteration
            remainder = 1, reverse_int = 4321 and n = 0
    
    """

    reversed_int = 0
    remainder = 0

    while n > 0:
        remainder = n % 10 

        reversed_int = reversed_int * 10 + remainder
        
        n = n//10 # integer divdion

    return reversed_int

integer_reversion(1235)

## Anagram Problem

def is_anagram(str1, str2):
    """
    An anagram phrase or word formed by rearranging the letter
    of a different word or phrase - using all the original letter
    exactly once

        the original word or phrase is called the subject

        any word or phrase that exactly reproduces the letter
        in anothere order is an anagram

        for example:
            restful -> fluster

    if the length of the strings differ - they are not anagrams

    1. sort both words
    2. check each position if they match then is anagram

    The overall running time is O(NlogN)+O(N)=O(NlogN)
    """

    # if the length is different then they are not anagram
    if len(str1) != len(str2):
        return False
    
    # this is the bottleneck because it has O(NlogN)
    str1 = sorted(str1)
    str2 = sorted(str2)

    # after that we have to check the letters with the same indexes
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
        
    return True

s1 = list("fluster")
s2 = list("restful")
is_anagram(s1, s2)




