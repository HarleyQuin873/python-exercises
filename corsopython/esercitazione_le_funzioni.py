# l1=[1,2,3,4,5,6,7]
# l2=[6,7,8,9,10,11,12]


# def listadif(l1,l2,*args):
#     l3 = []
#     return l3 = l1 - l2

a=[1,3,6,7]
b=[3,10]
def listadif(l1, l2=[1,2,3,4,5]):
    l=[]
    for x in l1:
        if not x in l2:
            l.append(x)
    return l

listadif(a,b)