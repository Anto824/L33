import time
from ess import *
from random import *

L = [1,2,3,4,5,6,7,8,9,10]
def perf_mix(f:callable):
    start = time.perf_counter()
    #print(f(L))
    f(L)
    end = time.perf_counter()
    elapsed = end-start
    return elapsed

def perf_sample(f:callable):
    n = randint(0,len(L)//2)
    start = time.perf_counter()
    #print(f(L,n))
    f(L,n)
    end = time.perf_counter()
    elapsed = end-start
    return elapsed



print(perf_mix(mix_list))
print(perf_mix(shuffle))
print('')

print(perf_sample(extract_elements_list))
print(perf_sample(sample))