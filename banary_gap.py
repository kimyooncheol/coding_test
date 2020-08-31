test_cases = [1042,15,32,9,529]

def solution(N):
    binarys = bin(N).replace('0b', '')
    binarygaps = []
    max_binarygap = 0
    count = 0
    for binary in binarys:
        if int(binary) == 0:
            count += 1
        if int(binary) == 1:
            if count > max_binarygap:
                max_binarygap = count
                count = 0
            else:
                count = 0
    return max_binarygap
    
for test_case in test_cases:
    print(test_case,':',solution(test_case))
    
"""
  https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
"""
