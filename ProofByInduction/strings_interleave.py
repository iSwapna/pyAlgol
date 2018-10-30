def doStringsInterleave(a, b, il):
    print('a sz:', len(a), 'b sz:', len(b), 'il sz:', len(il))
    i, j = 0, 0
    rem = ''
    while i < len(a) and j < len(il):
        if a[i] == il[j]:
            i += 1
            j += 1
        else:
            rem += il[j]
            j += 1
                
    if i != len(a):
        print('a', a[i:])
        return False
        
    #extract mismatch chars
    rem += il[j:]
    i, j = 0, 0
    rem2 = ''
    rem_b = ''
    while i < len(b):
        if b[i] != rem[i]:
            rem2 += rem[i]
            rem_b += b[i]
        i += 1
         
    if rem != b:   
        print('rem2', rem2)
        print('b_diff', rem_b)
        return False
        
    return True
                
