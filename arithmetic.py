from collections import *
import numpy as np
print("Arithmetic Encoding and Decoding")
print("=============================================")
h = int(input("Enter 1 if you want to enter in command window, 2 if you are using some file:"))
if h == 1:
    string = input("Enter the string you want to compress:")
elif h == 2:
    file = input("Enter the filename:")
    with open(file, 'r') as f:
        string = f.read()
else:
    print("You entered invalid input")

res = Counter(string) # counter from collections
print(str(res))
m = len(res)
print(m)
N = 5
a = np.zeros((m,5),dtype=object)

keys = list(res.keys())
value = list(res.values())
total = sum(value)

# Creating Table

a[m-1][3] = 0
for i in range(m):
   a[i][0] = keys[i]
   a[i][1] = value[i]
   a[i][2] = ((value[i]*1.0)/total)
i=0
a[m-1][4] = a[m-1][2]
while i < m-1:
   a[m-i-2][4] = a[m-i-1][4] + a[m-i-2][2]
   a[m-i-2][3] = a[m-i-1][4]
   i+=1
print(a)

# Encoding
# Lower Range, Upper Range and Tag using dict

print("===Encoding===" )
strlist = list(string)
Lenco = []
Uenco = []
Lenco.append(0)
Uenco.append(1)

for i in range(len(strlist)):
    result = np.where(a == keys[keys.index(strlist[i])])
    llistadd = (Lenco[i] + (Uenco[i] - Lenco[i])*float(a[result[0],3]))
    ulistadd = (Lenco[i] + (Uenco[i] - Lenco[i])*float(a[result[0],4]))

    Lenco.append(llistadd)
    Uenco.append(ulistadd)

    tag = (Lenco[-1] + Uenco[-1])/2.0

Lenco.insert(0, " Lower Range")
Uenco.insert(0, "Upper Range")
print(np.transpose(np.array(([Lenco],[Uenco]),dtype=object)))
print("The Tag is",tag)

# Decoding

print("===Decoding===" )
ltag = 0
utag = 1
decoded_string = []
for i in range(len(string)):
    decodenum = ((tag - ltag)*1.0)/(utag - ltag)
    for i in range(m):
        if (float(a[i,3]) < decodenum < float(a[i,4])):

            decoded_string.append(str(a[i,0]))
            ltag = float(a[i,3])
            utag = float(a[i,4])
            tag = decodenum

print("The decoded Sequence is:","".join(decoded_string))
