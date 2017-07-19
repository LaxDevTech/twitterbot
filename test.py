# this is a logic test
arr = [1,2,3]
for i in range(0,5):
    print(arr)
    try: prev
    except:
        prev = None
    cur = arr[0]
    print("prev" + str(prev))
    if prev == cur:
       print("No change")
    else:
        print("change")
    prev = cur 
    print(i)
    arr[0] = i
