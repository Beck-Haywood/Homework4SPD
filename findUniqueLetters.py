def findSubstring(string):
    arr = []
    current_longest = []
    for letter in string:
        if letter in arr:
            if len(current_longest) < len(arr):
                current_longest = arr
            arr = []
        arr.append(letter)
    return current_longest
print(findSubstring('qwerqtyuq u'))