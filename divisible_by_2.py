def prime_number(a):
    i=0
    while i<len(a):
        if a[i]%2==0:
            print a[i]
        i=i+1
a=[2,3,4,24,45,6,7,8,14,8]
prime_number(a)