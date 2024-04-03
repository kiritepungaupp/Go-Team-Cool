def remove_all_after(numbers, n):
    if numbers and n in numbers:
        index = numbers.index(n)
        return numbers[max(index - 2, 0):index + 1]
    else:
        return numbers
    
numbers = [1, 2, 3, 4, 5]
n = 3

result = remove_all_after(numbers, n)
print(result)