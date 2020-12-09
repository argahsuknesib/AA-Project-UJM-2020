from operator import add
from time import time
import string
import random

def argmin(iterable):
    return max(enumerate(iterable), key=lambda x: -x[1])[0]

def string_generator(size=10, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


def editDistDP(s1, s2):

    m = len(s1)
    n = len(s2)
    colx = [x for x in range(m+1)]
    ry = [y for y in range(n+1)]

    for i in range(1,m+1):
        new_ry = []
        new_ry.append(colx[i])
        for j in range(1,n+1):

            
            if s1[i-1] == s2[j-1]:

                new_ry.append(ry[j-1])

            else:

                new_ry.append( 1 + min(new_ry[-1],       

                                   ry[j],       
                                   ry[j-1])     )   
        ry = new_ry
    return ry

def NmW(X,Y):
    edt2 = 0
    if len(X) == len(Y):
        if X!=Y:
            edt2+=1
        return (X,Y),edt2
    else:
        
        flip = False
        if len(X) > len(Y):
            temp = X
            X = Y
            Y = temp
            flip = True
        s1 = ""
        
        for charecter in Y:
            if charecter != X:
                s1 += '-'
                edt2+=1
            else:
                s1 += X
                
        if flip:
            return (Y,s1),edt2
        else:
            return (s1,Y),edt2
                
        
def Hb(X,Y):
    Z = ""
    W = ""
    
    if len(X) == 0:
        for i in range(len(Y)):
            Z = Z + ' -'
            W = W + Y[i]
        edt2 = len(Y)
    elif len(Y) == 0:
        for i in range(len(X)):
            Z = Z + X[i]
            W = W + ' -'
        edt2 = len(X)
    elif len(X) == 1 or len(Y) == 1:
        (Z,W),edt2 = NmW(X,Y)

        
    else:
        xlen = len(X)
        xmid = int(len(X)/2)
        ylen = len(Y)

        #Finding optimal partition for Y, corresponding to partition [X[0],X[xmid],X[-1]] 
        ScoreL = editDistDP(X[0:xmid], Y)
        ScoreR = editDistDP(X[xmid:][::-1], Y[::-1])
        ymid = argmin(  map(add, ScoreL, ScoreR[::-1])  )
 
        #Recursively calling on the two generated subproblems
        (z1,w1),ed1 = Hb(X[0:xmid], Y[0:ymid])
        (z2,w2),ed2 = Hb(X[xmid:], Y[ymid:])
        (Z,W) = z1 + z2, w1 + w2
        edt2 = ed1+ed2

    return (Z,W),edt2
