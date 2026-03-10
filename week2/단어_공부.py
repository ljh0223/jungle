def sol():
    word=input().upper()
    counts={}
    for char in word:
        if char in counts:
            counts[char]+=1
        else:
            counts[char]=1

    max_count=0
    for val in counts.values():
        if val > max_count:
            max_count=val
    result=[]
    for key, val in counts.items():
        if val == max_count:
            result.append(key)
    if len(result)>1:
        print("?")
    else:
        print(result[0])

if __name__ == "__main__":
    sol()