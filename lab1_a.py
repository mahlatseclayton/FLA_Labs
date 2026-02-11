#a) takes as input a list arr of integers and outputs the resulting binary seperated string ⟨arr⟩
# • 𝑃(⟨𝚊𝚛𝚛⟩) = ⟨𝚊𝚛𝚛[0]⟩#⟨𝚊𝚛𝚛[1]⟩#⟨𝚊𝚛𝚛[2]⟩#…
arrInt=[1,2,3,4,5,6,7]
encodedArr=[]
for i in range(len(arrInt)):
    encodedArr.append(bin(arrInt[i]))
finalString=""
for i in range(len(encodedArr)):
    finalString+=encodedArr[i]+"#"
if finalString=="":
    print("empty integer array")

else:
    print(finalString)
