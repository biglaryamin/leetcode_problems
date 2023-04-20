def merge_sort(list1,list2):
    new_list=[]
    for num1 in list1:
        new_list.append(num1)
    
    for num2 in list2:
        new_list.append(num2)
    

    return new_list



def test_merge_sort():
    assert([1,2,3],[4,5,6])==[1,2,3,4,5,6]
