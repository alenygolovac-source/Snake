
# примитивные типы данных - int, str, bool, float ...
# ссылочный тип данных - list,dict ...

# def test(num): # num = 1 #ewq
#     num += 1 #ewq


# num = 1    #qwe
# test(num)  #test(1)  # 1 !!!!
# print(num) #qwe

# def test(num): # num = #qwe
#     num[0] += 1 #qwe

# num = [1]   #qwe
# test(num)   #test(#qwe) # #qwe !!!!
# print(num) #qwe


#import random

#num = random.randint(1,3)
#print(num)



"""
    Вывести 1 рандомное число и листа
"""

import random
#       0 1 2 3 4 5 6 
# nums = [8,5,0,6,8,4,5]

# idx = random.randint(0,6)

# print(nums[idx])


nums = [
    [4,1,2],
    [7,8,4]
]

idx1 = random.randint(0,1)
idx2 = random.randint(0,2)

print(nums[idx1][idx2])