# takes as input a string that represents a list of type-indicated binary seperated strings
# ⟨𝚝𝚢𝚙𝚎𝚍_𝚊𝚛𝚛⟩ and outputs each element by its type and a human readable format
# • Input: ⟨𝚝𝚢𝚙𝚎𝚍_𝚊𝚛𝚛⟩ = ⟨ℤ⟩#⟨5⟩##⟨Σ
# ∗
# ⟩#⟨5⟩##⟨ℚ⟩#⟨
# 1
# 2
# ⟩
# • Output: Integer 5 \n String 0101 \n Rational 1/2
from fractions import Fraction
int_id=1 #identifier for integers
rat_id=2 #identifier for rationals
print("Enter Encoded word:")
def changeBinary(x):
    real=int(x,2)
    real1=str(real)
    return real1
encoded_string=input()
word_array=encoded_string.split("##")
for x in word_array:
    # decode words

