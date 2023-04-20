def get_intersection(nums1, nums2):
    """Given two arrays, write a function to compute their intersection."""
    intersections = []

    for num1 in nums1:
        for num2 in nums2:
            if num1 == num2:
                if num1 not in intersections:
                    intersections.append(num1)
    

    return intersections



print(get_intersection([2,2], [1,2,2,1]))



