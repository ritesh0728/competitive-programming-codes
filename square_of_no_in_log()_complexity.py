
# squre log() complxity
def squre(n,pow):
    if pow==1:
        return n
    a=squre(n,pow//2)
    if pow%2:
        return n*a*a
    else:
        return a*a
print(squre(2,10))