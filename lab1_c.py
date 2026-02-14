# b) takes as input an integer 𝑘, and outputs the binary string ⟨𝑘⟩ as from the notes, and a binary
# type identifier as an integer
# • 𝑃(⟨𝑘⟩10
# ) = ⟨ℤ⟩#⟨𝑘⟩
# c) repeats the previous question but for the rationals ℚ, a string Σ
# ∗
# , a symbol Σ
# • Given that we are now using # to seperate our list, and our type hints, how can we represent
# both simultaneously and without a collision of meaning?
from fractions import Fraction
int_id=1 #identifier for integers
rat_id=2 #identifier for rationals
print("enter a rational number!")

x=input()
rat_input=Fraction(x)
if rat_input.denominator==1:
    rat_id=1
print(str(rat_id)+"#"+bin(rat_input.numerator)+"#"+bin(rat_input.denominator))



