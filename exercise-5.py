def reverse_ascending(numbers):
    temp_list = [numbers[0]]
    final_list = []
    for x in range(1,len(numbers)):

        if numbers[x] <= numbers[x-1]:
            final_list.append(temp_list)
            temp_list=[numbers[x]]
            continue
        temp_list.append(numbers[x])

    final_list.append(temp_list)
    finally_list = []
    for x in final_list:
        x.sort(reverse = True)
        finally_list = finally_list + x

    return finally_list


print(reverse_ascending([1,2,3,4,2,1,2,3]))
