import time
def merge_two_list(list1 , list2):
    start_time=time.milll   
    new_list=[]
    for num1 in list1:
        new_list.append(num1)
    for num2 in list2:
        new_list.append(num2)

    new_list.sort()


    return new_list




def test_function():
    assert merge_two_list([1,2,4,7],[3,5,7,8])==[1,2,3,4,5,7,7,8]


test_function()