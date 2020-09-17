from numpy import *

m1=array([
          [1,2,3],
          [4,5,6],
          [7,8,9]

        ])
m2=array([
         [1,2,3],
         [2,3,4],
         [4,5,6]

        ])
result=array=([
          [0,0,0],
          [0,0,0],
          [0,0,0]
         ])
#this loop iterating the rows in m1
for i in range(len(m1)):
#this loop iteraing the columns in m2
    for j in range(len(m2)):
#this loop iterating the rows in m2
        for k in range(len(m2)):
            result[i][j]=result[i][j]+(m1[i][k]*m2[k][j])
for e in result:
    print(e)


list1=[1,2,3,4,5,6]
list2=list1[0:6:2]
print("list2 = {}".format(list2))
add=0
i=0
while i<len(list2):
    add=add+i
    i=i+1
print(add)





