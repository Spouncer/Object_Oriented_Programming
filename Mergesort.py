My_list = ['New', 3.55, 75.56, 'Happy', 2021, 2022, 'Year', 31, 1, 3455.7465]
test = [10, 6, 8, 9, 3, 4, 1, 7, 2, 5, 6, 6, 7, 9, 99, 37, 7.5, 4.564]
'''
# def merge(l1, l2):
#     j = 0
#     a = 0
#     print(l1, l2)
#     if  l1 == [] and l2 == []:
#         return 
#     elif l2 == []:
#         return l1
#     elif l1 == []:
#         return l2
    
#     else:
#         if j < len(l2):
#             while a < len(l1):
#                 if l2[j] <= l1[j]:
#                     l1.insert(j , l2[j])
#                     j += 1
#                 elif a+j >= len(l1):
#                         break
#                 elif l2[j] <= l1[a + j]:
#                     l1.insert(a + j , l2[j])
#                     j += 1
#         for l in l2[j:]:
#             l1.append(l)
#         return l1
'''

def merge(l1, l2):
    i = 0
    j = 0
    r = []
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1

    if l2[-1] <= l1[-1]:
        l2.append(l1[-1])
        
    else:
        l1.append(l2[-1])

    n = len(l1) + len(l2)
    
    for a in range(n - 1):
        if l1[i] <= l2[j]:
            r.append(l1[i])
            if i < len(l1) - 1:
                i += 1
            
        else:
            r.append(l2[j])
            if j < len(l2) - 1:
                j += 1
            
    
    return r


def Mergesort(list):

    n = len(list)
    ind = int(n/2)
    half_1 = list[:ind]
    half_2 = list[ind:]
        
    if n > 2:
        
        l1 = Mergesort(half_1)
        l2 = Mergesort(half_2)
        
        return merge(l1, l2)

    else:
        return merge(half_1, half_2)


    
print(Mergesort(test))

strings = [ 'f', 'b', 'a', 'e', 'c', 'd']


print(Mergesort(strings))


import random
import time

list = random.sample(range(1, 10**8), 10**6)

t0 = time.time()
Mergesort(list)
t1 = time.time() - t0
print(t1)

# def type_sort(list):
#     string = []
#     integer = []
#     flo = []
    