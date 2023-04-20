# def isAnagram(str1, str2) -> bool:
#     if sorted(str1) == sorted(str2):
#         return True
#     return False



def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    for ch in set(s):
        print(set(s))
        if s.count(ch) != t.count(ch):
            return False
    return True 



print(isAnagram("anagram", "nagaram"))