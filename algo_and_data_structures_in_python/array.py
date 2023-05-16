# usually this is called an array - but in python it is called list
# if you want to use an array - then you use Numpy array
my_list = [1, 5, 10, 4]

print(my_list)

my_list_2 = ["Hello World", 10, 4.5] # mixed data type

print(my_list_2)

del my_list[0] # delete the first item

### Interview question

# Reverse an Array
    # Given an A array of integers - reverse this A array in linear running time using constant memory

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

# Palindrome

def palindrome_python(s):
    if s==s[::-1]: # s[::-1] reverse the order of the string
        return True
    
    return False

s = "madam"

print(palindrome_python(s))

print(n[::-1])
