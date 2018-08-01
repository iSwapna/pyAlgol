def find_the_missing_number(set_of_nums):

    max_num = set_of_nums.__len__() + 1
    sum_nums = 0
    
    for num in set_of_nums:
        sum_nums += num

    return max_num * (max_num + 1)/2 - sum_nums
        
if __name__ == "__main__":
    assert(find_the_missing_number({1,3,4,5,6}) == 2)
    #print(find_the_missing_number({3,2,1,5,6,7,8}))
