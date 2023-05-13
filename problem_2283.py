def digitCount(num: str) -> bool:
    for i in range(len(num)):
        if int(num[i]) != num.count(str(i)):
            return False
    return True