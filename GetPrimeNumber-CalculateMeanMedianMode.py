# Read the List of values from Input, filter the Prime Numbers and output mean, median and mode values
def prime_test(number):
    """ prime_test function finds if the list given is prime number

        Args:
          number: an input values from the list

        Returns:
        True value if the number is prime or False value if the number is not prime
        """
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    i = 3
    sqrtofnumber = int(number ** 0.5)

    while i <= sqrtofnumber:
        if number % i == 0:
            return False
        i = i + 2

    return True


# Get the Median Value
def median(num_list):
    """
    gets the median value of the given list
    Args:
    num_list: an input values from the list
    Returns:
    median value of the given list
    """
    length = len(num_list)
    if length % 2 != 0:
        return num_list[int(length / 2)]

    elif length == 1:
        return num_list[0]
    else:
        return (num_list[int(length / 2) - 1] + num_list[int(length / 2)]) / 2


# Main Program to read the values, sort the prime numbers in the given list and
# then print mean, median, mode by grouping the list with 3 values.
# Input Sample: 5,10,25,27,13,5,7,71,11,101,12,13,29,103
liststr = input()
liststr = liststr[0:len(liststr)]
listt = liststr.split(",")
numbers = []
for caselistt in listt:
    numbers.append(int(caselistt))


prime = sorted([num for num in list(set(numbers)) if prime_test(num)])

x = True
while x:
    min_num = min(prime)
    prime.remove(min_num)

    if len(prime) < 2:
        x = False

        if len(prime) != 0:
            print(min_num, max(prime), max(prime))
        else:
            print(min_num)
        break;

    med = int(median(prime))
    max_num = max(prime)
    prime.remove(max_num)
    print(min_num, med, max_num)