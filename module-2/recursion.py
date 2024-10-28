# Joseph Ayo, October 11th, 2024. Module 11.2 Assignment
# The purpose of this program is to create two functions, one that is 
# recursive, and one that is non-recursive. Both of these functions should
# print the number of 1's, up to and including n.
# Sources: Gaddis Python 6e Chapter 12 +  Slideshow (Module 11 Readings)
def recursive(n):
    # In this recursive function, our solution to this problem is very simple.
    # In order to print all numbers in between 1 and n, we will run the function,
    # subtracting 1 from n until n is equal to 1. Each time we run this function,
    # we will print n, giving us every number in between 1 and n.
    if n > 1:
        recursive(n-1)
    print(n)

def non_recursive(n):
    # In this non-recursive function, our solution to this problem is also quite
    # simple. In order to print all numbers in between 1 and n, we will run a loop,
    # subtracting 1 from n until n is equal to 1. Each time this loop iterates,
    # we will print i, which is a variable which will cycle through every value 
    # in between 1 and n+1, 
    # which will give us every number between 1 and n.
    for i in range(1, n + 1):
        print(i)

def main():
    # Input validation to ensure that n is a positive integer
    n = int(input("Enter a positive integer (greater than 0): "))
    if n <= 0:
        return print("Input must be greater than 0.")

    # Using the recursive function
    print(f"Demonstrating recursive function with n = {n}")
    recursive(n)

    # Using the non-recursive function
    print(f"Demonstrating non-recursive function with n = {n}")
    non_recursive(n)

main()