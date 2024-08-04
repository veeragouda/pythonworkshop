list = [0,1, 2, 3,3,4,5,6,7,7,8,10,12,15,18,20]

unique_list=[]
even =[]
odd = []

for i in list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)

for i in unique_list:
    if i % 2 ==0:
        even.append(i)

    if i % 2 !=0:
        odd.append(i)
# print(" raw list ", list)
print(" Unique list of numbers", unique_list)
print(" list of even numbers ", even)
print(" list of odd numbers ", odd)