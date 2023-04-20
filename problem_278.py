def first_bad_version(n):
    first, end = 0, n-1
    while first <= end:
        mid = first + end // 2
        if isBadVersion(mid):
            end = mid - 1
        else:
            first = mid+1