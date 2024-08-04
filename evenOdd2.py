list = [0,1, 2, 3,3,4,5,6,7,7,8,10,12,15,18,20]

unique_list=[]
even =[]
odd = []
count=0

for i in list:
    if i % 2 ==0:
        even.append(i)

    if i % 2 !=0:

        odd.append(i)
for i in list:
    count=count+1

print(" Unique list of numbers", unique_list)
print(" list of even numbers ", even,"even numbers counts : ",len(even))
print(" list of odd numbers ", odd, "odd number counts : ", len(odd))
print(" count numbers", count)
