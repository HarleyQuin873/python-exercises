import os

f = open("isolamisteriosa.txt", "rb")
print(f.tell())
    
n = f.seek(119)
str= f.read(7)
print(str)

    # end = os.SEEK_END
    # print("end: ", end)
    # print("f(read(end)): " , f.read(end))

end = f.seek(-9,os.SEEK_END)
print(end)
str = f.read()
print(str)
f.close()   

#     p="quattro"
#     print(n)
    
#     for i in f:
#             for x in p:
#                 lettera = f.read(i)
#                 b = f.read(i,"rb+")
#                 print("lettera:", lettera)
#                 print("b: ", b)
#             #break
# finally:
#     f.close()

