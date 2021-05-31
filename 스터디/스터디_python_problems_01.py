X=int(input())
Y=int(input())
if (0<X<=1000) and (0<Y<=1000):
    print('1')
if (-1000<=X<0) and (0<Y<=1000):
    print('2')
if (-1000<=X<0) and (-1000<=Y<0):
    print('3')
if (0<X<=1000) and (-1000<=Y<0):
    print('4')
