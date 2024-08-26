def aliquot_successor(n):
    val = 0
    for i in range (1, n):
        if n%i == 0:
            val = val + i
    return val


def aliquot_sequence(n):
    lst = []
    x = n
    while aliquot_successor(x) not in lst:
        lst.append(aliquot_successor(x))
        x = aliquot_successor(x)
    return lst

def aliquot_pairs(alst):
    answer = []
    i = 0
    while i in range(len(alst)):
        x = alst[i]
        while [aliquot_successor(x),aliquot_successor(x)] not in answer:
            answer = answer + [[x,aliquot_successor(x)]]
            x = aliquot_successor(x)
        i = i + 1
    answer.sort()
    lst = []
    for i in range(len(answer)):
        if answer[i] not in lst:
            lst.append(answer[i])
    return lst
    
    return answer

        
print(aliquot_pairs([6,8,10,220]))

