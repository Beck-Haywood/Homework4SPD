#Given a list of n numbers, determine if it contains any duplicate numbers.
def findUnique(numbers)
    arr = []
    for number in numbers
        if number not in arr:
            arr.append(number)
        else:
            return True
       return False