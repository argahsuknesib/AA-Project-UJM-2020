
from time import time
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import string
import random

import BranchAndBound
import DivideAndConquer
import Dynamic

def string_generator(size=100, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

firstString = string_generator(8)
secondString = string_generator(13)


# firstString = "MSIVRRSNVFDPFADLWADPFDTFRSIVPAISGGGSETAAFANARMDWKETPEAHVFKADLPGVKKEEVKVEVEDGNVLVVSGERTKEKEDKNDKWHRVERSSGKFVRRFRLLEDAKVEEVKAGLENGVLTVTVPKAEVKKPEVKAIQISG"

# secondString = "MWASAKIGGNYMKQTVRPTTLLESLFGDDFMNNAGYGTGVDIYREEGSYFVEIEMPGFEKEDIDIEFSGDILSIQATRRESEEKDEKNYFYRSRNQKNIKRQIRFAEVDANAIDASYQQGVLQITLPTKVEEHNSSKIRVQ"

print("{:<20}".format("First String  :"),firstString)
print("{:<20}".format("Second String :"),secondString)
  
print("Implementation by : Kushagra Singh Bisen")
print("--------- Branch and Bound ---------")
time_start = time()
result, a1, a2 =BranchAndBound.branchAndBound(firstString,secondString,0,max(len(firstString),len(secondString)))
print("{:<20}".format("Edit distance:"),result)
time_end = time()
time_branch = time_end - time_start
print("The time taken for the computation is %3f seconds." %(time_branch))
print("{:<20}".format("Sequence Alignment :"),a1,"\n",a2)

print('-------LINE-----BREAK------')

print("Implementation by : Anasuya Dasgupta")
print("--------- Divide and Conquer ---------")
time_start = time()
(Z,W),ed = DivideAndConquer.Hb(firstString,secondString)
print("{:<20}".format("Edit distance :"),ed)
time_end = time()
time_divide = time_end - time_start
print("The time taken for the computation is %3f seconds." %(time_divide))
print("{:<20}".format("Sequence Alignment :"),(Z,W))

print('---------LINE------BREAK-------')

print('Java and Python comparison code.')
print("--------- Dynamic Programming ---------")
time_start = time()
ed = Dynamic.editDistDp(firstString,secondString)
print("{:<20}".format("Edit distance :"),ed)
time_end = time()
time_dynamic = time_end - time_start
print("{:<20}".format("The time taken for the execution is %3f") %(time_dynamic), "seconds") 


params = {'legend.fontsize': 'x-small',
          'figure.figsize': (6, 6),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}

pylab.rcParams.update(params)
plt.figure(' Algorithms Time')
plt.plot([time_branch, time_divide, time_dynamic])
plt.text(0,time_branch, "Branch and Bound")
plt.text(1,time_divide, "Divide")
plt.text(2, time_dynamic, "Dynamic")
plt.ylabel('Time (seconds)')
plt.xlabel('Algorithms')
plt.show()

