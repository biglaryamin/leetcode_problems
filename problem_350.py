def intersect(nums1, nums2):
    output_list = []
    let = []
    for i, num1 in enumerate(nums1):
        for j, num2 in enumerate(nums2):
            if j in let:
                continue
            if num1 == num2:
                let.append(j)
                output_list.append(num1)
                break

    return output_list


print(intersect([1,2,2,1], [2,2]))