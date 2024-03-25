def chunking_by(numbers, chunk):
    counter = 0
    final_list = []
    tempo_list = []
    if len(numbers)/chunk == round(len(numbers)/chunk):
        itteration = round((len(numbers)/int(chunk)))
    else:
        itteration = round((len(numbers)/int(chunk)))+1
    
    for x in range(itteration):
        tempo_list = []
        for y in range(chunk):
            try:
                tempo_list.append(numbers[counter])
                counter +=1
            except:
                continue
        final_list.append(tempo_list)
    final_final_list = []
    for x in final_list:
        if len(x) > 0:
            final_final_list.append(x)
    return final_final_list

print(chunking_by([1,2,3,4,5],3))
