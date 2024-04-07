def replace_last(numbers):
    
    if len(numbers) == 0:
        return []
    if len(numbers) == 1:
        return numbers 
    first_number = numbers.pop(0)
    replace = numbers.append(first_number)
    return numbers

