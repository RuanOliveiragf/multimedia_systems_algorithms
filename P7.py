def compress_zeros(input_string):
    result = []
    count = 0
    
    for char in input_string:
        if char == '0':
            count += 1
        else:
            if count > 0:
                result.append(f"@{count}")
                count = 0
            result.append(char)
    
    if count > 0:
        result.append(f"@{count}")
    
    return ''.join(result)


input = input()

comp = compress_zeros(input)
print(comp)
