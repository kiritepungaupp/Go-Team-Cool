def index_power(numnbers, n):
    if len(numnbers) < n+1:
        return -1
    power = 1
    for x in range(n):
        power *= numnbers[n]
    return power


print(index_power([1,2,3,4,5,6],4))