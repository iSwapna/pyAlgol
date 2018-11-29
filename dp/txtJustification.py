# Word justification
def text_justify(txt, page_width):
    MAX_VAL = page_width ** 3
    N = len(txt)
    def badness(start, end):
        total_length = sum(map(len, txt[start: end]))
        total_length += end - start - 1
        if total_length > page_width:
            return MAX_VAL
        else:
            return (page_width - total_length) ** 3

    DP = [page_width ** 3 for _ in range(len(txt) + 1)]
    DP[-1] = 0
    parent = [0 for _ in txt]
    
    def justify(idx):
        if DP[idx] < MAX_VAL:
            return DP[idx]

        for i in range(idx, N):
            for j in range(i + 1, N + 1):
                if badness(i, j) == MAX_VAL:
                    break
                res = badness(i, j) + justify(j)
                if res < DP[i]:
                    DP[i] = res
                    parent[i] = j

        return DP[idx]
                    
    justify(0)
    result = []
    #uncomment to see parent pointers for reconstruction
    #print(parent)
    i = 0
    while i < len(txt):
        result.append(' '.join(txt[i: parent[i]]))
        i = parent[i]
    return result

print(text_justify(['blah', 'blah', 'blah', 'blah', 'reallylongword'], 14))
print(text_justify(['blah', 'blah', 'blah', 'blah', 'reallylongword', 'blah', 'blah', 'blah'], 14))
print(text_justify(['blahs', 'blah', 'blah', 'blah', 'reallylongword', 'blah', 'blah', 'blah', 'blah'], 14))
                   
                    
    
