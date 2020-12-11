'''

Advanced Algorithms Project.

This is the implementation of branch and
Bound Algorithm for 2 protein strings to find
the edit distance.

Done by ----> Kushagra Singh Bisen (M1 CPS2)

Arguments/Variables in this program are:
    1. string1 = the first protein string.
    2. string2 = the second protein string.
    3. bound = the parameter for bound and limitation edit distance.
    4. cost = the initial cost at root node will be zero.
'''
import string
import random
from time import time

def string_generator(size=10, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

def operations(al1, al2):
    print('************************************************************')
    print("The operation performed during branch and bound: \n")
    n = len(al1)
    for i in range(n):
        if al1[i] == "_":
            print("Deletion at index " + str(i))
        elif al2[i] == "_":
            print("Insertion " + al1[i] + " at index " + str(i))
        elif al1[i] != al2[i]:
            print("Substitution " + al1[i] + " for " + al2[i] + " at index " + str(i))

def branchAndBound(string1, string2, cost=0, bound=0):
    n = len(string1) 
    m = len(string2) 

    if n == 0 and m == 0:
        return 0, [], []

    if n == 0:
        return m, ["_" for i in range(m)], [string2[i] for i in range(m)]

    if m == 0:
        return n, [string1[i] for i in range(n)], ["_" for i in range(n)]

    weightx = abs((n - 1) - m)
    weighty = weightx + cost
    
    weightp = abs(n - (m - 1))
    weightq = weightp + cost

    weightw = abs((n - 1) - (m - 1))
    if string1[-1] == string2[-1]:
        weightm = weightw + cost - 1
    else:
        weightm = weightw + cost
    ad1, ad2, ai1, ai2, ac1, ac2 = [], [], [], [], [], []

    if bound >= weighty:
        deletion,ad1,ad2  = branchAndBound(string1[:-1], string2, cost + 1, bound)  # Deletion
        deletion += 1
    else:
        deletion = 1000000

    if bound >= weightq:
        insertion,ai1,ai2 = branchAndBound(string1, string2[:-1], cost + 1, bound)  # Insertion
        insertion += 1
    else:
        insertion = 1000000
    if bound >= weightw:
        if (string1[-1] != string2[-1]):
            substitution,ac1,ac2 = branchAndBound(string1[:-1], string2[:-1], cost + 1, bound) # substitution
            substitution += 1
        else:
            substitution,ac1,ac2 = branchAndBound(string1[:-1], string2[:-1], cost, bound)
    else:
        substitution = 1000000

    values = [deletion, insertion, substitution]
    minval = min(deletion, insertion, substitution)
    if values.index(minval) == 0:
        ad1 = ad1 + [string1[-1]]
        ad2 = ad2 + ["_"]
        return minval, ad1, ad2
    elif values.index(minval) == 1:
        ai1 = ai1 + ["_"]
        ai2 = ai2 +[string2[-1]]
        return minval, ai1, ai2
    else:
        ac1 = ac1 + [string1[-1]]
        ac2 = ac2 + [string2[-1]]
        return minval, ac1, ac2

if __name__ == "__main__":
    print('***********************************')
    print('Kushagra Singh Bisen M1 CPS2')
    print("Branch and bound for edit distance problem.")
    string1 = string_generator(8)
    string2 = string_generator(13)

    # string1 = "MSIVRRSNVFDPFADLWADPFDTFRSIVPAISGGGSETAAFANARMDWKETPEAHVFKADLPGVKKEEVKVEVEDGNVLVVSGERTKEKEDKNDKWHRVERSSGKFVRRFRLLEDAKVEEVKAGLENGVLTVTVPKAEVKKPEVKAIQISG"
    # string2 = "MWASAKIGGNYMKQTVRPTTLLESLFGDDFMNNAGYGTGVDIYREEGSYFVEIEMPGFEKEDIDIEFSGDILSIQATRRESEEKDEKNYFYRSRNQKNIKRQIRFAEVDANAIDASYQQGVLQITLPTKVEEHNSSKIRVQ"

    print("first string is ", string1)
    print("second string is ", string2)
    start_time=time()
    result, a1, a2  = branchAndBound(string1,string2,0,max(len(string1),len(string2)))
    print(a1,'\n',a2)
    print('\nThe edit distance is: ',result)
    end_time=time()
    print('The time taken to compute the edit distance is : %3f seconds'%(end_time-start_time))
    print(operations(al1=string1,al2=string2))
    print('\n')
    print('The program has ended. You can re-run the program with different values to recompute the strings.')
    print('and then finding the edit distance and computation.')
            


        
    

    






