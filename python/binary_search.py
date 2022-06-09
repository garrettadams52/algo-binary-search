import random




def binary_search(num, val_arr):
    min = val_arr[0]
    max = val_arr[len(val_arr)-1]

    mid = (max+min)//2
    print(num, mid)

    if num != mid and len(val_arr) <= 1:
        return -1

    if num == mid:
        return True
    elif num > mid:
        val_arr = val_arr[len(val_arr)//2:]
        return binary_search(num,val_arr)
    elif num < mid:
        val_arr = val_arr[:len(val_arr)//2]
        return binary_search(num,val_arr)

    #print(val_arr)



values = random.sample(list(range(1,10000)), 1000)
values.sort() # We now have a sorted list of 1000 unique values between 1 and 10,000

print(binary_search(537, values), values) # this returns the index of 537 in values if it exists and -1 if it doesn't exist