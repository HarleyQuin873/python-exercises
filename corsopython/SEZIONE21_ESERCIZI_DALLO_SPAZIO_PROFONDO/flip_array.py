def getMinOperations(arr):
    n=len(arr)
    MAX_BITS=31 #perchè arr[i] < 1e9

    total_ops = 0

    for b in range(MAX_BITS):
        ones = 0
        for x in arr:
            if(x>>b) & 1:
                ones += 1
        zeros = n - ones
        total_ops += min(ones, zeros)
    
    return total_ops

print(getMinOperations([5, 5]))          # → 0
print(getMinOperations([7, 6, 10, 11]))  # → 6