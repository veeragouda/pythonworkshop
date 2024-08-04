text=input("enter the word : ")
vowel=[]
for i in text:
    if i in "aieouAEIOU":
        vowel.append(i)
        print(i)  # Print each vowel

print("Vowels in the text:", vowel)
print("no of vowels :",len(vowel))

