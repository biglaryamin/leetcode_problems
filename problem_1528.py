def restoreString(s: str, indices: List[int]):
    res = [''] * len(s)
    for i in range(len(s)):
        res[indices[i]] = s[i]
    return ''.join(i for i in res)